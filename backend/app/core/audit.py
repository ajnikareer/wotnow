"""Audit trail of every admin change (who, what, when)."""
from __future__ import annotations

import time
import uuid

from ..store.base import get_db

COLL = "audit"


def log(actor: str, action: str, target: str = "", detail=None) -> None:
    ts = time.time()
    rid = f"{int(ts * 1000)}-{uuid.uuid4().hex[:4]}"
    try:
        get_db().put(COLL, rid, {"id": rid, "ts": ts, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts)),
                                 "actor": actor, "action": action, "target": target, "detail": detail})
    except Exception:
        pass


def recent(limit: int = 100) -> list[dict]:
    return get_db().query_ex(COLL, order_by="ts", desc=True, limit=limit)
