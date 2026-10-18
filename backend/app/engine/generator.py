"""
Content engine: plan → generate (Gemini, or fact-card templates offline) → validate → dedupe → publish.
"""
from __future__ import annotations

import hashlib
import logging
import random
import re
from datetime import datetime, timezone
from typing import Optional

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import MythDraft, PollDraft, ScamDraft, ScenarioDraft
from ..config import get_settings
from ..store.base import get_db
from . import cards as C
from . import dedupe, planner
from .validator import validate

log = logging.getLogger("wotnow.engine")
POSTS = "posts"
OPT_IDS = "abcd"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _cap_sentences(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), s)


def at_phrase(setting: str) -> str:
    s = setting.strip()
    if s == "home":
        return "at home"
    if s.startswith("online"):
        return "in an " + s
    if any(w in s for w in ("bus", "train", "metro", "platform")):
        return "on the " + s
    return "at the " + s


def the_phrase(setting: str) -> str:
    return "home" if setting == "home" else "the " + setting


def _fill(t: str, combo: dict) -> str:
    at = at_phrase(combo["setting"])
    return _cap_sentences(t.format(name=combo["character"], relation=combo["relation"], setting=combo["setting"], time=combo["time"],
                                   at=at, At=at[0].upper() + at[1:], the=the_phrase(combo["setting"])))


def _new_id(combo: dict) -> str:
    h = hashlib.sha1(f"{combo['key']}{now_iso()}{random.random()}".encode()).hexdigest()[:8]
    return f"{combo['agentId']}-{combo['kind'].replace('_', '')}-{h}"


def _base(combo: dict, kind: str, title: str, card_ids: list[str], source: str) -> dict:
    return {"id": _new_id(combo), "agentId": combo["agentId"], "type": kind, "createdAt": now_iso(),
            "bands": [combo["band"]], "title": title, "sourceCards": C.source_cards(card_ids),
            "status": "live", "source": source, "combo": {k: v for k, v in combo.items() if k != "key"} | {"key": combo["key"]},
            "stats": {"responses": 0, "avgScore": None}, "voteCounts": {}, "scoreSum": 0}


# ---------------- offline / template generation (from fact cards) ----------------
def from_card(combo: dict, used_texts: set[str] | None = None) -> Optional[dict]:
    card = C.card(combo["cardId"])
    kind = combo["kind"]
    used_texts = used_texts or set()
    v = combo.get("variant", 0)
    if kind == "scenario" and card.get("scenario"):
        sc = card["scenario"]
        sit = sc["situations"][v % len(sc["situations"])]
        combo = dict(combo)
        if sc.get("settings") and combo["setting"] not in sc["settings"]:
            combo["setting"] = sc["settings"][v % len(sc["settings"])]
        if sc.get("times") and combo["time"] not in sc["times"]:
            combo["time"] = sc["times"][v % len(sc["times"])]
        p = _base(combo, kind, card["title"], [card["id"]], "cards")
        p.update(body=_fill(sit, combo), question=_fill(sc["question"], combo),
                 scene={"emojis": sc["emojis"], "bubble": sc.get("bubble")},
                 rubric=[{"id": f"r{i + 1}", "point": r["point"], "note": r["note"], "weight": r["weight"],
                          "critical": r["critical"], "card": card["id"], "keys": r["keys"]} for i, r in enumerate(sc["rubric"])],
                 dangerousActions=card.get("dont", [])[:4], dangerPatterns=sc.get("dangerous", []),
                 modelAnswer=" ".join(card.get("do", [])[:4]))
        return p
    if kind == "poll" and card.get("quiz"):
        items = [q for q in card["quiz"] if q["q"] not in used_texts] or card["quiz"]
        q = items[v % len(items)]
        p = _base(combo, kind, card["title"], [card["id"]], "cards")
        p.update(body="Quick check:", question=q["q"], options=[{"id": OPT_IDS[i], "text": t} for i, t in enumerate(q["options"])],
                 answerKey=OPT_IDS[q["correct"]], explanation=q["explanation"])
        p["bands"] = card["bands"]
        return p
    if kind == "myth_fact" and card.get("myths"):
        items = [m for m in card["myths"] if f'“{m["statement"]}”' not in used_texts] or card["myths"]
        m = items[v % len(items)]
        p = _base(combo, kind, card["title"], [card["id"]], "cards")
        st = m["statement"].strip()
        is_q = st.endswith("?") or st.lower().startswith(("should", "can", "is", "do", "does", "would", "could", "are"))
        body = "Quick question:" if is_q else "True or false?"
        if "myth" in st.lower() or "believe" in st.lower():
            body = "Lots of people believe this. Do you?"
        p.update(body=body, statement=f'“{st}”', answerKey=m["answer"],
                 explanation=m["truth"])
        p["bands"] = card["bands"]
        return p
    if kind == "scam_legit" and card.get("scams"):
        items = [s for s in card["scams"] if s["text"] not in used_texts] or card["scams"]
        s = items[v % len(items)]
        p = _base(combo, kind, card["title"], [card["id"]], "cards")
        p.update(body="This message just arrived. Is it real?", message={"from": s["from"], "text": s["text"]},
                 answerKey=s["answer"], explanation=s["explanation"])
        p["bands"] = card["bands"]
        return p
    return None


