"""
Feed selection: which posts a student sees, newest first.

Rules
  • Only LIVE posts (pending, unpublished and rejected posts never reach the feed).
  • Class band: a student sees posts for their own band and the band below (junior → junior; middle → junior+middle;
    senior → middle+senior). Older students are never shown content written for younger children's *next* band up.
  • Parent topic switches and the expert's minimum class still apply.
  • Local alerts: only TODAY's alert for the student's city (yesterday's alert is stale).
  • Order: today's city alert first, then newest first. "Pinned" posts are always kept in the feed even when they are older
    than the cut-off (they appear after the newer posts), so the demo scenarios never scroll away.

Cost: the newest posts (plus the pinned ones) are read once per FEED_CACHE_TTL_S seconds and shared by all students, so
Firestore reads stay flat however many students open the feed.
"""
from __future__ import annotations

import time
from typing import Optional

from ..conditions.live import slug as city_slug
from ..core.settings import get_platform
from ..engine import cards as C
from ..engine.generator import POSTS
from ..store.base import get_db
from . import clock

BAND_ORDER = ("junior", "middle", "senior")
WINDOW = 150                                   # newest live posts kept in the shared window
DEFAULT_PINS = ("oil-fire", "scam-power", "drink")   # a scenario, a scam-or-legit and a poll for the demo

_cache: dict = {"db": None, "at": 0.0, "posts": []}


def invalidate() -> None:
    """Call after any change that should show up immediately (publish, unpublish, pin)."""
    _cache["at"] = 0.0


def window() -> list[dict]:
    """Newest live posts + pinned live posts. Treat the returned dicts as read-only."""
    db = get_db()
    ttl = get_platform().feed_cache_ttl_s
    if ttl > 0 and _cache["db"] is db and time.time() - _cache["at"] < ttl:
        return _cache["posts"]
    recent = db.query_ex(POSTS, {"status": "live"}, order_by="createdAt", desc=True, limit=WINDOW)
    seen = {p["id"] for p in recent}
    pinned = [p for p in db.query(POSTS, pinned=True) if p.get("status") == "live" and p["id"] not in seen]
    posts = recent + pinned
    _cache.update(db=db, at=time.time(), posts=posts)
    return posts


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


def is_today_alert(p: dict, today_iso: str) -> bool:
    if p.get("type") != "local_alert":
        return False
    try:
        return clock.local_date_of(p["createdAt"]).isoformat() == today_iso
    except Exception:
        return False


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
    posts.sort(key=lambda p: (is_today_alert(p, today), p.get("createdAt", "")), reverse=True)
    return posts


def select(posts: list[dict], limit: int) -> list[dict]:
    """The newest `limit` posts, plus any pinned posts that fell off the end."""
    return posts[:limit] + [p for p in posts[limit:] if p.get("pinned")]


def latest(u: dict, tab: str = "foryou", since: Optional[str] = None) -> dict:
    """Cheap 'anything new?' check for the web app: newest post time and how many are newer than `since`."""
    posts = visible(u, tab)
    newest = max((p.get("createdAt", "") for p in posts), default=None)
    n = sum(1 for p in posts if since and p.get("createdAt", "") > since and not p.get("pinned"))
    return {"latest": newest, "newCount": n}


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
