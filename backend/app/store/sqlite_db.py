"""
SQLite document store: one file, WAL mode, safe for one process with many threads.
Documents are JSON; collections are plain strings (so 'users' and 'users/u1/activity' never mix).
Mount DB_PATH's folder as a Docker volume so data survives container restarts and rebuilds.
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import threading
import time
from typing import Any, Optional

from .base import Database, _sort_key

_IDENT = re.compile(r"^[A-Za-z0-9_]+$")


class SqliteDatabase(Database):
    name = "sqlite"

    def __init__(self, path: str) -> None:
        self.path = path
        if path != ":memory:":
            os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
        self._lock = threading.RLock()
        self.conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None, timeout=30)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=NORMAL")
        self.conn.execute("PRAGMA busy_timeout=30000")
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS docs (collection TEXT NOT NULL, id TEXT NOT NULL, data TEXT NOT NULL, "
            "updated REAL NOT NULL, PRIMARY KEY (collection, id)) WITHOUT ROWID")

    def close(self) -> None:
        with self._lock:
            try:
                self.conn.close()
            except Exception:
                pass

    # ---------- basic ops ----------
    def get(self, collection, doc_id) -> Optional[dict]:
        with self._lock:
            r = self.conn.execute("SELECT data FROM docs WHERE collection=? AND id=?", (collection, doc_id)).fetchone()
        return json.loads(r[0]) if r else None

    def put(self, collection, doc_id, data) -> dict:
        blob = json.dumps(data, ensure_ascii=False, default=str)
        with self._lock:
            self.conn.execute("INSERT OR REPLACE INTO docs (collection, id, data, updated) VALUES (?,?,?,?)",
                              (collection, doc_id, blob, time.time()))
        return data

    def delete(self, collection, doc_id) -> None:
        with self._lock:
            self.conn.execute("DELETE FROM docs WHERE collection=? AND id=?", (collection, doc_id))

    # ---------- queries ----------
    def _sql_parts(self, filters: dict) -> tuple[str, list, dict]:
        """Filters on str/int fields are pushed into SQL; everything else is filtered in Python."""
        clauses, args, py = [], [], {}
        for k, v in filters.items():
            if _IDENT.match(k) and isinstance(v, (str, int)) and not isinstance(v, bool):
                clauses.append(f"json_extract(data, '$.{k}') = ?")
                args.append(v)
            else:
                py[k] = v
        return (" AND " + " AND ".join(clauses)) if clauses else "", args, py

    def query(self, collection, **filters) -> list[dict]:
        return self.query_ex(collection, filters)

    def query_ex(self, collection, filters=None, order_by=None, desc=False, limit=None) -> list[dict]:
        filters = filters or {}
        where, args, py = self._sql_parts(filters)
        sql = "SELECT data FROM docs WHERE collection=?" + where
        sql_order = bool(order_by and _IDENT.match(order_by))
        if sql_order:
            sql += f" ORDER BY json_extract(data, '$.{order_by}') IS NULL, json_extract(data, '$.{order_by}') {'DESC' if desc else 'ASC'}"
        if limit and not py:
            sql += " LIMIT ?"
            args = args + [int(limit)]
        with self._lock:
            rows = self.conn.execute(sql, [collection] + args).fetchall()
        out = [json.loads(r[0]) for r in rows]
        for k, v in py.items():
            out = [d for d in out if d.get(k) == v]
        if order_by and not sql_order:
            out.sort(key=lambda d: _sort_key(d.get(order_by)), reverse=desc)
        return out[:limit] if (limit and py) else out

    def count(self, collection, **filters) -> int:
        where, args, py = self._sql_parts(filters)
        if py:
            return len(self.query(collection, **filters))
        with self._lock:
            return self.conn.execute("SELECT COUNT(*) FROM docs WHERE collection=?" + where, [collection] + args).fetchone()[0]

    # ---------- atomic lease (one pipeline worker at a time) ----------
    def acquire_lease(self, name: str, owner: str, ttl_s: float) -> bool:
        now = time.time()
        with self._lock:
            self.conn.execute("BEGIN IMMEDIATE")
            try:
                r = self.conn.execute("SELECT data FROM docs WHERE collection='locks' AND id=?", (name,)).fetchone()
                cur = json.loads(r[0]) if r else None
                if cur and cur.get("owner") != owner and cur.get("expires", 0) > now:
                    self.conn.execute("ROLLBACK")
                    return False
                self.conn.execute("INSERT OR REPLACE INTO docs (collection, id, data, updated) VALUES ('locks',?,?,?)",
                                  (name, json.dumps({"owner": owner, "expires": now + ttl_s}), now))
                self.conn.execute("COMMIT")
                return True
            except Exception:
                try:
                    self.conn.execute("ROLLBACK")
                except Exception:
                    pass
                raise
