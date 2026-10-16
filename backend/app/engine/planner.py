"""
Novelty planner: picks a fresh combination (agent × card × format × band × setting × character × twist × time)
that this agent has used least recently. Coverage is stored per agent in the `coverage` collection.
"""
from __future__ import annotations

import hashlib
import random
from typing import Optional

from ..store.base import get_db
from . import cards as C

KINDS = ("scenario", "poll", "myth_fact", "scam_legit")
KIND_WEIGHTS = {"scenario": 4, "poll": 3, "myth_fact": 2, "scam_legit": 3}


def supported_kinds(card: dict, llm: bool) -> list[str]:
    ks = []
    if card.get("scenario") or (llm and card["agentId"] != "compass"):
        ks.append("scenario")
    if card.get("quiz") or llm:
        ks.append("poll")
    if card.get("myths") or llm:
        ks.append("myth_fact")
    if card.get("scams") or (llm and card["agentId"] == "cipher"):
        ks.append("scam_legit")
    return ks


def combo_key(c: dict) -> str:
    raw = "|".join(str(c.get(k)) for k in ("cardId", "kind", "band", "setting", "character", "twist", "variant"))
    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def plan(agent_id: str, llm: bool, kind: Optional[str] = None, band: Optional[str] = None,
         rng: Optional[random.Random] = None, candidates: int = 16) -> Optional[dict]:
    rng = rng or random.Random()
    a = C.agent(agent_id)
    if not a:
        return None
    combos = C.combos()
    db = get_db()
    cov = db.get("coverage", agent_id) or {"used": {}, "recentCards": []}
    pool = []
    for _ in range(candidates * 3):
        b = band or rng.choice([x for x in C.BANDS if x != "junior" or a["minGrade"] <= 5])
        cards = C.cards_for(agent_id, b)
        if not cards:
            continue
        card = rng.choice(cards)
        kinds = [k for k in supported_kinds(card, llm) if kind in (None, k)]
        if not kinds:
            continue
        k = rng.choices(kinds, weights=[KIND_WEIGHTS[x] for x in kinds])[0]
        variant = rng.randrange(8)
        c = {"agentId": agent_id, "cardId": card["id"], "kind": k, "band": b,
             "setting": rng.choice(combos["settings"][b]), "character": rng.choice(combos["characters"]),
             "relation": rng.choice(combos["relations"]), "twist": rng.choice(combos["twists"]),
             "time": rng.choice(combos["times"]), "difficulty": combos["difficulty"][b], "variant": variant}
        c["key"] = combo_key(c)
        recent_penalty = 3 if card["id"] in cov.get("recentCards", [])[-4:] else 0
        c["_cost"] = cov["used"].get(c["key"], 0) * 10 + recent_penalty + rng.random()
        pool.append(c)
        if len(pool) >= candidates:
            break
    if not pool:
        return None
    best = min(pool, key=lambda x: x["_cost"])
    best.pop("_cost")
    return best


def mark_used(combo: dict) -> None:
    db = get_db()
    cov = db.get("coverage", combo["agentId"]) or {"used": {}, "recentCards": []}
    cov["used"][combo["key"]] = cov["used"].get(combo["key"], 0) + 1
    cov["recentCards"] = (cov.get("recentCards", []) + [combo["cardId"]])[-20:]
    db.put("coverage", combo["agentId"], cov)
