"""Feed, post views, votes, check-ins, scenario answers and top responses."""
from __future__ import annotations

import asyncio
import logging

from fastapi import HTTPException

from ..ai import prompts
from ..ai.llm import get_llm
from ..engine import cards as C
from ..engine.generator import POSTS
from ..engine.local_alerts import build_alert
from ..judge import scoring
from ..judge.judge import judge
from ..judge.moderation import moderate
from ..store.base import get_db
from . import clock, users

log = logging.getLogger("wotnow.posts")
HIDDEN = {"rubric", "dangerousActions", "dangerPatterns", "modelAnswer", "answerKey", "explanation", "voteCounts", "scoreSum",
          "combo", "status", "source", "quality", "conditions", "citySlug", "checkins"}
RESP = "responses"


def public(p: dict, my: dict | None = None) -> dict:
    out = {k: v for k, v in p.items() if k not in HIDDEN}
    if p["type"] == "local_alert":
        out["stats"] = {"responses": p.get("checkins", 0) + p.get("stats", {}).get("responses", 0)}
    out["my"] = my
    return out


def get_post(post_id: str) -> dict:
    p = get_db().get(POSTS, post_id)
    if not p or p.get("status") != "live":
        raise HTTPException(404, "Post not found")
    return p


def _allowed(u: dict, p: dict) -> bool:
    a = C.agent(p["agentId"])
    topics = u.get("parentSettings", {}).get("topics", {})
    return (u["band"] in p.get("bands", []) and a and topics.get(a["domain"], True) and u["grade"] >= a["minGrade"])


async def feed(u: dict, tab: str = "foryou", agent_id: str | None = None, limit: int = 30) -> list[dict]:
    db = get_db()
    city_slug = None
    try:
        alert = await asyncio.wait_for(build_alert(u.get("city") or "Pune"), timeout=12)
        city_slug = alert.get("citySlug")
    except Exception as exc:
        log.warning("local alert unavailable: %s", exc)
    posts = [p for p in db.query(POSTS) if p.get("status") == "live"]
    posts = [p for p in posts if p["type"] != "local_alert" or p.get("citySlug") == city_slug]
    posts = [p for p in posts if _allowed(u, p)]
    if agent_id:
        posts = [p for p in posts if p["agentId"] == agent_id]
    elif tab == "following":
        posts = [p for p in posts if p["agentId"] in u.get("follows", [])]
    elif tab == "near":
        posts = [p for p in posts if p["type"] == "local_alert" or p["agentId"] in ("terra", "civic")]
    today = clock.today().isoformat()
    posts.sort(key=lambda p: (p["type"] == "local_alert" and p["createdAt"][:10] >= today[:10], p["createdAt"]), reverse=True)
    my = users.my_state(u["id"])
    return [public(p, my.get(p["id"])) for p in posts[:limit]]


# ---------------- votes ----------------
def _correct_key(p: dict) -> str:
    return p["answerKey"]


def vote_result(p: dict, choice: str, xp: int = 0) -> dict:
    counts = p.get("voteCounts", {})
    total = sum(counts.values()) or 1
    keys = [o["id"] for o in p.get("options") or []] or (["myth", "fact"] if p["type"] == "myth_fact" else ["scam", "legit"])
    dist = {k: round(counts.get(k, 0) * 100 / total) for k in keys}
    return {"choice": choice, "correct": _correct_key(p), "isCorrect": choice == _correct_key(p), "distribution": dist,
            "explanation": p.get("explanation", ""), "xpAwarded": xp}


def vote(u: dict, post_id: str, choice: str) -> dict:
    p = get_post(post_id)
    if p["type"] not in ("poll", "myth_fact", "scam_legit"):
        raise HTTPException(400, "This post can't be voted on")
    valid = [o["id"] for o in p.get("options") or []] or (["myth", "fact"] if p["type"] == "myth_fact" else ["scam", "legit"])
    if choice not in valid:
        raise HTTPException(400, f"choice must be one of {valid}")
    prev = users.get_my(u["id"], post_id)
    if prev and prev.get("choice"):
        return vote_result(p, prev["choice"], 0)
    users.enforce_limits(u)
    p.setdefault("voteCounts", {})[choice] = p["voteCounts"].get(choice, 0) + 1
    p["stats"]["responses"] = p["stats"].get("responses", 0) + 1
    get_db().put(POSTS, p["id"], p)
    ok = choice == p["answerKey"]
    good, bad = scoring.XP_VOTE[p["type"]]
    xp = good if ok else bad
    domain = C.agent(p["agentId"])["domain"]
    if ok and p["type"] == "scam_legit":
        u.setdefault("counts", {})["scamCorrect"] = u["counts"].get("scamCorrect", 0) + 1
    users.record(u, "vote", xp, post=p, score=100 if ok else 0, domain=domain)
    users.set_my(u["id"], post_id, {"choice": choice})
    return vote_result(p, choice, xp)


def my_vote(u: dict, post_id: str) -> dict | None:
    p = get_post(post_id)
    m = users.get_my(u["id"], post_id)
    return vote_result(p, m["choice"]) if m and m.get("choice") else None


