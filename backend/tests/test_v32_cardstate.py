"""
Neon card states (new / done / retry), the 'since your last visit' baseline, and the Today tab.
The colour is decided on the server from what the student has done, so it is persistent and identical on every device.
"""
import asyncio
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest

from app.engine.generator import POSTS
from app.services import clock, feed, posts, users, visits
from app.store.base import get_db

IST = ZoneInfo("Asia/Kolkata")
UTC = timezone.utc
T0 = datetime(2026, 10, 15, 12, 0, tzinfo=IST)           # Thu 15 Oct 2026, 12:00 IST = 06:30 UTC


@pytest.fixture()
def clk(monkeypatch):
    box = {"now": T0}
    monkeypatch.setattr(clock, "now_local", lambda: box["now"])

    async def no_alert(city):
        return None
    monkeypatch.setattr(posts, "build_alert", no_alert)

    def advance(**kw):
        box["now"] = box["now"] + timedelta(**kw)
    box["advance"] = advance
    return box


def ago(**kw) -> str:
    """ISO time (UTC) `kw` before T0."""
    return (T0 - timedelta(**kw)).astimezone(UTC).isoformat()


def mk(pid, type="poll", at=None, status="live", agent="ember", bands=("middle",), **kw):
    p = {"id": pid, "agentId": agent, "type": type, "bands": list(bands), "createdAt": at or ago(hours=1), "status": status, "title": f"T {pid}",
         "body": "b", "question": "q?", "sourceCards": [], "stats": {"responses": 0}, "options": [{"id": "a", "text": "x"}, {"id": "b", "text": "y"}],
         "answerKey": "a", "explanation": "because", "voteCounts": {}, "rubric": [{"id": "r1", "point": "p", "note": "n", "weight": 100, "critical": True, "card": "X"}], "dangerousActions": []}
    p.update(kw)
    get_db().put(POSTS, pid, p)
    return p


def student(uid="kid", grade=8):
    return users.update_profile(users.get_user(uid), {"grade": grade, "city": "Pune"})


def states(rows):
    return {r["id"]: r["state"] for r in rows}


BASE = T0.astimezone(UTC) - timedelta(hours=24)


# ------------------------------------------------------------------ the state rules
@pytest.mark.parametrize("score,state", [(0, "retry"), (40, "retry"), (49, "retry"), (50, "done"), (62, "done"), (92, "done"), (100, "done")])
def test_scenario_state_by_score(score, state):
    p = mk("s", "scenario")
    assert feed.card_state(p, {"answered": True, "score": score}) == state


def test_vote_and_checkin_states():
    poll, myth, scam, alert = mk("p"), mk("m", "myth_fact", answerKey="myth"), mk("c", "scam_legit", answerKey="scam"), mk("al", "local_alert")
    assert feed.card_state(poll, {"choice": "a", "correct": True}) == "done"
    assert feed.card_state(poll, {"choice": "b", "correct": False}) == "retry"
    assert feed.card_state(myth, {"choice": "fact", "correct": False}) == "retry"
    assert feed.card_state(scam, {"choice": "scam", "correct": True}) == "done"
    assert feed.card_state(alert, {"checkedIn": True}) == "done"
    assert feed.card_state(poll, None) == "none" and feed.card_state(alert, {}) == "none"


def test_what_the_student_did_always_beats_new():
    p = mk("p", at=ago(minutes=5))
    assert feed.card_state(p, None, BASE) == "new"
    assert feed.card_state(p, {"choice": "a", "correct": True}, BASE) == "done"
    assert feed.card_state(p, {"choice": "b", "correct": False}, BASE) == "retry"
    s = mk("s", "scenario", at=ago(minutes=5))
    assert feed.card_state(s, {"answered": True, "score": 20}, BASE) == "retry"


