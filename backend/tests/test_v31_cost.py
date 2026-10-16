"""
Read-cost regressions. Firestore bills per document read, and the app now runs 24/7, so the always-on parts must not scale
with the amount of data: an idle scheduler tick, the feed window, /api/info and the admin-settings refresh.
"""
import asyncio
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.core import overrides
from app.core.settings import get_platform
from app.engine import generator, local_alerts
from app.engine import quiz as quiz_mod
from app.pipeline import config as pcfg
from app.pipeline import scheduler
from app.services import clock, feed
from app.store import base
from app.store.memory_db import MemoryDatabase

IST = ZoneInfo("Asia/Kolkata")


class CountingDB(MemoryDatabase):
    """Counts billed reads the way Firestore would: unbounded scans bill every document, ordered+limited queries bill the page."""
    def __init__(self):
        self.reads = 0

    def get(self, collection, doc_id):
        self.reads += 1
        return super().get(collection, doc_id)

    def query(self, collection, **filters):
        rows = super().query(collection, **filters)
        self.reads += len(rows)
        return rows

    def query_ex(self, collection, filters=None, order_by=None, desc=False, limit=None):
        rows = MemoryDatabase.query(self, collection, **(filters or {}))
        if order_by:
            rows.sort(key=lambda d: (d.get(order_by) is None, d.get(order_by)), reverse=desc)
        rows = rows[:limit] if limit else rows
        self.reads += len(rows)
        return rows

    def count(self, collection, **filters):
        self.reads += 1
        return len(MemoryDatabase.query(self, collection, **filters))


@pytest.fixture()
def db():
    d = CountingDB()
    base._INSTANCE = d
    return d


def big(db):
    """A database that has been running for weeks."""
    for i in range(400):
        db.put("posts", f"old-{i}", {"id": f"old-{i}", "agentId": "ember", "type": "poll", "status": "live", "origin": "pipeline", "bands": ["middle"],
                                     "createdAt": f"2026-09-{1 + i % 28:02d}T10:00:00+00:00", "title": "t"})
    for i in range(300):
        db.put("agent_traces", f"t{i}", {"id": f"t{i}", "ts": time.time() - i * 60, "skill": "judge"})
    for i in range(80):
        db.put("users", f"u{i}", {"id": f"u{i}", "city": "Pune"})
    for i in range(60):
        db.put("pipeline_runs", f"r{i}", {"id": f"r{i}", "ts": f"2026-10-{1 + i % 14:02d}T00:00:00"})


def test_idle_scheduler_tick_reads_a_handful_of_documents(db, monkeypatch):
    state = {"now": datetime(2026, 10, 15, 22, 0, tzinfo=IST), "n": 0}
    monkeypatch.setattr(clock, "now_local", lambda: state["now"])

    async def gen(agent_id, kind=None, band=None, publish=True, rng=None, local=None):
        state["n"] += 1
        pid = f"new-{state['n']}"
        return {"ok": True, "attempts": [], "post": {"id": pid, "agentId": agent_id, "type": "poll", "createdAt": state["now"].astimezone(ZoneInfo("UTC")).isoformat(),
                                                      "bands": ["middle"], "title": "t", "status": "live", "sourceCards": [], "stats": {}}}

    async def alert(city, publish=True):
        return {"id": f"alert-{city}"}

    async def quiz(agent_id=None, rng=None):
        return {"id": "q", "title": "Blitz"}
    monkeypatch.setattr(generator, "generate_one", gen)
    monkeypatch.setattr(local_alerts, "build_alert", alert)
    monkeypatch.setattr(quiz_mod, "build_quiz", quiz)
    big(db)
    for _ in range(10):                                             # let every expert post and today's alerts/quizzes finish
        asyncio.run(scheduler.tick())
    posted = len([p for p in MemoryDatabase.query(db, "posts") if p["id"].startswith("new-")])
    assert posted == 8
    db.reads = 0
    r = asyncio.run(scheduler.tick())                               # nothing is due now
    assert r["actions"] == [] and r["errors"] == []
    assert db.reads < 40, f"an idle tick read {db.reads} documents"
    db.reads = 0
    for _ in range(5):
        asyncio.run(scheduler.tick())
    assert db.reads < 200


