"""
Document-store PORT. Collections may be paths, e.g. 'users/u1/activity'.

Backends (env DB_BACKEND):
  memory     in-process dict (tests, throwaway demos)
  sqlite     single file on a volume (DB_PATH, default /data/wotnow.db): persistent, no cloud permissions needed
  firestore  Cloud Firestore (Cloud Run)
"""
from __future__ import annotations

import os
import time
from abc import ABC, abstractmethod
from typing import Any, Optional

_INSTANCE = None


def _sort_key(v: Any):
    return (v is None, v if isinstance(v, (int, float, str)) else str(v))


class Database(ABC):
    name = "base"

    @abstractmethod
    def get(self, collection: str, doc_id: str) -> Optional[dict]: ...
    @abstractmethod
    def put(self, collection: str, doc_id: str, data: dict) -> dict: ...
    @abstractmethod
    def query(self, collection: str, **filters: Any) -> list[dict]: ...
    @abstractmethod
    def delete(self, collection: str, doc_id: str) -> None: ...

    def update(self, collection: str, doc_id: str, patch: dict) -> dict:
        cur = self.get(collection, doc_id) or {}
        cur.update(patch)
        return self.put(collection, doc_id, cur)

    def query_ex(self, collection: str, filters: Optional[dict] = None, order_by: Optional[str] = None,
                 desc: bool = False, limit: Optional[int] = None) -> list[dict]:
        """Filtered, ordered, limited query. Default implementation sorts in Python; sqlite overrides it."""
        rows = self.query(collection, **(filters or {}))
        if order_by:
            rows.sort(key=lambda d: _sort_key(d.get(order_by)), reverse=desc)
        return rows[:limit] if limit else rows

    def count(self, collection: str, **filters: Any) -> int:
        return len(self.query(collection, **filters))

    def acquire_lease(self, name: str, owner: str, ttl_s: float) -> bool:
        """Best-effort lease lock (atomic on sqlite). Used so only one worker runs the content pipeline."""
        now = time.time()
        cur = self.get("locks", name)
        if cur and cur.get("owner") != owner and cur.get("expires", 0) > now:
            return False
        self.put("locks", name, {"owner": owner, "expires": now + ttl_s})
        return True

    def release_lease(self, name: str, owner: str) -> None:
        cur = self.get("locks", name)
        if cur and cur.get("owner") == owner:
            self.delete("locks", name)


def get_db() -> Database:
    global _INSTANCE
    if _INSTANCE is None:
        from ..config import get_settings
        backend = get_settings().DB_BACKEND
        if backend == "firestore":
            from .firestore_db import FirestoreDatabase
            _INSTANCE = FirestoreDatabase()
        elif backend == "sqlite":
            from .sqlite_db import SqliteDatabase
            _INSTANCE = SqliteDatabase(os.getenv("DB_PATH", "/data/wotnow.db"))
        else:
            from .memory_db import MemoryDatabase
            _INSTANCE = MemoryDatabase()
    return _INSTANCE


def reset_db() -> None:
    """Tests only."""
    global _INSTANCE
    if _INSTANCE is not None and hasattr(_INSTANCE, "close"):
        try:
            _INSTANCE.close()
        except Exception:
            pass
    _INSTANCE = None
    from .memory_db import _STORE
    _STORE.clear()
