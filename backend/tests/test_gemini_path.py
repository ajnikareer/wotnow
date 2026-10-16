"""Exercises the Gemini code path with a fake provider (no network): drafts → validator → dedupe → publish; judge; replies."""
import asyncio
import random

import pytest


class FakeLLM:
    name, available = "fake", True

    def __init__(self):
        self.calls = []

    async def generate_json(self, system, prompt, schema, temperature=0.4):
        n = schema.__name__
        self.calls.append(n)
        if n == "ScenarioDraft":
            return {"title": "Smoke in the stairwell", "body": "It is late evening. Ivy is coming home when she sees grey smoke "
                    "drifting out of the stairwell door on her floor of the apartment building. A neighbour presses the lift button "
                    "and waves her in. Her phone battery is almost dead and she can hear an alarm ringing somewhere below.",
                    "question": "What should Ivy do?", "scene_emojis": ["🏢", "💨"], "scene_bubble": "Quick, take the lift!",
                    "rubric": [{"point": "Use the stairs, not the lift", "note": "Lifts can fail.", "weight": 40, "critical": True, "card": "FIRE-003"},
                               {"point": "Stay low under smoke", "note": "Cleaner air low.", "weight": 30, "critical": False, "card": "FIRE-003"},
                               {"point": "Call 101 or 112 once safe", "note": "Get help.", "weight": 30, "critical": False, "card": "FIRE-003"}],
                    "dangerous_actions": ["take the lift"], "model_answer": "Avoid the lift, use stairs, stay low, call 101."}
        if n == "PollDraft":
            return {"title": "Pan fire", "body": "Your snack pan is on fire.", "question": "What first?", "options": [{"text": "Water"}, {"text": "Lid"}, {"text": "Fan"}, {"text": "Run"}],
                    "correct_index": 1, "explanation": "A lid cuts off oxygen to the fire."}
        if n == "MythDraft":
            return {"title": "Smoke", "statement": "Smoke is only dangerous if you can see flames", "answer": "myth", "explanation": "Smoke itself is dangerous to breathe."}
        if n == "JudgeOut":
            return {"hits": ["r1", "r3", "zz"], "dangerous": False, "dangerous_reason": "", "feedback": "Great that you used the stairs! Also stay low under smoke."}
        if n == "ModerationOut":
            return {"label": "ok", "reason": ""}
        if n == "AlertDraft":
            return {"title": "Smoggy morning in Delhi", "body": "Air is heavy today.", "steps": ["Play indoors", "Carry water", "Skip burning leaves"], "step_emojis": ["🏠", "💧", "🚫"]}
        if n == "StartersOut":
            return {"starters": ["One", "Two", "Three"]}
        if n == "QuizDraft":
            return {"title": "Fire Blitz", "questions": [{"text": f"Q{i}?", "options": [{"text": "a"}, {"text": "b"}, {"text": "c"}, {"text": "d"}], "correct_index": 2, "explanation": "because"} for i in range(5)]}
        return None

    async def generate_text(self, system, prompt, temperature=0.4):
        return "Nice work using the stairs! 👏"

    async def embed(self, text):
        return None


@pytest.fixture()
def fake(monkeypatch):
    from app.store.base import reset_db
    from app.ai import llm
    reset_db()
    f = FakeLLM()
    monkeypatch.setattr(llm, "_PROVIDER", f)
    return f


def test_gemini_generation_and_judging(fake):
    from app.engine.generator import generate_one
    from app.judge.judge import judge
    r = asyncio.run(generate_one("ember", kind="scenario", rng=random.Random(4)))
    assert r["ok"], r["attempts"]
    p = r["post"]
    assert p["source"] == "gemini" and len(p["scene"]["emojis"]) == 3 and sum(x["weight"] for x in p["rubric"]) == 100
    ev = asyncio.run(judge(p, "Use the stairs and call 101 when outside", "middle"))
    assert ev["judgedBy"] == "gemini" and ev["score"] == 70 and ev["feedback"].startswith("Great")
    # safety net: Gemini missed a danger, but no pattern exists for generated posts -> trust Gemini
    r2 = asyncio.run(generate_one("ember", kind="poll", rng=random.Random(5)))
    assert r2["ok"] and r2["post"]["answerKey"] == "b"


def test_gemini_alert_quiz_starters(fake):
    from app.engine.local_alerts import build_alert
    from app.engine.quiz import build_quiz
    a = asyncio.run(build_alert("Delhi"))
    assert a["source"] == "gemini" and a["title"] == "Smoggy morning in Delhi"
    q = asyncio.run(build_quiz("ember"))
    assert q["title"] == "Fire Blitz" and q["questions"][0]["correct"] == "c"
