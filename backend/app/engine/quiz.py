"""Live fastest-finger quizzes: 5 questions from one agent's fact cards (Gemini or card quiz items)."""
from __future__ import annotations

import random
from datetime import datetime, timezone

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import QuizDraft
from ..store.base import get_db
from . import cards as C

QUIZZES = "live_quizzes"
OPT = "abcd"


def _from_cards(agent_id: str, rng: random.Random) -> list[dict]:
    items = [(c, q) for c in C.cards_for(agent_id) for q in c["quiz"]]
    others = [(c, q) for c in C.all_cards() if c["agentId"] != agent_id and "junior" in c["bands"] for q in c["quiz"]]
    rng.shuffle(items), rng.shuffle(others)
    picked = (items + others)[:5]
    return [{"id": f"q{i + 1}", "text": q["q"], "options": [{"id": OPT[j], "text": t} for j, t in enumerate(q["options"])],
             "correct": OPT[q["correct"]], "explanation": q["explanation"], "card": c["id"]} for i, (c, q) in enumerate(picked)]


async def build_quiz(agent_id: str | None = None, rng: random.Random | None = None) -> dict:
    rng = rng or random.Random()
    agent_id = agent_id or rng.choice(["ember", "signal", "pulse", "cipher", "civic", "terra", "basil"])
    a = C.agent(agent_id)
    title = f"{a['domainLabel']} Blitz"
    qs = None
    llm = get_llm()
    if llm.available:
        d = await llm.generate_json(prompts.SYSTEM_QUIZ.format(name=a["name"], domain=a["domainLabel"], audience="Classes 6-12"),
                                    "FACT CARDS: " + prompts.card_brief(C.cards_for(agent_id)), QuizDraft, temperature=0.7)
        try:
            if d and len(d["questions"]) == 5 and all(len(q["options"]) == 4 and 0 <= q["correct_index"] < 4 for q in d["questions"]):
                qs = [{"id": f"q{i + 1}", "text": q["text"], "options": [{"id": OPT[j], "text": o["text"]} for j, o in enumerate(q["options"])],
                       "correct": OPT[q["correct_index"]], "explanation": q["explanation"]} for i, q in enumerate(d["questions"])]
                title = d.get("title") or title
        except Exception:
            qs = None
    qs = qs or _from_cards(agent_id, rng)
    quiz = {"id": f"quiz-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{agent_id}", "agentId": agent_id, "title": title,
            "createdAt": datetime.now(timezone.utc).isoformat(), "questions": qs}
    get_db().put(QUIZZES, quiz["id"], quiz)
    return quiz


async def current_quiz() -> dict:
    qs = sorted(get_db().query(QUIZZES), key=lambda q: q["createdAt"], reverse=True)
    return qs[0] if qs else await build_quiz()
