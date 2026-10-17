"""Feed rules (live only, class bands, today's alert, pins, limits), the shared newest-posts window, /api/feed/latest, pinning."""
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.core.settings import get_platform
from app.engine.generator import POSTS
from app.services import clock, feed, posts, users
from app.store.base import get_db

IST = ZoneInfo("Asia/Kolkata")
UTC = ZoneInfo("UTC")
NOW = datetime(2026, 10, 15, 12, 0, tzinfo=IST)          # fixed "now": Thu 15 Oct 2026, noon IST


@pytest.fixture(autouse=True)
def fixed_clock(monkeypatch):
    monkeypatch.setattr(clock, "now_local", lambda: NOW)


def ts(h: int, d: int = 15, m: int = 0) -> str:
    """ISO time in UTC for 'day d, h:m'."""
    return datetime(2026, 10, d, h, m, tzinfo=UTC).isoformat()


def mk(pid, agent="ember", type="poll", bands=("middle",), at=None, status="live", **kw):
    p = {"id": pid, "agentId": agent, "type": type, "bands": list(bands), "createdAt": at or ts(5), "status": status,
         "title": f"T {pid}", "body": "b", "sourceCards": [], "stats": {"responses": 0}, "options": [], "answerKey": "a", "explanation": "x"}
    p.update(kw)
    get_db().put(POSTS, pid, p)
    return p


def student(uid="u1", grade=8, city="Pune", **patch):
    u = users.get_user(uid)
    return users.update_profile(u, {"grade": grade, "city": city, **patch})


def ids(rows):
    return [p["id"] for p in rows]


# ------------------------------------------------------------------ visibility rules
def test_only_live_posts_and_the_class_band_rule():
    mk("pj", bands=["junior"], at=ts(1)); mk("pm", bands=["middle"], at=ts(2)); mk("ps", bands=["senior"], at=ts(3))
    mk("pall", bands=["junior", "middle", "senior"], at=ts(4))
    mk("pend", status="pending", at=ts(5)); mk("unp", status="unpublished", at=ts(6)); mk("rej", status="rejected", at=ts(7))
    assert ids(feed.visible(student("mid", 8))) == ["pall", "pm", "pj"]                       # own band + the one below; newest first
    assert ids(feed.visible(student("sen", 10))) == ["pall", "ps", "pm"]
    assert ids(feed.visible(student("jun", 4))) == ["pall", "pj"]
    assert feed.band_ok("middle", ["senior"]) is False and feed.band_ok("senior", ["junior"]) is False and feed.band_ok("senior", []) is False


def test_topics_and_minimum_class():
    mk("fire", agent="ember", bands=["middle", "senior"]); mk("cars", agent="compass", bands=["senior"]); mk("road", agent="signal", bands=["middle"])
    u = student("t1", 10)
    u["parentSettings"]["topics"]["careers"] = True                                           # parents switch Careers on (it starts off)
    users.save(u)
    assert set(ids(feed.visible(u))) == {"fire", "cars", "road"}
    assert set(ids(feed.visible(student("t2", 8)))) == {"fire", "road"}                       # Careers needs Class 9+ (and a senior-band post)
    u["parentSettings"]["topics"]["fire"] = False
    users.save(u)
    assert "fire" not in ids(feed.visible(u))


def test_only_todays_alert_for_the_students_city_comes_first():
    ALL = ["junior", "middle", "senior"]
    mk("alert-pune-today", agent="terra", type="local_alert", bands=ALL, at=ts(3, 15), city="Pune", citySlug="pune")
    mk("alert-pune-yday", agent="terra", type="local_alert", bands=ALL, at=ts(3, 14), city="Pune", citySlug="pune")
    mk("alert-hyd-today", agent="terra", type="local_alert", bands=ALL, at=ts(3, 15), city="Hyderabad", citySlug="hyderabad")
    mk("alert-pune-late", agent="terra", type="local_alert", bands=ALL, at=ts(20, 14), city="Pune", citySlug="pune")     # 01:30 IST on the 15th
    mk("newer", at=ts(6)); mk("older", at=ts(1))
    got = ids(feed.visible(student("p1", 8, "Pune")))
    assert got == ["alert-pune-today", "alert-pune-late", "newer", "older"]                  # today's alerts first (newest first), then posts
    assert "alert-pune-yday" not in got and "alert-hyd-today" not in got                     # stale, or another city
    assert ids(feed.visible(student("h1", 8, "Hyderabad"))) == ["alert-hyd-today", "newer", "older"]
    assert ids(feed.visible(student("b1", 8, "Bangalore"))) == ["newer", "older"]            # no alert for a city that has none yet


