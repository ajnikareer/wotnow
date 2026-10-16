"""Content engine, validator, dedupe and fact-card integrity."""
import asyncio
import random
import re


def test_cards_integrity():
    from app.engine import cards as C
    ids = [c["id"] for c in C.all_cards()]
    assert len(ids) == len(set(ids)) and len(ids) >= 30
    for c in C.all_cards():
        assert C.agent(c["agentId"]) and c["bands"] and c["facts"] and c["do"]
        if c.get("scenario"):
            assert sum(r["weight"] for r in c["scenario"]["rubric"]) == 100
            for r in c["scenario"]["rubric"]:
                re.compile(r["keys"])


def test_every_agent_can_generate_offline():
    from app.store.base import reset_db
    from app.engine.generator import generate_one
    reset_db()
    rng = random.Random(1)
    for a in ["ember", "signal", "pulse", "basil", "civic", "terra", "cipher", "compass"]:
        r = asyncio.run(generate_one(a, rng=rng))
        assert r["ok"], (a, r["attempts"])
        p = r["post"]
        assert p["sourceCards"] and p["type"] in ("scenario", "poll", "myth_fact", "scam_legit")
        if p["type"] == "scenario":
            assert sum(x["weight"] for x in p["rubric"]) == 100 and p["question"].endswith("?")


def test_engine_stops_when_offline_material_runs_out():
    """Offline templates are finite; dedupe must refuse repeats instead of posting duplicates."""
    from app.store.base import reset_db
    from app.engine.generator import generate_one
    reset_db()
    rng = random.Random(2)
    made = [asyncio.run(generate_one("basil", kind="myth_fact", rng=rng)) for _ in range(12)]
    oks = [m["post"]["statement"] for m in made if m["ok"]]
    assert len(oks) == len(set(oks))                      # never duplicates
    assert any(not m["ok"] for m in made)                 # eventually reports "duplicate"


def test_validator_rejects_bad_drafts():
    from app.engine.validator import validate
    base = {"type": "scenario", "title": "Test", "body": "word " * 40, "question": "What now?",
            "rubric": [{"point": "a", "note": "n", "weight": 50, "critical": True, "card": "FIRE-012"},
                       {"point": "b", "note": "n", "weight": 30, "critical": False, "card": "BAD"},
                       {"point": "c", "note": "n", "weight": 30, "critical": False, "card": "FIRE-012"}],
            "scene": {"emojis": ["🔥"], "bubble": "x"}}
    ok, warns = validate(dict(base), {"FIRE-012"})
    assert ok and sum(r["weight"] for r in ok["rubric"]) == 100 and ok["rubric"][1]["card"] == "FIRE-012" and len(ok["scene"]["emojis"]) == 3
    bad = dict(base, body="Give him 500 mg paracetamol. " + "word " * 40)
    assert validate(bad, {"FIRE-012"})[0] is None
    poll = {"type": "poll", "title": "P", "question": "Which?", "options": [{"id": "a", "text": "x"}, {"id": "b", "text": "x"}, {"id": "c", "text": "y"}, {"id": "d", "text": "z"}],
            "answerKey": "a", "explanation": "because it is right"}
    assert validate(poll, {"X"})[0] is None
    scam = {"type": "scam_legit", "title": "S", "message": {"from": "9876543210", "text": "Call 9876543210 now"}, "answerKey": "scam", "explanation": "classic scam pattern here"}
    out = validate(scam, {"X"})[0]
    assert "9876543210" not in out["message"]["text"]


def test_scoring_levels():
    from app.judge.scoring import level_for, score
    assert level_for(0) == (1, "Beginner", 150) and level_for(2340) == (7, "Prepared", 3000)
    rub = [{"id": "r1", "weight": 60}, {"id": "r2", "weight": 40}]
    assert score(rub, {"r1", "r2"}, False, False) == 100 and score(rub, {"r1", "r2"}, True, False) == 40


def test_local_alert_mock():
    from app.store.base import reset_db
    from app.engine.local_alerts import build_alert
    reset_db()
    a = asyncio.run(build_alert("Delhi"))
    assert a["city"] == "New Delhi" and any("AQI 230" in c for c in a["chips"]) and len(a["steps"]) == 3
    b = asyncio.run(build_alert("Bangalore"))
    assert b["citySlug"] == "bengaluru"
