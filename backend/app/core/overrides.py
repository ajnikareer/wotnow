"""
Admin-editable configuration stored in the database, layered over the files shipped in the image.

  pipeline            content schedule and publishing rules
  skill:<name>        per-skill agent parameters (temperature, review step, guardrail flags)
  instr:<file>        agent instruction text (e.g. instr:writer.md)
  rules               global guardrails (policy, blocked patterns, allowed numbers, PII patterns)
  card:<id>           fact-card edits (facts / do / dont / title / reviewed / disabled)
  evals:cases         golden test cases for the judge agent

Reads are cached for a few seconds; every write is versioned, audited in config_history, and invalidates the cache,
so a change in the admin UI reaches every agent within seconds, with no redeploy.
"""
from __future__ import annotations

import hashlib
import logging
import threading
import time
from typing import Any, Optional

from ..store.base import get_db

log = logging.getLogger("wotnow.overrides")
COLL = "config_overrides"
HIST = "config_history"
TTL_S = 10.0

_lock = threading.RLock()
_cache: dict[str, dict] = {}
_loaded_at = 0.0
_version = "0"


def invalidate() -> None:
    global _loaded_at
    with _lock:
        _loaded_at = 0.0


def _refresh() -> None:
    global _cache, _loaded_at, _version
    with _lock:
        if time.time() - _loaded_at < TTL_S:
            return
        try:
            docs = get_db().query(COLL)
            _cache = {d["key"]: d for d in docs if "key" in d}
            parts = sorted(f"{k}:{d.get('version', 0)}" for k, d in _cache.items())
            _version = hashlib.sha1("|".join(parts).encode()).hexdigest()[:12]
        except Exception as exc:  # database problem must never take the agents down
            log.warning("overrides unavailable, using file defaults: %s", exc)
        _loaded_at = time.time()


def get(key: str) -> Optional[Any]:
    """The override value for a key, or None."""
    _refresh()
    d = _cache.get(key)
    return d["value"] if d else None


def meta(key: str) -> Optional[dict]:
    _refresh()
    d = _cache.get(key)
    return {k: d[k] for k in ("version", "updatedAt", "updatedBy")} if d else None


def all_keys(prefix: str = "") -> list[str]:
    _refresh()
    return sorted(k for k in _cache if k.startswith(prefix))


def version() -> str:
    """Changes whenever any override changes (used to rebuild cached agents and compiled guardrails)."""
    _refresh()
    return _version


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())


def put(key: str, value: Any, actor: str = "system") -> dict:
    db = get_db()
    cur = db.get(COLL, key.replace("/", "~")) or {}
    doc = {"key": key, "value": value, "version": int(cur.get("version", 0)) + 1, "updatedAt": _now(), "updatedBy": actor}
    db.put(COLL, key.replace("/", "~"), doc)
    db.put(HIST, f"{key.replace('/', '~')}@{doc['version']:05d}", {**doc, "id": f"{key}@{doc['version']}"})
    invalidate()
    return doc


def delete(key: str, actor: str = "system") -> bool:
    db = get_db()
    k = key.replace("/", "~")
    cur = db.get(COLL, k)
    if not cur:
        return False
    v = int(cur.get("version", 0)) + 1
    db.put(HIST, f"{k}@{v:05d}", {"key": key, "value": None, "deleted": True, "version": v, "updatedAt": _now(), "updatedBy": actor, "id": f"{key}@{v}"})
    db.delete(COLL, k)
    invalidate()
    return True


def history(key: str, limit: int = 20) -> list[dict]:
    rows = [r for r in get_db().query(HIST, key=key)]
    rows.sort(key=lambda r: r.get("version", 0), reverse=True)
    return rows[:limit]