def test_counters_are_rebuilt_once_after_an_upgrade_and_never_by_other_days(db, monkeypatch):
    monkeypatch.setattr(clock, "now_local", lambda: datetime(2026, 10, 15, 22, 0, tzinfo=IST))
    db.put("posts", "a", {"id": "a", "agentId": "ember", "origin": "pipeline", "createdAt": "2026-10-15T04:00:00+00:00"})
    db.put("posts", "b", {"id": "b", "agentId": "ember", "origin": "pipeline", "createdAt": "2026-10-14T04:00:00+00:00"})
    db.put("posts", "c", {"id": "c", "agentId": "ember", "origin": "seed", "createdAt": "2026-10-15T04:00:00+00:00"})      # not made by the pipeline
    assert scheduler.posts_today("ember", "2026-10-14") == 1 and db.get("pipeline_counts", "ember") is None     # other days never write
    assert scheduler.posts_today("ember", "2026-10-15") == 1
    assert db.get("pipeline_counts", "ember") == {"id": "ember", "day": "2026-10-15", "count": 1}
    db.reads = 0
    assert scheduler.posts_today("ember", "2026-10-15") == 1 and db.reads == 1                                 # now a single small read
    monkeypatch.setattr(clock, "now_local", lambda: datetime(2026, 10, 16, 9, 0, tzinfo=IST))
    assert scheduler.posts_today("ember", "2026-10-16") == 0 and db.get("pipeline_counts", "ember")["day"] == "2026-10-16"   # new day, new counter


def test_publishing_bumps_the_counter_and_clears_the_feed_cache(db, monkeypatch):
    monkeypatch.setattr(clock, "now_local", lambda: datetime(2026, 10, 15, 22, 0, tzinfo=IST))
    monkeypatch.setenv("FEED_CACHE_TTL_S", "300"); get_platform.cache_clear()
    assert feed.window() == []
    post = {"id": "n1", "agentId": "ember", "type": "poll", "createdAt": "2026-10-15T10:00:00+00:00", "bands": ["middle"], "title": "t", "stats": {}}
    asyncio.run(scheduler._publish(dict(post), pcfg.load()))
    assert scheduler.posts_today("ember", "2026-10-15") == 1
    assert [p["id"] for p in feed.window()] == ["n1"]                                # cache was invalidated by the publish
    asyncio.run(scheduler._publish(dict(post, id="n2", createdAt="2026-10-15T11:00:00+00:00"), pcfg.load()))
    assert scheduler.posts_today("ember", "2026-10-15") == 2 and db.get("pipeline_counts", "ember")["count"] == 2


def test_the_feed_window_is_bounded_and_shared(db, monkeypatch):
    monkeypatch.setenv("FEED_CACHE_TTL_S", "30"); get_platform.cache_clear()
    big(db)
    db.put("posts", "pin", {"id": "pin", "agentId": "ember", "type": "poll", "status": "live", "bands": ["middle"], "createdAt": "2026-01-01T00:00:00+00:00", "pinned": True})
    db.reads = 0
    first = feed.window()
    assert len(first) == feed.WINDOW + 1 and db.reads == feed.WINDOW + 1          # 150 newest + the pinned one, not all 401
    assert feed.window() is first and db.reads == feed.WINDOW + 1                 # every other student in the next 30 s costs nothing