def test_new_needs_a_baseline_and_a_post_made_after_it():
    assert feed.card_state(mk("a", at=ago(hours=2)), None, BASE) == "new"
    assert feed.card_state(mk("b", at=ago(hours=30)), None, BASE) == "none"       # before the baseline
    assert feed.card_state(mk("c", at=ago(hours=2)), None, None) == "none"        # no baseline (post detail page): never 'new'
    assert feed.card_state(mk("d", at="not a date"), None, BASE) == "none"
    assert feed.card_state(mk("e", at=(T0 - timedelta(hours=1)).replace(tzinfo=None).isoformat()), None, BASE) in ("new", "none")   # naive time = UTC, no crash


def test_older_votes_get_their_correctness_filled_in():
    p = mk("p", answerKey="a")
    assert feed.enrich_my(p, {"choice": "a"}) == {"choice": "a", "correct": True}
    assert feed.enrich_my(p, {"choice": "b"}) == {"choice": "b", "correct": False}
    assert feed.enrich_my(p, {"choice": "a", "correct": False}) == {"choice": "a", "correct": False}      # an explicit value is kept
    assert feed.enrich_my(p, None) is None and feed.enrich_my(mk("s", "scenario"), {"answered": True, "score": 5}) == {"answered": True, "score": 5}
    assert posts.public(p, {"choice": "b"})["state"] == "retry"                                           # detail page / old data still coloured


# ------------------------------------------------------------------ since your last visit
def test_first_visit_baseline_is_24_hours_back(clk):
    u = student()
    assert visits.touch(u) == BASE
    assert get_db().get("users", "kid")["visit"] == {"baseline": BASE.isoformat(), "last": T0.astimezone(UTC).isoformat()}


def test_baseline_holds_during_a_visit_and_moves_after_a_gap(clk):
    u = student()
    first = visits.touch(u)
    clk["advance"](minutes=20)
    assert visits.touch(users.get_user("kid")) == first                      # within 30 minutes: same visit, same baseline
    last_seen = clk["now"].astimezone(UTC)
    clk["advance"](minutes=45)                                               # 45 minutes of silence: a new visit
    assert visits.touch(users.get_user("kid")) == last_seen                  # NEW = everything since the previous visit ended
    clk["advance"](minutes=10)
    assert visits.touch(users.get_user("kid")) == last_seen                  # …and it holds for this visit too


def test_baseline_never_older_than_72_hours(clk):
    u = student()
    visits.touch(u)
    clk["advance"](days=30)
    b = visits.touch(users.get_user("kid"))
    assert b == clk["now"].astimezone(UTC) - timedelta(hours=72)             # a month away is not "a month of new posts"
    stored = get_db().get("users", "kid")["visit"]
    assert stored["baseline"] == T0.astimezone(UTC).isoformat()              # (the stored value is the true last visit)


def test_visit_bookkeeping_writes_at_most_once_a_minute(clk, monkeypatch):
    u = student()
    db = get_db()
    calls = []
    orig = db.update
    monkeypatch.setattr(db, "update", lambda c, i, patch: (calls.append((c, i, sorted(patch))), orig(c, i, patch))[1])
    visits.touch(u)
    assert len(calls) == 1 and calls[0] == ("users", "kid", ["visit"])       # only the `visit` field is written
    for _ in range(5):
        clk["advance"](seconds=5)
        visits.touch(u)
    assert len(calls) == 1                                                   # 25 seconds later: no new write
    clk["advance"](seconds=40)
    visits.touch(u)
    assert len(calls) == 2


def test_visit_write_does_not_clobber_other_fields_and_failures_are_swallowed(clk, monkeypatch):
    u = student()
    db = get_db()
    db.update("users", "kid", {"xp": 777})                                   # something else changed the profile meanwhile
    visits.touch(u)
    assert db.get("users", "kid")["xp"] == 777 and "visit" in db.get("users", "kid")
    monkeypatch.setattr(db, "update", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("db down")))
    clk["advance"](hours=2)
    assert isinstance(visits.touch(u), datetime)                             # the feed must still load


