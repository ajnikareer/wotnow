"""Content pipeline: schedule maths, ticks, approve-first, pause, backoff, alerts, quizzes, lease, housekeeping."""
import asyncio
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.core import overrides
from app.engine import generator, local_alerts
from app.engine import quiz as quiz_mod
from app.pipeline import config as pcfg
from app.pipeline import scheduler
from app.services import clock
from app.store.base import get_db

IST = ZoneInfo("Asia/Kolkata")


@pytest.fixture()
def env(monkeypatch):
    state = {"now": datetime(2026, 10, 15, 22, 0, tzinfo=IST), "calls": [], "fail": set(), "alerts": [], "quizzes": []}
    monkeypatch.setattr(clock, "now_local", lambda: state["now"])

    async def fake_generate(agent_id, kind=None, band=None, publish=True, rng=None, local=None):
        state["calls"].append((agent_id, kind, publish))
        if agent_id in state["fail"]:
            return {"ok": False, "attempts": [{"error": "validation", "issues": ["bad rubric"]}]}
        pid = f"{agent_id}-{len(state['calls'])}"
        post = {"id": pid, "agentId": agent_id, "type": kind or "poll", "createdAt": state["now"].astimezone(ZoneInfo("UTC")).isoformat(), "bands": ["middle"],
                "title": f"Post {pid}", "body": "b", "status": "live", "source": "gemini", "sourceCards": [], "stats": {"responses": 0}}
        if publish:
            get_db().put(generator.POSTS, pid, post)
        return {"ok": True, "post": post, "attempts": [{"ok": True}]}

    async def fake_alert(city, publish=True):
        state["alerts"].append(city)
        return {"id": f"alert-{city}", "source": "rules"}

    async def fake_quiz(agent_id=None, rng=None):
        state["quizzes"].append(agent_id)
        return {"id": f"quiz-{len(state['quizzes'])}", "title": "Blitz"}

    monkeypatch.setattr(generator, "generate_one", fake_generate)
    monkeypatch.setattr(local_alerts, "build_alert", fake_alert)
    monkeypatch.setattr(quiz_mod, "build_quiz", fake_quiz)

    def at(h, m=0):
        state["now"] = datetime(2026, 10, 15, h, m, tzinfo=IST)
    state["at"] = at
    return state


def run(coro):
    return asyncio.run(coro)


def test_slots_are_spread_inside_the_active_window():
    cfg = pcfg.load()
    one = {a: scheduler.slots_for(a, cfg) for a in ("ember", "signal", "pulse", "basil", "civic", "terra", "cipher", "compass")}
    assert all(len(v) == 1 and 8 * 60 <= v[0] < 21 * 60 for v in one.values())
    assert len({v[0] for v in one.values()}) >= 6                          # experts are staggered, not simultaneous
    assert one["ember"] == scheduler.slots_for("ember", cfg)               # stable across calls
    cfg3 = {**cfg, "posts_per_expert_per_day": 3}
    s3 = scheduler.slots_for("ember", cfg3)
    assert len(s3) == 3 and s3 == sorted(s3) and s3[1] - s3[0] > 200
    assert scheduler.slots_for("ember", {**cfg, "posts_per_expert_per_day": 0}) == []


def test_nothing_due_before_the_window_then_one_post_per_tick(env):
    env["at"](6, 0)
    r = run(scheduler.tick())
    assert r["actions"] == [] and env["calls"] == []
    env["at"](22, 0)                                                        # every expert is now behind by one
    made = []
    for _ in range(8):
        r = run(scheduler.tick())
        assert len(r["actions"]) >= 1
        made += [a for a in r["actions"] if a["type"] == "post"]
    assert len(made) == 8 and len({a["agent"] for a in made}) == 8          # max_per_tick=1 → one expert per pass
    assert all(call[2] is False for call in env["calls"])                  # pipeline publishes itself (publish=False)
    before = len(env["calls"])
    assert [a for a in run(scheduler.tick())["actions"] if a["type"] == "post"] == [] and len(env["calls"]) == before
    posts = get_db().query(generator.POSTS)
    assert len(posts) == 8 and all(p["origin"] == "pipeline" and p["status"] == "live" and p.get("publishedAt") for p in posts)
    assert scheduler.posts_today("ember", "2026-10-15") == 1 and scheduler.posts_today("ember", "2026-10-14") == 0