def test_alert_city_scan_is_hourly_not_every_tick(db, monkeypatch):
    state = {"now": datetime(2026, 10, 15, 7, 0, tzinfo=IST), "alerts": []}
    monkeypatch.setattr(clock, "now_local", lambda: state["now"])

    async def alert(city, publish=True):
        state["alerts"].append(city)
        return {"id": f"alert-{city}"}
    monkeypatch.setattr(local_alerts, "build_alert", alert)
    db.put("users", "u1", {"id": "u1", "city": "Hyderabad"})
    cfg = pcfg.load()
    run = {"actions": [], "errors": []}
    asyncio.run(scheduler._alerts(cfg, run, "2026-10-15", 7 * 60))
    assert sorted(state["alerts"]) == ["Hyderabad", "Pune"]
    db.put("users", "u2", {"id": "u2", "city": "Chennai"})                          # a new city appears during the day
    db.reads = 0
    asyncio.run(scheduler._alerts(cfg, run, "2026-10-15", 7 * 60 + 5))
    assert db.reads == 1 and len(state["alerts"]) == 2                              # skipped: only the small state document was read
    st = db.get("pipeline_state", "alerts")
    db.put("pipeline_state", "alerts", {**st, "checkedAt": time.time() - 3700})     # an hour later …
    asyncio.run(scheduler._alerts(cfg, run, "2026-10-15", 8 * 60 + 10))
    assert sorted(state["alerts"]) == ["Chennai", "Hyderabad", "Pune"]              # … the new city gets its alert


def test_failed_alert_is_retried_sooner(db, monkeypatch):
    calls = []

    async def flaky(city, publish=True):
        calls.append(city)
        if len(calls) == 1:
            raise RuntimeError("weather API down")
        return {"id": "a"}
    monkeypatch.setattr(local_alerts, "build_alert", flaky)
    monkeypatch.setattr(clock, "now_local", lambda: datetime(2026, 10, 15, 7, 0, tzinfo=IST))
    run = {"actions": [], "errors": []}
    asyncio.run(scheduler._alerts(pcfg.load(), run, "2026-10-15", 7 * 60))
    assert run["errors"] and db.get("pipeline_state", "alerts")["complete"] is False
    st = db.get("pipeline_state", "alerts")
    db.put("pipeline_state", "alerts", {**st, "checkedAt": time.time() - 700})       # 10+ minutes later (retry window)
    asyncio.run(scheduler._alerts(pcfg.load(), run, "2026-10-15", 7 * 60 + 12))
    assert calls == ["Pune", "Pune"] and db.get("pipeline_state", "alerts")["complete"] is True


def test_housekeeping_reads_only_the_oldest_documents(db):
    big(db)
    db.put("pipeline_state", "housekeeping", {"id": "housekeeping", "ts": 0})
    old = time.time() - 40 * 86400
    for i in range(5):
        db.put("agent_traces", f"ancient{i}", {"id": f"ancient{i}", "ts": old - i, "skill": "judge"})
    for i in range(400):
        db.put("pipeline_runs", f"extra{i}", {"id": f"extra{i}", "ts": f"2026-08-{1 + i % 28:02d}T00:00:{i % 60:02d}"})
    db.reads = 0
    scheduler._housekeeping(pcfg.load())
    assert db.reads <= 200 + 500 + 5                                                # 200 oldest traces + one page of runs, never everything
    assert all(db.get("agent_traces", f"ancient{i}") is None for i in range(5))
    assert len(MemoryDatabase.query(db, "pipeline_runs")) == 300                    # 460 runs trimmed down to run_retention


def test_overrides_refresh_is_throttled_by_the_ttl(db, monkeypatch):
    monkeypatch.setenv("OVERRIDES_TTL_S", "60"); get_platform.cache_clear()
    overrides.put("pipeline", {"paused": False}, "t")
    overrides.put("rules", {"max_input_chars": 5000}, "t")
    overrides.invalidate()
    db.reads = 0
    for _ in range(50):
        overrides.get("pipeline"); overrides.version(); overrides.get("rules")
    assert db.reads == 2                                                            # one refresh (2 override documents) for 150 lookups
    overrides.put("pipeline", {"paused": True}, "admin")                            # a write in this process is visible at once
    assert overrides.get("pipeline") == {"paused": True}


def test_api_info_never_scans_data(db, v3_client):
    big(db)
    db.reads = 0
    for _ in range(5):
        assert v3_client.get("/api/info").json()["pipeline"] == {"enabled": False, "paused": False}
    assert db.reads <= 10