# ---------------- Gemini generation ----------------
SCHEMA = {"scenario": ScenarioDraft, "poll": PollDraft, "myth_fact": MythDraft, "scam_legit": ScamDraft}


def _from_draft(combo: dict, d: dict, card_ids: list[str]) -> dict:
    kind = combo["kind"]
    p = _base(combo, kind, d.get("title", "").strip(), card_ids, "gemini")
    if kind == "scenario":
        p.update(body=d["body"].strip(), question=d["question"].strip(),
                 scene={"emojis": d.get("scene_emojis", []), "bubble": d.get("scene_bubble")},
                 rubric=[dict(r) for r in d.get("rubric", [])], dangerousActions=d.get("dangerous_actions", []),
                 dangerPatterns=[], modelAnswer=d.get("model_answer", ""))
    elif kind == "poll":
        p.update(body=d["body"].strip(), question=d["question"].strip(),
                 options=[{"id": OPT_IDS[i], "text": o["text"].strip()} for i, o in enumerate(d.get("options", [])[:4])],
                 answerKey=OPT_IDS[d["correct_index"]] if 0 <= d.get("correct_index", -1) < 4 else None, explanation=d["explanation"])
    elif kind == "myth_fact":
        st = d["statement"].strip().strip('"“”')
        p.update(body="Lots of people believe this. Do you?", statement=f"“{st}”", answerKey=d["answer"].lower().strip(), explanation=d["explanation"])
    elif kind == "scam_legit":
        p.update(body="This message just arrived. Is it real?", message={"from": d["sender"], "text": d["text"]},
                 answerKey=d["answer"].lower().strip(), explanation=d["explanation"])
    return p


def recent_posts(agent_id: str, limit: int = 60) -> list[dict]:
    ps = [p for p in get_db().query(POSTS, agentId=agent_id) if p.get("status") == "live"]
    return sorted(ps, key=lambda p: p["createdAt"], reverse=True)[:limit]


async def generate_one(agent_id: str, kind: Optional[str] = None, band: Optional[str] = None,
                       publish: bool = True, rng: Optional[random.Random] = None, local: dict | None = None) -> dict:
    """Returns a report dict: {ok, post?, attempts:[...]}"""
    s = get_settings()
    llm = get_llm()
    use_llm = llm.available
    recent = recent_posts(agent_id)
    used_texts = {p.get("question") or p.get("statement") or (p.get("message") or {}).get("text") for p in recent}
    attempts = []
    for _ in range(s.MAX_GEN_ATTEMPTS):
        combo = planner.plan(agent_id, use_llm, kind=kind, band=band, rng=rng)
        if not combo:
            attempts.append({"error": "no plannable combination"})
            break
        planner.mark_used(combo)
        card = C.card(combo["cardId"])
        related = [c for c in C.cards_for(agent_id) if c["id"] != card["id"]][:1]
        allowed = [card] + related
        post = None
        if use_llm:
            agent = C.agent(agent_id)
            draft = await llm.generate_json(
                prompts.agent_system(agent, combo["band"]),
                prompts.generation_prompt(combo["kind"], {k: combo[k] for k in ("band", "difficulty", "setting", "character", "relation", "twist", "time")},
                                          allowed, local, [p.get("title", "") + ": " + (p.get("question") or p.get("statement") or "") for p in recent[:8]]),
                SCHEMA[combo["kind"]], temperature=s.GEN_TEMPERATURE)
            if draft:
                try:
                    post = _from_draft(combo, draft, [c["id"] for c in allowed])
                except Exception as exc:
                    attempts.append({"combo": combo["key"], "error": f"bad draft: {exc}"})
                    continue
        if post is None:
            post = from_card(combo, used_texts)
        if post is None:
            attempts.append({"combo": combo["key"], "error": "card has no material for this format"})
            continue
        post, issues = validate(post, {c["id"] for c in allowed})
        if post is None:
            attempts.append({"combo": combo["key"], "error": "validation", "issues": issues})
            continue
        dup, sim, vec, method = await dedupe.check(post, agent_id, recent)
        if dup:
            attempts.append({"combo": combo["key"], "error": "duplicate", "similarity": sim, "method": method})
            continue
        post["quality"] = {"similarity": sim, "dedupe": method, "warnings": post.pop("_warnings", [])}
        if publish:
            get_db().put(POSTS, post["id"], post)
            dedupe.save_vector(post["id"], agent_id, vec)
        attempts.append({"combo": combo["key"], "ok": True, "similarity": sim, "method": method})
        return {"ok": True, "post": post, "attempts": attempts}
    return {"ok": False, "attempts": attempts}
