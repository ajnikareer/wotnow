"""
Scheduled / admin jobs (Cloud Scheduler sends header X-Jobs-Token).
  POST /jobs/generate        new posts from every agent (content engine)
  POST /jobs/local-alerts    Terra alert for every city that has students
  POST /jobs/live-quiz       next live quiz
  POST /jobs/preview         generate WITHOUT publishing (great for the demo: shows combo, validation, dedupe)
  POST /jobs/seed            (re)seed demo content and users
"""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends

from ..auth import require_jobs_token
from ..engine import cards as C
from ..engine.generator import generate_one
from ..engine.local_alerts import build_alert
from ..engine.quiz import build_quiz
from ..services.users import USERS
from ..store.base import get_db

router = APIRouter(prefix="/jobs", dependencies=[Depends(require_jobs_token)])


@router.post("/generate")
async def generate(agent: Optional[str] = None, count: int = 1, kind: Optional[str] = None):
    ids = [agent] if agent else [a["id"] for a in C.agents()]
    report = []
    for a in ids:
        for _ in range(max(1, min(count, 5))):
            r = await generate_one(a, kind=kind)
            report.append({"agent": a, "ok": r["ok"], "postId": r.get("post", {}).get("id"), "type": r.get("post", {}).get("type"),
                           "attempts": r["attempts"]})
    return {"created": sum(1 for r in report if r["ok"]), "report": report}


@router.post("/preview")
async def preview(agent: str = "ember", kind: Optional[str] = None, band: Optional[str] = None):
    r = await generate_one(agent, kind=kind, band=band, publish=False)
    return r


@router.post("/local-alerts")
async def local_alerts():
    cities = sorted({(u.get("city") or "Pune") for u in get_db().query(USERS)}) or ["Pune"]
    out = []
    for c in cities:
        p = await build_alert(c)
        out.append({"city": c, "postId": p["id"], "source": p.get("source")})
    return {"alerts": out}


@router.post("/live-quiz")
async def live_quiz(agent: Optional[str] = None):
    q = await build_quiz(agent)
    return {"id": q["id"], "title": q["title"], "questions": len(q["questions"])}


@router.post("/seed")
async def seed(reset: bool = False):
    from ..seed import seed_all
    return await seed_all(force=True)