def test_more_posts_per_day_and_disabled_experts_and_formats(env):
    pcfg.save({"posts_per_expert_per_day": 2, "max_per_tick": 5, "experts": {"compass": False, "cipher": False}, "formats": {"poll": False, "myth_fact": False, "scam_legit": False}}, "t")
    env["at"](22, 0)
    for _ in range(3):
        run(scheduler.tick())
    posts = get_db().query(generator.POSTS)
    assert len(posts) == 12 and not any(p["agentId"] in ("compass", "cipher") for p in posts)       # 6 experts × 2
    assert {c[1] for c in env["calls"]} == {"scenario"}                                             # only scenarios enabled


def test_approve_first_queue_and_cap(env):
    pcfg.save({"approve_first": True, "max_pending": 3, "max_per_tick": 5}, "t")
    env["at"](22, 0)
    r = run(scheduler.tick())
    posts = get_db().query(generator.POSTS)
    assert len(posts) == 3 and all(p["status"] == "pending" and "publishedAt" not in p for p in posts)
    assert any("review queue is full" in e["error"] for e in r["errors"])
    assert scheduler.status()["pending"] == 3
    pid = posts[0]["id"]
    get_db().update(generator.POSTS, pid, {"status": "live"})                                        # admin approves one
    r = run(scheduler.tick())
    assert len(get_db().query(generator.POSTS)) == 4                                                  # room for exactly one more


def test_pause_blocks_automatic_runs_but_not_admin_run_now(env):
    pcfg.save({"paused": True}, "t")
    env["at"](22, 0)
    assert run(scheduler.tick()) == {"skipped": "paused"} and env["calls"] == []
    r = run(scheduler.generate_now(["ember", "pulse"], "scenario"))
    assert [a["agent"] for a in r["actions"]] == ["ember", "pulse"] and r["source"] == "admin"
    assert {c[1] for c in env["calls"]} == {"scenario"}
    pcfg.save({"paused": False, "enabled": False}, "t")
    assert run(scheduler.tick()) == {"skipped": "disabled"}


def test_failure_backoff_and_recovery(env):
    env["fail"].add("cipher")
    pcfg.save({"experts": {a: (a == "cipher" or a == "ember") for a in pcfg.defaults()["experts"]}, "failure_backoff_min": 30}, "t")
    env["at"](22, 0)
    r1 = run(scheduler.tick())                       # cipher sorts before ember → fails first
    assert any("could not generate" in e["error"] and "bad rubric" in e["error"] for e in r1["errors"])       # reason is surfaced to the admin
    calls_after_first = len(env["calls"])
    r2 = run(scheduler.tick())                       # cipher is in backoff → ember is tried instead
    assert [a["agent"] for a in r2["actions"] if a["type"] == "post"] == ["ember"] and len(env["calls"]) == calls_after_first + 1
    env["fail"].clear()
    get_db().update(scheduler.STATE, "cipher", {"backoffUntil": 0})
    r3 = run(scheduler.tick())
    assert [a["agent"] for a in r3["actions"] if a["type"] == "post"] == ["cipher"]


def test_generator_exception_is_contained(env, monkeypatch):
    async def boom(*a, **k):
        raise RuntimeError("gemini exploded")
    monkeypatch.setattr(generator, "generate_one", boom)
    env["at"](22, 0)
    r = run(scheduler.tick())
    assert any("could not generate" in e["error"] for e in r["errors"])
    assert not [a for a in r["actions"] if a["type"] == "post"]