def checkin(u: dict, post_id: str) -> dict:
    p = get_post(post_id)
    if p["type"] != "local_alert":
        raise HTTPException(400, "Only local alerts support check-ins")
    if (users.get_my(u["id"], post_id) or {}).get("checkedIn"):
        return {"xpAwarded": 0}
    users.enforce_limits(u)
    p["checkins"] = p.get("checkins", 0) + 1
    get_db().put(POSTS, p["id"], p)
    u.setdefault("counts", {})["checkins"] = u["counts"].get("checkins", 0) + 1
    users.record(u, "checkin", scoring.XP_CHECKIN, post=p)
    users.set_my(u["id"], post_id, {"checkedIn": True})
    return {"xpAwarded": scoring.XP_CHECKIN}


# ---------------- scenario answers ----------------
async def answer(u: dict, post_id: str, text: str) -> dict:
    p = get_post(post_id)
    if p["type"] != "scenario":
        raise HTTPException(400, "Only scenarios take written answers")
    text = (text or "").strip()[:600]
    if len(text) < 3:
        raise HTTPException(400, "Answer is empty")
    users.enforce_limits(u)
    ev, mod = await asyncio.gather(judge(p, text, u["band"]), moderate(text))
    prev = users.get_my(u["id"], post_id) or {}
    best_before = prev.get("score", 0) if prev.get("answered") else 0
    first = not prev.get("answered")
    xp_total = scoring.answer_xp(ev["score"])
    xp = xp_total if first else max(0, xp_total - scoring.answer_xp(best_before))   # retries only earn the improvement
    db = get_db()
    visible = mod["label"] == "ok" and not ev["dangerous"]
    db.put(f"{POSTS}/{post_id}/{RESP}", u["id"], {
        "id": u["id"], "nickname": u["nickname"], "avatar": u["avatar"], "text": text, "score": ev["score"], "hits": ev["hits"],
        "dangerous": ev["dangerous"], "moderation": mod, "visible": visible, "createdAt": clock.utc_iso(), "expertReply": None})
    if first:
        p["stats"]["responses"] = p["stats"].get("responses", 0) + 1
        p["scoreSum"] = p.get("scoreSum", 0) + ev["score"]
        p["stats"]["avgScore"] = round(p["scoreSum"] / p["stats"]["responses"])
        db.put(POSTS, p["id"], p)
        u["answers"] = u.get("answers", 0) + 1
        u["scoreSum"] = u.get("scoreSum", 0) + ev["score"]
    missed = next((c["point"] for c in ev["checklist"] if not c["hit"]), None)
    domain = C.agent(p["agentId"])["domain"]
    u = users.record(u, "answer", xp, post=p, score=ev["score"], domain=domain, missed=missed,
                     extra={"judgedBy": ev["judgedBy"], "blocked": mod["label"] != "ok"})
    users.set_my(u["id"], post_id, {"answered": True, "score": max(ev["score"], best_before)})
    pub = users.public(u)
    return {"score": ev["score"], "label": ev["label"], "checklist": ev["checklist"], "dangerous": ev["dangerous"],
            "dangerousReason": ev["dangerousReason"], "feedback": ev["feedback"], "sourceCards": p["sourceCards"],
            "xpAwarded": xp, "judgedBy": ev["judgedBy"], "me": {"xp": pub["xp"], "level": pub["level"], "streak": pub["streak"]}}


def _template_reply(p: dict, r: dict) -> str:
    missed = [x for x in p["rubric"] if x["id"] not in set(r.get("hits", []))]
    if not missed:
        card = C.card(p["sourceCards"][0]["id"]) if p.get("sourceCards") else None
        tip = (card or {}).get("do", [""])[-1]
        return f"Textbook answer! 🙌 {tip}." if tip else "Textbook answer! 🙌"
    return f"Good thinking! One more step: {missed[0]['point'][0].lower() + missed[0]['point'][1:]}."


async def top_responses(p: dict, limit: int = 3) -> list[dict]:
    if p["type"] != "scenario":
        return []
    db = get_db()
    coll = f"{POSTS}/{p['id']}/{RESP}"
    rs = [r for r in db.query(coll) if r.get("visible")]
    rs.sort(key=lambda r: (r["score"], r.get("createdAt", "")), reverse=True)
    rs = rs[:limit]
    agent = C.agent(p["agentId"])
    llm = get_llm()
    for r in rs:
        if not r.get("expertReply"):
            text = None
            if llm.available:
                text = await llm.generate_text(prompts.SYSTEM_REPLY.format(name=agent["name"], domain=agent["domainLabel"]),
                                               f"SCENARIO: {p['body']} {p.get('question', '')}\nSTUDENT ANSWER: <<<{r['text']}>>>", temperature=0.6)
            r["expertReply"] = (text or _template_reply(p, r))[:220]
            db.put(coll, r["id"], r)
    return [{"id": r["id"], "nickname": r["nickname"], "avatar": r["avatar"], "text": r["text"], "score": r["score"],
             "expertPick": i == 0 and r["score"] >= 90, "expertReply": r["expertReply"]} for i, r in enumerate(rs)]
