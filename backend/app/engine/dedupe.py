"""
Duplicate check for new posts.
Primary: Vertex AI text embeddings (cosine). Fallback (mock/offline or embedding error): character-trigram cosine.
"""
from __future__ import annotations

import math
import re
from collections import Counter

from ..ai.llm import get_llm
from ..config import get_settings
from ..store.base import get_db

VEC = "post_vectors"


def post_text(p: dict) -> str:
    parts = [p.get("title", ""), p.get("body", ""), p.get("question", ""), p.get("statement", ""),
             (p.get("message") or {}).get("text", ""), " ".join(o["text"] for o in p.get("options") or [])]
    return " ".join(x for x in parts if x).strip()


def _tri(text: str) -> Counter:
    t = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    t = re.sub(r"\s+", " ", t)
    return Counter(t[i:i + 3] for i in range(max(0, len(t) - 2)))


def _cos_counter(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(k, 0) for k, v in a.items())
    return dot / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())))


def _cos(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


async def check(candidate: dict, agent_id: str, recent: list[dict]) -> tuple[bool, float, list[float] | None, str]:
    """Returns (is_duplicate, max_similarity, embedding_or_None, method)."""
    s = get_settings()
    text = post_text(candidate)
    vec = await get_llm().embed(text)
    if vec:
        db = get_db()
        best = 0.0
        for p in recent:
            v = (db.get(VEC, p["id"]) or {}).get("vec")
            if v:
                best = max(best, _cos(vec, v))
        return best >= s.DEDUPE_THRESHOLD, round(best, 3), vec, "embedding"
    tri = _tri(text)
    best = max((_cos_counter(tri, _tri(post_text(p))) for p in recent), default=0.0)
    return best >= s.DEDUPE_FALLBACK_THRESHOLD, round(best, 3), None, "trigram"


def save_vector(post_id: str, agent_id: str, vec: list[float] | None) -> None:
    if vec:
        get_db().put(VEC, post_id, {"id": post_id, "agentId": agent_id, "vec": vec})
