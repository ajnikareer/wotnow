"""Parent dashboard: time, weekly activity, skills, recent answers, AI talking points, safety, controls."""
from __future__ import annotations

from datetime import timedelta

from fastapi import HTTPException

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import StartersOut
from ..engine import cards as C
from ..judge import scoring
from . import clock, users


def _when(day: str) -> str:
    t = clock.today()
    if day == t.isoformat():
        return "Today"
    if day == (t - timedelta(days=1)).isoformat():
        return "Yesterday"
    return day


def _template_starters(recent: list[dict]) -> list[str]:
    out = []
    for r in recent:
        if r.get("missed") and len(out) < 2:
            out.append(f"Ask: “{r['postTitle']}: what would you do?” Then talk about this step: {r['missed'].lower()}.")
    out.append("Show them where the main switch, gas valve and fire exit are at home. It takes 2 minutes.")
    out.append("Practise together: what number do we call in an emergency in India? (112)")
    return out[:3]


async def summary(u: dict) -> dict:
    acts = users.activity(u["id"])
    today = clock.today()
    week = []
    for i in range(6, -1, -1):
        d = today - timedelta(days=i)
        day_acts = [a for a in acts if a["date"] == d.isoformat()]
        week.append({"day": d.strftime("%a"), "minutes": round(sum(scoring.MINUTES.get(a["kind"], 0) for a in day_acts)),
                     "answers": sum(1 for a in day_acts if a["kind"] in ("answer", "vote"))})
    answered = [a for a in acts if a["kind"] == "answer"][-6:][::-1]
    recent = [{"postTitle": a["postTitle"], "agentId": a["agentId"], "score": a["score"], "when": _when(a["date"]),
               **({"missed": a["missed"]} if a.get("missed") and a["score"] < 100 else {})} for a in answered[:4]]
    starters = None
    llm = get_llm()
    if llm.available and answered:
        r = await llm.generate_json(prompts.SYSTEM_STARTERS,
                                    "RECENT ANSWERS: " + str([{k: a.get(k) for k in ("postTitle", "score", "missed")} for a in answered]),
                                    StartersOut, temperature=0.6)
        if r and len(r.get("starters", [])) >= 3:
            starters = r["starters"][:3]
    pub = users.public(u)
    s = u.get("parentSettings") or users.default_settings(u["grade"])
    blocked = sum(1 for a in acts if a.get("blocked"))
    return {"child": {k: pub[k] for k in ("nickname", "avatar", "grade", "streak", "xp", "levelName", "skills")},
            "minutesToday": round(users.minutes_on(u["id"], today)), "dailyLimit": s["dailyLimit"], "week": week,
            "recent": recent, "conversationStarters": starters or _template_starters(recent),
            "safety": {"flaggedReplies": 0, "blockedContent": blocked, "dms": "disabled"}, "settings": s}


async def update_settings(u: dict, s: dict) -> dict:
    try:
        lim = int(s.get("dailyLimit", 30))
    except (TypeError, ValueError):
        raise HTTPException(400, "dailyLimit must be a number")
    topics = {d: bool((s.get("topics") or {}).get(d, True)) for d in users.ALL_DOMAINS}
    if u["grade"] < 9:
        topics["careers"] = False
    u["parentSettings"] = {"dailyLimit": max(5, min(180, lim)), "quietHours": str(s.get("quietHours", ""))[:20],
                           "weeklyEmail": bool(s.get("weeklyEmail", True)), "topics": topics}
    users.save(u)
    return await summary(u)
