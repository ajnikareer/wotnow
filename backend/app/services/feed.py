"""
Feed selection: which posts a student sees, newest first, and what colour each card is.

Rules
  • Only LIVE posts (pending, unpublished and rejected posts never reach the feed).
  • Class band: a student sees posts for their own band and the band below (junior → junior; middle → junior+middle;
    senior → middle+senior).
  • Parent topic switches and the expert's minimum class still apply.
  • Local alerts: only TODAY's alert for the student's city.
  • Tabs: today (posts made today, local time) · foryou · near · following; an expert filter overrides the tab.
  • Order: today's city alert first, then newest first. "Pinned" posts stay in the feed even when older than the cut-off.

Card state (the neon border), decided on the server from what the student has done, so it is the same on every device:
  done   green   answered a scenario with a score of PASS_SCORE or more · voted correctly · did the alert's check-in
  retry  red     scenario score below PASS_SCORE (dangerous answers are capped at 40) · voted wrongly
  new    yellow  posted since the student's last visit and not yet answered (see services/visits.py)
  none   plain   everything else

Cost: the newest posts (plus the pinned ones) are read once per FEED_CACHE_TTL_S seconds and shared by all students.
"""
from __future__ import annotations

import time
from datetime import datetime, timezone
from typing import Optional

from ..conditions.live import slug as city_slug
from ..core.settings import get_platform
from ..engine import cards as C
from ..engine.generator import POSTS
from ..store.base import get_db
from . import clock

BAND_ORDER = ("junior", "middle", "senior")
WINDOW = 150                                   # newest live posts kept in the shared window
DEFAULT_PINS = ()
TABS = ("today", "foryou", "near", "following")
VOTE_TYPES = ("poll", "myth_fact", "scam_legit")
PASS_SCORE = 50                                # scenario score at which a card turns green (below it: red)

_cache: dict = {"db": None, "at": 0.0, "posts": []}


def invalidate() -> None:
    """Call after any change that should show up immediately (publish, unpublish, pin)."""
    _cache["at"] = 0.0


def window() -> list[dict]:
    """Newest live posts. Treat the returned dicts as read-only."""
    db = get_db()
    ttl = get_platform().feed_cache_ttl_s
    if ttl > 0 and _cache["db"] is db and time.time() - _cache["at"] < ttl:
        return _cache["posts"]
    posts = db.query_ex(POSTS, {"status": "live"}, order_by="createdAt", desc=True, limit=WINDOW)
    _cache.update(db=db, at=time.time(), posts=posts)
    return posts


# ---------------- time helpers ----------------
def parse_iso(s) -> Optional[datetime]:
    if not s:
        return None
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def posted_today(p: dict, today_iso: str) -> bool:
    d = parse_iso(p.get("createdAt"))
    return bool(d and d.astimezone(clock.tz()).date().isoformat() == today_iso)


def is_today_alert(p: dict, today_iso: str) -> bool:
    return p.get("type") == "local_alert" and posted_today(p, today_iso)


# ---------------- who sees what ----------------
def band_ok(user_band: str, post_bands: list[str]) -> bool:
    i = BAND_ORDER.index(user_band) if user_band in BAND_ORDER else 1
    ok = {BAND_ORDER[i]} | ({BAND_ORDER[i - 1]} if i > 0 else set())
    return bool(ok & set(post_bands or []))


def allowed(u: dict, p: dict) -> bool:
    a = C.agent(p["agentId"])
    if not a:
        return False
    topics = u.get("parentSettings", {}).get("topics", {})
    return bool(band_ok(u["band"], p.get("bands", [])) and topics.get(a["domain"], True) and u["grade"] >= a["minGrade"])


def visible(u: dict, tab: str = "foryou", agent_id: Optional[str] = None, extra: Optional[list[dict]] = None) -> list[dict]:
    """Every live post this student may see, in feed order (no limit applied)."""
    posts = list(window())
    have = {p["id"] for p in posts}
    posts += [p for p in (extra or []) if p["id"] not in have]
    today = clock.today().isoformat()
    my_city = (u.get("city") or "").strip()
    slug = city_slug(my_city)

    def mine(p: dict) -> bool:
        if p["type"] != "local_alert":
            return True
        return is_today_alert(p, today) and (p.get("citySlug") == slug or (p.get("city") or "").lower() == my_city.lower())

    posts = [p for p in posts if mine(p) and allowed(u, p)]
    if agent_id:
        posts = [p for p in posts if p["agentId"] == agent_id]
    elif tab == "following":
        posts = [p for p in posts if p["agentId"] in u.get("follows", [])]
    elif tab == "near":
        posts = [p for p in posts if p["type"] == "local_alert" or p["agentId"] in ("terra", "civic")]
    elif tab == "today":
        posts = [p for p in posts if posted_today(p, today)]
    posts.sort(key=lambda p: p.get("createdAt", ""), reverse=True)
    return posts


def select(posts: list[dict], limit: int) -> list[dict]:
    """The newest `limit` posts."""
    return posts[:limit]


def latest(u: dict, tab: str = "foryou", since: Optional[str] = None) -> dict:
    """Cheap 'anything new?' check for the web app: newest post time, how many are newer than `since`, and today's post count."""
    posts = visible(u, tab)
    newest = max((p.get("createdAt", "") for p in posts), default=None)
    n = sum(1 for p in posts if since and p.get("createdAt", "") > since)
    today_count = len(posts) if tab == "today" else len(visible(u, "today"))
    return {"latest": newest, "newCount": n, "todayCount": today_count}


# ---------------- the neon border ----------------
def enrich_my(p: dict, my: Optional[dict]) -> Optional[dict]:
    """Adds `correct` to a stored vote (older votes were saved without it)."""
    if my and p.get("type") in VOTE_TYPES and my.get("choice") is not None and "correct" not in my:
        return {**my, "correct": my["choice"] == p.get("answerKey")}
    return my


def card_state(p: dict, my: Optional[dict], baseline: Optional[datetime] = None) -> str:
    """'done' | 'retry' | 'new' | 'none'. What the student has done always wins over 'new'."""
    my = my or {}
    t = p.get("type")
    if t == "scenario" and my.get("answered"):
        return "done" if int(my.get("score") or 0) >= PASS_SCORE else "retry"
    if t in VOTE_TYPES and my.get("choice") is not None:
        return "done" if my.get("correct") else "retry"
    if t == "local_alert" and my.get("checkedIn"):
        return "done"
    if baseline is not None:
        d = parse_iso(p.get("createdAt"))
        if d is not None and d > baseline:
            return "new"
    return "none"


def pin_defaults_once() -> int:
    """First start only: keep the demo posts in everyone's feed. Returns how many were pinned."""
    db = get_db()
    if db.get("pipeline_state", "pins_default"):
        return 0
    n, found = 0, 0
    for pid in DEFAULT_PINS:
        p = db.get(POSTS, pid)
        if not p:
            continue
        found += 1
        if not p.get("pinned"):
            p["pinned"] = True
            db.put(POSTS, pid, p)
            n += 1
    if found:                                   # only remember once the demo posts exist (seeding may come later)
        db.put("pipeline_state", "pins_default", {"id": "pins_default", "at": clock.utc_iso(), "pinned": n})
        invalidate()
    return n