def test_alert_created_just_after_local_midnight_counts_as_today():
    """The old rule compared UTC dates with the local date, so a 00:30 IST alert (19:00 UTC the day before) disappeared."""
    mk("alert", agent="terra", type="local_alert", bands=["middle"], at=ts(19, 14), city="Pune", citySlug="pune")
    assert ids(feed.visible(student("m1", 8, "Pune"))) == ["alert"]


def test_tabs_and_expert_filter():
    mk("a", agent="ember"); mk("b", agent="terra"); mk("c", agent="civic"); mk("d", agent="pulse")
    u = student("tab", 8)
    u["follows"] = ["ember"]
    users.save(u)
    assert set(ids(feed.visible(u, "foryou"))) == {"a", "b", "c", "d"}
    assert ids(feed.visible(u, "following")) == ["a"]
    assert set(ids(feed.visible(u, "near"))) == {"b", "c"}
    assert ids(feed.visible(u, "foryou", agent_id="pulse")) == ["d"]


def test_limit_keeps_the_newest_and_pinned_posts_survive_the_cut():
    for i in range(30):
        mk(f"p{i:02d}", at=ts(0, 1 + i % 14, i))                                              # different times
    mk("old-pinned", at=ts(0, 1, 0), pinned=True); mk("old-plain", at=ts(0, 1, 1))
    u = student("lim", 8)
    allv = feed.visible(u)
    top = feed.select(allv, 10)
    assert len(top) == 11 and ids(top)[:10] == ids(allv)[:10] and top[-1]["id"] == "old-pinned" and "old-plain" not in ids(top)
    inside = feed.select(allv, 100)
    assert ids(inside).count("old-pinned") == 1                                               # never duplicated when it fits


# ------------------------------------------------------------------ the shared window and its cache
def test_window_cache_ttl_and_invalidation(monkeypatch):
    monkeypatch.setenv("FEED_CACHE_TTL_S", "30"); get_platform.cache_clear()
    clockbox = {"t": 1000.0}
    monkeypatch.setattr(feed.time, "time", lambda: clockbox["t"])
    mk("one", at=ts(1))
    u = student("c1", 8)
    assert ids(feed.visible(u)) == ["one"]
    mk("two", at=ts(2))
    assert ids(feed.visible(u)) == ["one"]                       # still the cached window
    clockbox["t"] += 31
    assert ids(feed.visible(u)) == ["two", "one"]                # TTL expired
    mk("three", at=ts(3))
    feed.invalidate()
    assert ids(feed.visible(u)) == ["three", "two", "one"]       # explicit invalidation (publish / pin)


def test_cache_is_not_shared_across_databases(monkeypatch):
    monkeypatch.setenv("FEED_CACHE_TTL_S", "300"); get_platform.cache_clear()
    from app.store.base import reset_db
    mk("old", at=ts(1))
    assert ids(feed.window()) == ["old"]
    reset_db()
    mk("new", at=ts(2))
    assert ids(feed.window()) == ["new"]


def test_pinned_posts_outside_the_window_are_still_included():
    for i in range(feed.WINDOW + 20):
        mk(f"n{i:03d}", at=datetime(2026, 10, 15, 0, 0, tzinfo=UTC).isoformat()[:-6] + f".{i:06d}+00:00")
    mk("ancient", at=ts(0, 1), pinned=True); mk("ancient-hidden", at=ts(0, 1, 5), pinned=True, status="unpublished")
    got = ids(feed.window())
    assert "ancient" in got and "ancient-hidden" not in got and len(got) == feed.WINDOW + 1


# ------------------------------------------------------------------ the service the router calls
def test_feed_service_adds_todays_alert_and_survives_alert_failure(monkeypatch):
    u = student("svc", 8)
    mk("x", at=ts(4))
    alert = {"id": "alert-pune-today", "agentId": "terra", "type": "local_alert", "bands": ["junior", "middle", "senior"], "createdAt": ts(1), "status": "live",
             "city": "Pune", "citySlug": "pune", "title": "Hot", "body": "b", "chips": [], "steps": [], "sourceCards": [], "stats": {"responses": 0}, "checkins": 0}

    async def ok(city):
        return alert

    async def boom(city):
        raise RuntimeError("weather down")
    monkeypatch.setattr(posts, "build_alert", ok)
    rows = asyncio.run(posts.feed(u))
    assert [r["id"] for r in rows] == ["alert-pune-today", "x"] and rows[0]["my"] is None and "answerKey" not in rows[1] and "status" not in rows[1]
    monkeypatch.setattr(posts, "build_alert", boom)
    assert [r["id"] for r in asyncio.run(posts.feed(u))] == ["x"]                 # the feed still loads without the alert