# ------------------------------------------------------------------ through the feed service
def test_feed_marks_new_posts_then_the_colour_follows_what_the_student_does(clk):
    mk("fresh1", at=ago(minutes=30)); mk("fresh2", at=ago(hours=3)); mk("old", at=ago(hours=40))
    mk("fresh-scn", "scenario", at=ago(hours=2)); mk("fresh-vote", at=ago(hours=1))
    u = student()
    assert states(asyncio.run(posts.feed(u))) == {"fresh1": "new", "fresh2": "new", "old": "none", "fresh-scn": "new", "fresh-vote": "new"}

    # the student votes (right) and answers a scenario (badly) → colours change and PERSIST
    users.set_my("kid", "fresh-vote", {"choice": "a", "correct": True})
    users.set_my("kid", "fresh-scn", {"answered": True, "score": 30})
    clk["advance"](minutes=5)
    now = states(asyncio.run(posts.feed(users.get_user("kid"))))
    assert now["fresh-vote"] == "done" and now["fresh-scn"] == "retry" and now["fresh1"] == "new" and now["old"] == "none"

    # a better retry turns the red card green; a later worse one can't turn it back (best score is kept)
    users.set_my("kid", "fresh-scn", {"answered": True, "score": 85})
    assert states(asyncio.run(posts.feed(users.get_user("kid"))))["fresh-scn"] == "done"

    # another visit tomorrow: unanswered "new" posts become plain, answered ones keep their colour
    clk["advance"](days=1)
    mk("brand-new", at=ago(minutes=-1430))                                    # made 23.8 h after T0, i.e. just now
    later = states(asyncio.run(posts.feed(users.get_user("kid"))))
    assert later["fresh1"] == "none" and later["fresh2"] == "none" and later["brand-new"] == "new"
    assert later["fresh-vote"] == "done" and later["fresh-scn"] == "done"


def test_state_is_the_same_on_another_device_and_after_a_restart(clk):
    mk("p", at=ago(minutes=10))
    asyncio.run(posts.feed(student()))
    users.set_my("kid", "p", {"choice": "b", "correct": False})
    from app.store import base
    keep = dict(base._STORE)                                                  # "restart": everything in memory is rebuilt from the stored documents
    feed.invalidate()
    assert states(asyncio.run(posts.feed(users.get_user("kid"))))["p"] == "retry"
    assert base._STORE == keep


def test_vote_stores_correctness_for_the_colour(clk):
    mk("poll", answerKey="a")
    u = student()
    posts.vote(u, "poll", "b")
    assert users.get_my("kid", "poll") == {"choice": "b", "correct": False}
    assert states(asyncio.run(posts.feed(users.get_user("kid"))))["poll"] == "retry"
    mk("poll2", answerKey="a")
    posts.vote(users.get_user("kid"), "poll2", "a")
    assert users.get_my("kid", "poll2") == {"choice": "a", "correct": True}
    assert states(asyncio.run(posts.feed(users.get_user("kid"))))["poll2"] == "done"


def test_answer_flow_colours_and_best_score_is_kept(clk, monkeypatch):
    mk("scn", "scenario")
    box = {"score": 30}

    async def fake_judge(post, text, band):
        return {"score": box["score"], "label": "x", "checklist": [{"id": "r1", "point": "p", "hit": False, "note": ""}], "dangerous": box["score"] <= 40,
                "dangerousReason": None, "feedback": "f", "hits": [], "judgedBy": "rules"}

    async def fake_mod(text):
        return {"label": "ok"}
    monkeypatch.setattr(posts, "judge", fake_judge)
    monkeypatch.setattr(posts, "moderate", fake_mod)
    u = student()

    def now():
        return states(asyncio.run(posts.feed(users.get_user("kid"))))["scn"]
    asyncio.run(posts.answer(u, "scn", "I would panic"))
    assert now() == "retry"                                                   # 30: red
    box["score"] = 80
    asyncio.run(posts.answer(users.get_user("kid"), "scn", "No water, use a lid"))
    assert now() == "done"                                                    # 80: green
    box["score"] = 10
    asyncio.run(posts.answer(users.get_user("kid"), "scn", "ignore it"))
    assert users.get_my("kid", "scn")["score"] == 80 and now() == "done"      # a worse retry can't turn it red again


