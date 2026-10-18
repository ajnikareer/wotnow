"""Public API used by the web app. Shapes match web/src/lib/types.ts exactly."""
from __future__ import annotations

import random
import time
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..auth import get_optional_uid, get_uid
from ..config import get_settings
from ..engine import cards as C
from ..engine.generator import POSTS
from ..engine.quiz import QUIZZES, current_quiz
from ..judge import scoring
from ..services import leaderboard as lb
from ..services import parent as parent_svc
from ..services import posts as P
from ..services import users
from ..store.base import get_db

router = APIRouter(prefix="/api")


class MePatch(BaseModel):
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    grade: Optional[int] = None
    city: Optional[str] = None
    school: Optional[str] = None
    className: Optional[str] = None
    follows: Optional[list[str]] = None


class AnswerIn(BaseModel):
    text: str


class VoteIn(BaseModel):
    choice: str


class QuizIn(BaseModel):
    score: int
    quizId: Optional[str] = None


# ---------- me ----------
@router.get("/me")
async def me(uid: str = Depends(get_uid)):
    return users.public(users.get_user(uid))


@router.post("/me")
async def update_me(body: MePatch, uid: str = Depends(get_uid)):
    return users.public(users.update_profile(users.get_user(uid), body.model_dump(exclude_none=True)))


@router.delete("/me")
async def delete_me(uid: str = Depends(get_uid)):
    users.delete_user(uid)
    return {"deleted": True}


# ---------- agents ----------
def _agent_public(a: dict) -> dict:
    db = get_db()
    live = [p for p in db.query(POSTS, agentId=a["id"]) if p.get("status") == "live"]
    real_users = [u for u in db.query("users") if not u.get("id", "").startswith("seed-") and not u.get("id", "").startswith("demo-")]
    learners = sum(1 for u in real_users if a["id"] in u.get("follows", []))
    return {k: a[k] for k in ("id", "name", "domain", "domainLabel", "emoji", "colors", "bio", "topics", "pillar", "minGrade", "sensitive", "approveFirst") if k in a} | {
        "stats": {
            "posts": len(live),
            "learners": learners,
            "avgScore": 85,
            "factCards": len(C.cards_for(a["id"])),
        }
    }


@router.get("/agents")
async def agents():
    return [_agent_public(a) for a in C.agents()]


@router.get("/agents/{agent_id}")
async def agent(agent_id: str):
    a = C.agent(agent_id)
    if not a:
        raise HTTPException(404, "Expert not found")
    return _agent_public(a)


@router.get("/agents/{agent_id}/cards")
async def agent_cards(agent_id: str):
    return [{k: c[k] for k in ("id", "title", "subtopic", "bands", "facts", "do", "dont", "reviewed")} for c in C.cards_for(agent_id)]


# ---------- feed & posts ----------
@router.get("/feed")
async def feed(tab: str = "foryou", agent: Optional[str] = None, uid: str = Depends(get_uid)):
    if tab not in ("foryou", "following", "near"):
        raise HTTPException(400, "tab must be foryou|following|near")
    return await P.feed(users.get_user(uid), tab, agent)


@router.get("/posts/{post_id}")
async def post(post_id: str, uid: str = Depends(get_uid)):
    p = P.get_post(post_id)
    my = users.get_my(uid, post_id)
    responses = await P.top_responses(p) if (my or {}).get("answered") else []
    return {"post": P.public(p, my), "responses": responses}


@router.post("/posts/{post_id}/answer")
async def answer(post_id: str, body: AnswerIn, uid: str = Depends(get_uid)):
    return await P.answer(users.get_user(uid), post_id, body.text)


@router.post("/posts/{post_id}/vote")
async def vote(post_id: str, body: VoteIn, uid: str = Depends(get_uid)):
    return P.vote(users.get_user(uid), post_id, body.choice)


@router.get("/posts/{post_id}/vote")
async def my_vote(post_id: str, uid: str = Depends(get_uid)):
    return P.my_vote(users.get_user(uid), post_id)


@router.post("/posts/{post_id}/checkin")
async def checkin(post_id: str, uid: str = Depends(get_uid)):
    return P.checkin(users.get_user(uid), post_id)


# ---------- leaderboard ----------
@router.get("/leaderboard")
async def leaderboard(scope: str = "global", uid: str = Depends(get_uid)):
    if scope not in ("global", "country", "city", "class", "school"):
        raise HTTPException(400, "scope must be global|country|city")
    return lb.board(users.get_user(uid), scope)


