"""
Scenario answer judge.
Gemini decides WHICH rubric points the answer covers (by meaning) and whether it's dangerous, and writes feedback.
Code computes the score. Offline: keyword patterns from the fact card rubric, with a negation guard.
"""
from __future__ import annotations

import re

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import JudgeOut
from ..config import get_settings
from . import scoring

NEGATION = re.compile(r"(no|not|never|don'?t|do not|stop|avoid|instead of|without|rather than)\b[^.]{0,30}$", re.I)
STOP = set("the a an to of and or in on at for with is are be it this that you your they them he she his her if then so do".split())


def _overlap_hit(point: str, text: str) -> bool:
    words = [w for w in re.findall(r"[a-z]+", point.lower()) if w not in STOP and len(w) > 3]
    t = text.lower()
    found = sum(1 for w in words if w[:5] in t)
    return bool(words) and found / len(words) >= 0.5


def offline_judge(post: dict, text: str) -> dict:
    hits = set()
    for r in post["rubric"]:
        if r.get("keys"):
            if re.search(r["keys"], text, re.I):
                hits.add(r["id"])
        elif _overlap_hit(r["point"], text):
            hits.add(r["id"])
    dangerous, reason = False, ""
    for pat in post.get("dangerPatterns", []):
        m = re.search(pat, text, re.I)
        if m and not NEGATION.search(text[max(0, m.start() - 45):m.start()]):
            dangerous, reason = True, f"'{m.group(0)}' could make things worse"
            break
    return {"hits": hits, "dangerous": dangerous, "dangerous_reason": reason, "feedback": None, "by": "rules"}


def template_feedback(post: dict, hits: set[str], dangerous: bool, score: int) -> str:
    missed = [r for r in post["rubric"] if r["id"] not in hits]
    missed.sort(key=lambda r: (not r.get("critical"), -r["weight"]))
    if dangerous:
        first = missed[0]["note"] if missed else ""
        return f"Part of your answer could make things worse. {first} Remember: {post['rubric'][0]['point'].lower()}.".strip()
    if not missed:
        return "You covered every key step. That’s exactly what an expert would do! 🎉"
    good = "You avoided the most dangerous mistake. " if score >= 60 else "Good start. "
    return f"{good}Next time, remember to {missed[0]['point'][0].lower() + missed[0]['point'][1:]}. {missed[0]['note']}"


async def judge(post: dict, text: str, band: str) -> dict:
    short = len(text.strip()) < 12
    llm = get_llm()
    res = None
    if llm.available and not short:
        system = prompts.SYSTEM_JUDGE.format(audience_short={"junior": "young (8-10 year old)", "middle": "middle-school", "senior": "high-school"}.get(band, "school"))
        out = await llm.generate_json(system, prompts.judge_prompt(post, text), JudgeOut, temperature=get_settings().JUDGE_TEMPERATURE)
        if out is not None:
            valid = {r["id"] for r in post["rubric"]}
            res = {"hits": {h for h in out.get("hits", []) if h in valid}, "dangerous": bool(out.get("dangerous")),
                   "dangerous_reason": out.get("dangerous_reason", ""), "feedback": (out.get("feedback") or "").strip() or None, "by": "gemini"}
            # safety net: a matching danger pattern overrides a missed danger flag
            off = offline_judge(post, text)
            if off["dangerous"] and not res["dangerous"]:
                res["dangerous"], res["dangerous_reason"] = True, off["dangerous_reason"]
    if res is None:
        res = offline_judge(post, text)
    sc = scoring.score(post["rubric"], res["hits"], res["dangerous"], short)
    feedback = res["feedback"] or template_feedback(post, res["hits"], res["dangerous"], sc)
    if short:
        feedback = "Tell us a bit more! Write the steps you would actually take, in your own words."
    checklist = [{"id": r["id"], "point": r["point"], "hit": r["id"] in res["hits"], "note": r["note"]} for r in post["rubric"]]
    missed = sum(1 for c in checklist if not c["hit"])
    return {"score": sc, "label": scoring.label(sc, res["dangerous"], missed), "checklist": checklist,
            "dangerous": res["dangerous"], "dangerousReason": res["dangerous_reason"] or None,
            "feedback": feedback, "hits": sorted(res["hits"]), "judgedBy": res["by"]}
