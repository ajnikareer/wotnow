"""
"Since your last visit": what counts as NEW for a student.

A *visit* is a run of feed loads with no gap longer than SESSION_GAP_S (30 minutes). The student's NEW baseline is the moment
their PREVIOUS visit ended. Posts created after that baseline (and not yet answered) get the yellow NEW border; the baseline
only moves forward when a new visit starts, so the yellow cards stay yellow for the whole visit and the student can work through them.

  first ever visit        baseline = 24 hours ago
  next visit              baseline = the last time the feed was loaded during the previous visit
  never older than        72 hours (someone returning after a month isn't shown a month of posts as "new")

The baseline is stored on the student's own document (`visit`), so it survives restarts and follows the student across devices.
The document is written at most once a minute per student (Firestore bills per write).
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Optional

from ..store.base import get_db
from . import clock

SESSION_GAP_S = 30 * 60
FIRST_VISIT_S = 24 * 3600
MAX_NEW_AGE_S = 72 * 3600
TOUCH_EVERY_S = 60


def _parse(s) -> Optional[datetime]:
    if not s:
        return None
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def now_utc() -> datetime:
    return clock.now_local().astimezone(timezone.utc)


def touch(u: dict, now: Optional[datetime] = None) -> datetime:
    """Records that the student is looking at the feed now and returns their NEW baseline (a UTC datetime)."""
    now = now or now_utc()
    v = u.get("visit") or {}
    last, base = _parse(v.get("last")), _parse(v.get("baseline"))
    new_visit = False
    if last is None or base is None:
        base, new_visit = now - timedelta(seconds=FIRST_VISIT_S), True
    elif (now - last).total_seconds() > SESSION_GAP_S:
        base, new_visit = last, True
    if new_visit or last is None or (now - last).total_seconds() >= TOUCH_EVERY_S:
        visit = {"baseline": base.isoformat(), "last": now.isoformat()}
        u["visit"] = visit
        try:
            get_db().update("users", u["id"], {"visit": visit})     # touches only this field, so it can't overwrite other changes
        except Exception:
            pass                                                    # a failed bookkeeping write must never break the feed
    return max(base, now - timedelta(seconds=MAX_NEW_AGE_S))