# ---------- live quiz ----------
def _crowd_scores(quiz_id: str) -> list[int]:
    n = get_settings().DEMO_CROWD
    if n <= 0:
        return []
    rng = random.Random(quiz_id)
    return [max(0, min(100, int(rng.gauss(48, 18)))) for _ in range(n)]


@router.get("/live/next")
async def live_next(uid: Optional[str] = Depends(get_optional_uid)):
    q = await current_quiz()
    quiz_id = q["id"]
    db = get_db()
    now = time.time()

    # Track presence if user has an active identity (session token or demo student)
    if uid:
        try:
            u = users.get_user(uid)
            nick = u.get("nickname") or "Learner"
        except Exception:
            nick = "Learner"
        db.put(f"{QUIZZES}/{quiz_id}/presence", uid, {
            "id": uid,
            "nickname": nick,
            "updatedAt": now,
        })

    # Find all presences active in the last 10 minutes (600 seconds)
    presences = db.query(f"{QUIZZES}/{quiz_id}/presence")
    active_presences = [p for p in presences if p.get("updatedAt", 0) > (now - 600)]

    # Also load completed results
    results = db.query(f"{QUIZZES}/{quiz_id}/results")

    # Build unique active players dictionary
    active_map: dict[str, str] = {}
    for p in active_presences:
        if p.get("id"):
            active_map[p["id"]] = p.get("nickname") or "Learner"
    for r in results:
        if r.get("id"):
            active_map[r["id"]] = r.get("nickname") or "Learner"

    active_players = list(active_map.values())
    total_players = max(len(active_map), 1 if uid else 0) + get_settings().DEMO_CROWD

    return {k: q[k] for k in ("id", "agentId", "title", "questions")} | {
        "startsIn": 5,
        "players": total_players,
        "activePlayers": active_players,
    }


@router.post("/live/submit")
async def live_submit(body: QuizIn, uid: str = Depends(get_uid)):
    u = users.get_user(uid)
    q = await current_quiz()
    if body.quizId and body.quizId != q["id"]:
        q = get_db().get(QUIZZES, body.quizId) or q
    users.enforce_limits(u)
    score = max(0, min(500, int(body.score)))
    db = get_db()
    coll = f"{QUIZZES}/{q['id']}/results"
    
    prev = db.get(coll, uid)
    first = prev is None
    prev_score = prev.get("score", 0) if prev else 0
    new_best = max(score, prev_score)
    db.put(coll, uid, {"id": uid, "score": new_best, "nickname": u["nickname"]})
    
    # Ensure presence is also kept active
    db.put(f"{QUIZZES}/{q['id']}/presence", uid, {"id": uid, "nickname": u["nickname"], "updatedAt": time.time()})
    
    all_results = db.query(coll)
    others = [r["score"] for r in all_results if r["id"] != uid] + _crowd_scores(q["id"])
    rank = 1 + sum(1 for s in others if s > score)
    xp = score if first else max(0, score - prev_score)
    u.setdefault("counts", {})["quizBest"] = max(u["counts"].get("quizBest", 0), new_best)
    users.record(u, "quiz", xp, extra={"postTitle": q["title"], "agentId": q["agentId"]})
    
    # Accurate total players (all who submitted + active presence)
    presences = db.query(f"{QUIZZES}/{q['id']}/presence")
    now = time.time()
    active_presences = [p for p in presences if p.get("updatedAt", 0) > (now - 600)]
    all_players = set([r.get("id") for r in all_results if r.get("id")] + [p.get("id") for p in active_presences if p.get("id")])
    total_players = max(len(all_players), len(others) + 1)
    
    return {"rank": rank, "players": total_players, "xpAwarded": xp}


# ---------- parent ----------
@router.get("/parent/summary")
async def parent_summary(uid: str = Depends(get_uid)):
    return await parent_svc.summary(users.get_user(uid))


@router.post("/parent/settings")
async def parent_settings(body: dict, uid: str = Depends(get_uid)):
    return await parent_svc.update_settings(users.get_user(uid), body)


@router.get("/levels")
async def levels():
    return [{"level": i + 1, "name": n, "xp": scoring.THRESHOLDS[i]} for i, n in enumerate(scoring.LEVELS)]
