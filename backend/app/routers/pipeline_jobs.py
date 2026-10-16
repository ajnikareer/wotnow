"""POST /jobs/tick: lets Cloud Scheduler (or curl/cron) run one pipeline pass. Token protected."""
from __future__ import annotations

from fastapi import APIRouter, Depends

from ..auth import require_jobs_token
from ..pipeline import scheduler

router = APIRouter(prefix="/jobs", tags=["jobs"], dependencies=[Depends(require_jobs_token)])


@router.post("/tick")
async def tick():
    return await scheduler.tick(source="scheduler")
