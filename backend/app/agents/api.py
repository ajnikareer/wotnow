"""Agent transparency endpoints (great for the demo and for debugging)."""
from __future__ import annotations

from fastapi import APIRouter, Depends

from ..ai.llm import agent_runtime_name, get_llm
from ..auth import require_jobs_token
from ..engine import cards as C
from . import config as cfg

router = APIRouter(prefix="/api/ai", tags=["agents"])


@router.get("/agents")
async def agents_catalogue():
    """Which ADK agents exist, what each skill does, and which guardrails apply. Public, no student data."""
    from .factory import AgentFactory
    return {"runtime": agent_runtime_name(), "provider": get_llm().name,
            "framework": "Google Agent Development Kit (ADK)", "model": cfg.registry()["defaults"]["model"],
            "experts": [{"id": a["id"], "name": a["name"], "domain": a["domainLabel"], "persona": a.get("persona", ""),
                         "factCards": len(C.cards_for(a["id"]))} for a in C.agents()],
            "skills": AgentFactory().catalogue(),
            "guardrails": {"policy": cfg.rules()["policy"], "allowedNumbers": cfg.rules()["allowed_numbers"],
                           "blockedOutput": list(cfg.rules()["blocked_output_patterns"]), "piiScrubbed": list(cfg.rules()["pii_patterns"])}}


@router.get("/traces", dependencies=[Depends(require_jobs_token)])
async def agent_traces(limit: int = 50):
    """Most recent agent runs (skill, agent, latency, guardrail events, reviewer verdict). Needs X-Jobs-Token."""
    try:
        from .runtime import TRACES
    except Exception:
        return {"traces": []}
    return {"traces": list(TRACES)[: max(1, min(limit, 200))]}
