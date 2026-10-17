"""The shared demo student ('demo-student') must always be usable by judges."""
from __future__ import annotations

from ..core.security import DEMO_ID
from ..store.base import get_db

DEMO_DAILY_LIMIT = 180        # minutes per day: effectively unlimited. It is ONE profile used by every visitor,
                              # so a normal 30-minute child limit would lock everybody out after a few answers.


def ensure_demo_defaults() -> bool:
    """Run at startup. The seeded demo student starts with quiet hours 22:00-06:00 (which blocked answers late at night) and a
    30-minute daily limit (shared by every visitor). Clears the first and raises the second. Returns True if it changed anything.
    Does nothing if the demo student doesn't exist yet. Safe to run on every start (the profile is read-only for visitors)."""
    db = get_db()
    u = db.get("users", DEMO_ID)
    if not u:
        return False
    s = dict(u.get("parentSettings") or {})
    changed = False
    if s.get("quietHours"):
        s["quietHours"], changed = "", True
    if int(s.get("dailyLimit") or 0) < DEMO_DAILY_LIMIT:
        s["dailyLimit"], changed = DEMO_DAILY_LIMIT, True
    if changed:
        db.update("users", DEMO_ID, {"parentSettings": s})
    return changed