def test_alerts_once_per_city_per_day_and_quiz_slots(env):
    get_db().put("users", "u1", {"id": "u1", "city": "Hyderabad"})
    get_db().put("users", "u2", {"id": "u2", "city": "Hyderabad"})
    env["at"](6, 0)
    run(scheduler.tick())
    assert env["alerts"] == [] and env["quizzes"] == []                      # before 06:30 / 12:45
    env["at"](7, 0)
    run(scheduler.tick())
    assert sorted(env["alerts"]) == ["Hyderabad", "Pune"]
    run(scheduler.tick())
    assert len(env["alerts"]) == 2                                          # not repeated the same day
    env["at"](13, 0)
    run(scheduler.tick())
    assert len(env["quizzes"]) == 1
    run(scheduler.tick())
    assert len(env["quizzes"]) == 1
    env["at"](20, 0)
    run(scheduler.tick())
    assert len(env["quizzes"]) == 2
    pcfg.save({"alerts_enabled": False, "quizzes_enabled": False}, "t")
    env["state_day"] = None
    env["now"] = datetime(2026, 10, 16, 23, 0, tzinfo=IST)                    # next day
    run(scheduler.tick())
    assert len(env["alerts"]) == 2 and len(env["quizzes"]) == 2


def test_lease_prevents_two_workers(env):
    env["at"](22, 0)
    assert get_db().acquire_lease(scheduler.LEASE, "someone-else", 600)
    assert run(scheduler.tick()) == {"skipped": "another worker is running"} and env["calls"] == []


def test_runs_heartbeat_and_housekeeping(env):
    db = get_db()
    old = time.time() - 40 * 86400
    db.put("agent_traces", "old", {"id": "old", "ts": old, "skill": "judge"})
    db.put("agent_traces", "new", {"id": "new", "ts": time.time(), "skill": "judge"})
    for i in range(5):
        db.put(scheduler.RUNS, f"r{i}", {"id": f"r{i}", "ts": f"2026-01-0{i + 1}T00:00:00"})
    pcfg.save({"run_retention": 20}, "t")
    overrides.put("pipeline", {**(overrides.get("pipeline") or {}), "run_retention": 20, "trace_retention_days": 14}, "t")
    env["at"](22, 0)
    run(scheduler.tick())
    assert db.get("agent_traces", "old") is None and db.get("agent_traces", "new") is not None
    st = scheduler.status()
    assert st["lastTickAt"] and st["lastRun"]["actions"] and st["paused"] is False and st["enabled"] is False   # PIPELINE_ENABLED=false in tests


def test_pipeline_config_validation():
    for bad in ({"posts_per_expert_per_day": 99}, {"active_start": "9am"}, {"active_start": "20:00", "active_end": "08:00"},
                {"experts": {"nobody": True}}, {"formats": {"haiku": True}}, {"quiz_times": ["25:00"]}, {"mystery": 1}, {"max_per_tick": 0}):
        with pytest.raises(ValueError):
            pcfg.validate(bad)
    saved = pcfg.save({"posts_per_expert_per_day": 2, "experts": {"ember": False}, "quiz_times": ["19:00", "12:00", "12:00"]}, "me")
    assert saved["posts_per_expert_per_day"] == 2 and saved["experts"]["ember"] is False and saved["experts"]["pulse"] is True
    assert saved["quiz_times"] == ["12:00", "19:00"]
    pcfg.save({"experts": {"pulse": False}}, "me")
    assert pcfg.load()["experts"]["ember"] is False and pcfg.load()["experts"]["pulse"] is False      # nested settings merge
    assert pcfg.reset("me")["posts_per_expert_per_day"] == 1


def test_schedule_today_reports_progress(env):
    env["at"](22, 0)
    rows = {r["agent"]: r for r in scheduler.schedule_today()}
    assert rows["ember"]["due"] == 1 and rows["ember"]["done"] == 0 and rows["ember"]["behind"] == 1 and len(rows["ember"]["slots"][0]) == 5
    run(scheduler.generate_now(["ember"]))
    assert {r["agent"]: r for r in scheduler.schedule_today()}["ember"]["behind"] == 0