def test_alert_checkin_turns_the_card_green(clk):
    mk("alert", "local_alert", agent="terra", bands=["junior", "middle", "senior"], at=ago(hours=2), city="Pune", citySlug="pune")
    u = student()
    assert states(asyncio.run(posts.feed(u)))["alert"] == "new"
    posts.checkin(users.get_user("kid"), "alert")
    assert states(asyncio.run(posts.feed(users.get_user("kid"))))["alert"] == "done"


# ------------------------------------------------------------------ the Today tab
def test_today_tab_has_only_todays_posts_and_todays_alert(clk):
    mk("t1", at=ago(hours=1)); mk("t2", at=ago(hours=5))                      # 11:00 and 07:00 IST today
    mk("early", at=ago(hours=11, minutes=30))                                 # 00:30 IST today (UTC says yesterday)
    mk("yday", at=ago(hours=13)); mk("old", at=ago(days=3)); mk("pinned", at=ago(days=9), pinned=True)
    mk("alert-today", "local_alert", agent="terra", bands=["junior", "middle", "senior"], at=ago(hours=6), city="Pune", citySlug="pune")
    mk("alert-yday", "local_alert", agent="terra", bands=["junior", "middle", "senior"], at=ago(hours=30), city="Pune", citySlug="pune")
    u = student()
    today = [r["id"] for r in asyncio.run(posts.feed(u, "today"))]
    assert today == ["alert-today", "t1", "t2", "early"]                       # alert first, then newest first; no yesterday, no pinned oldies
    foryou = [r["id"] for r in asyncio.run(posts.feed(users.get_user("kid"), "foryou"))]
    assert set(foryou) == {"alert-today", "t1", "t2", "early", "yday", "old", "pinned"} and "alert-yday" not in foryou
    assert feed.latest(u, "foryou")["todayCount"] == 4 == feed.latest(u, "today")["todayCount"]
    assert [p["id"] for p in feed.visible(student("junior-kid", 4), "today")] == ["alert-today"]   # a Class 4 child sees no middle-band posts, only the all-class alert


def test_today_tab_respects_class_band_and_topics(clk):
    mk("mid", agent="signal", bands=["middle"], at=ago(hours=1)); mk("senior-only", bands=["senior"], at=ago(hours=1)); mk("fire", agent="ember", at=ago(hours=1))
    u = student()
    u["parentSettings"]["topics"]["fire"] = False
    users.save(u)
    assert [r["id"] for r in asyncio.run(posts.feed(users.get_user("kid"), "today"))] == ["mid"]


def test_feed_tabs_and_states_through_the_http_api(clk, v3_client):
    """The new GET /api/feed (feed_api) must answer instead of the older one in routers/api.py, which rejects tab=today."""
    mk("n", at=ago(minutes=20)); mk("o", at=ago(hours=40))
    h = {"X-Demo-User": "http-kid"}
    r = v3_client.get("/api/feed", params={"tab": "today"}, headers=h)
    assert r.status_code == 200 and [p["id"] for p in r.json()] == ["n"] and r.json()[0]["state"] == "new"
    foryou = {p["id"]: p["state"] for p in v3_client.get("/api/feed", headers=h).json()}
    assert foryou == {"n": "new", "o": "none"}
    assert v3_client.get("/api/feed", params={"tab": "bogus"}, headers=h).status_code == 400
    lat = v3_client.get("/api/feed/latest", headers=h).json()
    assert lat["todayCount"] == 1 and lat["newCount"] == 0 and lat["latest"]
    assert "answerKey" not in r.json()[0] and "rubric" not in r.json()[0]    # still no answer keys in the feed


def test_new_feed_route_wins_over_the_old_one():
    from app.main import app
    gets = [r for r in app.routes if getattr(r, "path", None) == "/api/feed" and "GET" in getattr(r, "methods", set())]
    assert gets and gets[0].endpoint.__module__.endswith("routers.feed_api")