def test_feed_service_limit_and_my_state(monkeypatch):
    async def none(city):
        return None
    monkeypatch.setattr(posts, "build_alert", none)
    for i in range(60):
        mk(f"f{i:02d}", at=ts(0, 1 + i // 5, i % 5))
    u = student("my", 8)
    users.set_my("my", "f59", {"choice": "a"})
    rows = asyncio.run(posts.feed(u))
    assert len(rows) == posts.FEED_LIMIT == 40 and rows[0]["id"] == "f59" and rows[0]["my"] == {"choice": "a", "correct": True}   # `correct` is added for older votes
    assert len(asyncio.run(posts.feed(u, limit=5))) == 5


# ------------------------------------------------------------------ /api/feed/latest and pinning
def test_latest_endpoint(v3_client):
    mk("a", at=ts(1)); mk("b", at=ts(2)); mk("c", at=ts(3)); mk("senior-only", bands=["senior"], at=ts(4)); mk("old", at=ts(0, 1), pinned=True)
    h = {"X-Demo-User": "viewer"}
    r = v3_client.get("/api/feed/latest", headers=h).json()
    assert r["latest"] == ts(3) and r["newCount"] == 0                               # a Class 8 student never sees the senior-only post
    assert v3_client.get("/api/feed/latest", params={"since": ts(1)}, headers=h).json()["newCount"] == 2       # properly encoded
    assert v3_client.get(f"/api/feed/latest?since={ts(1)}", headers=h).json()["newCount"] == 2                  # raw '+' (decoded as a space) still works
    assert v3_client.get("/api/feed/latest", params={"since": ts(3)}, headers=h).json()["newCount"] == 0
    near = v3_client.get("/api/feed/latest?tab=near", headers=h).json()
    assert near["latest"] is None and near["newCount"] == 0
    assert v3_client.get("/api/feed/latest?tab=nonsense", headers=h).status_code == 400
    mk("d", at=ts(6)); feed.invalidate()
    r = v3_client.get("/api/feed/latest", params={"since": ts(3)}, headers=h).json()
    assert r["latest"] == ts(6) and r["newCount"] == 1


def test_pin_endpoint_needs_admin_and_takes_effect_at_once(v3_client):
    mk("keep", at=ts(1))
    assert v3_client.post("/api/admin/posts/keep/pin", json={"pinned": True}).status_code == 403
    H = {"X-Admin-Token": "t"}
    assert v3_client.post("/api/admin/posts/keep/pin", json={"pinned": True}, headers=H).json() == {"id": "keep", "pinned": True}
    assert get_db().get(POSTS, "keep")["pinned"] is True
    assert v3_client.post("/api/admin/posts/keep/pin", json={"pinned": False}, headers=H).json()["pinned"] is False
    assert v3_client.post("/api/admin/posts/nope/pin", json={}, headers=H).status_code == 404
    acts = [a["action"] for a in get_db().query_ex("audit", order_by="ts", desc=True, limit=5)]
    assert acts[:2] == ["post.unpin", "post.pin"]


def test_pin_defaults_once():
    assert feed.pin_defaults_once() == 0 and get_db().get("pipeline_state", "pins_default") is None     # nothing seeded yet: try again next start
    mk("oil-fire", at=ts(1)); mk("drink", at=ts(2)); mk("other", at=ts(3))
    assert feed.pin_defaults_once() == 2
    assert get_db().get(POSTS, "oil-fire")["pinned"] and get_db().get(POSTS, "drink")["pinned"] and not get_db().get(POSTS, "other").get("pinned")
    assert get_db().get("pipeline_state", "pins_default")["pinned"] == 2
    get_db().update(POSTS, "oil-fire", {"pinned": False})
    assert feed.pin_defaults_once() == 0 and get_db().get(POSTS, "oil-fire")["pinned"] is False          # an admin's un-pin is respected
