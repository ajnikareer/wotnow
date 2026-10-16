"""
ADK runtime: runs one skill as an ADK invocation (Runner + InMemorySessionService + guardrail plugin)
and records a trace of every run (skill, agent, time, guardrail events, reviewer verdict).
Each run uses a fresh, short-lived session: agents never see another child's data.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
import uuid
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Optional

from google.adk.apps import App
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from ..engine import cards as C
from . import config as cfg
from .factory import AgentFactory
from .guardrails import WotnowGuardrails

log = logging.getLogger("wotnow.agents")
TRACES: deque = deque(maxlen=200)


@dataclass
class RunResult:
    output: Any = None
    ok: bool = False
    blocked: Optional[str] = None
    review: Optional[dict] = None
    trace: dict = field(default_factory=dict)


def _parse(v: Any) -> Any:
    if isinstance(v, str):
        s = v.strip()
        if s.startswith("```"):
            s = s.strip("`").removeprefix("json").strip()
        try:
            return json.loads(s)
        except Exception:
            return v
    if hasattr(v, "model_dump"):
        return v.model_dump()
    return v


class AgentRuntime:
    def __init__(self, model_override=None):
        self.app = cfg.registry()["app_name"]
        self.factory = AgentFactory(model_override)
        self.sessions = InMemorySessionService()
        self.plugin = WotnowGuardrails(self.factory.flags)   # shares the live flags dict
        self._runners: dict[int, Runner] = {}

    def _runner(self, agent) -> Runner:
        r = self._runners.get(id(agent))
        if r is None:
            app = App(name=self.app, root_agent=agent, plugins=[self.plugin])
            r = Runner(app=app, session_service=self.sessions)
            self._runners[id(agent)] = r
        return r

    @staticmethod
    def initial_state(meta: dict, spec: dict) -> dict:
        reg = cfg.registry()
        expert = C.agent(meta.get("agent_id") or "") or {}
        band = meta.get("band") or "all"
        return {
            "expert_name": expert.get("name", "the wotnow expert"),
            "expert_domain": expert.get("domainLabel", "life-skills"),
            "expert_persona": expert.get("persona", "Warm, practical and encouraging."),
            "audience": reg["audiences"].get(band, reg["audiences"]["all"]),
            "task": reg["tasks"].get(spec.get("task") or "", spec.get("description", "")),
            "draft": "",
        }

    async def run(self, skill: str, message: str, meta: Optional[dict] = None) -> RunResult:
        meta = meta or {}
        spec = cfg.skill(skill)
        agent, out_key, review_key = self.factory.get(skill, meta.get("agent_id"))
        runner = self._runner(agent)
        uid = "svc"
        sid = f"{skill}-{uuid.uuid4().hex[:12]}"
        t0 = time.perf_counter()
        trace = {"ts": time.time(), "skill": skill, "agent": agent.name, "expert": meta.get("agent_id"), "band": meta.get("band")}
        res = RunResult(trace=trace)
        await self.sessions.create_session(app_name=self.app, user_id=uid, session_id=sid, state=self.initial_state(meta, spec))
        try:
            msg = types.Content(role="user", parts=[types.Part(text=message)])

            async def _go():
                async for _ in runner.run_async(user_id=uid, session_id=sid, new_message=msg):
                    pass
            await asyncio.wait_for(_go(), timeout=float(spec.get("timeout_s", 60)))
            st = (await self.sessions.get_session(app_name=self.app, user_id=uid, session_id=sid)).state
            res.output = _parse(st.get(out_key))
            res.review = _parse(st.get(review_key)) if review_key else None
            res.blocked = st.get("guard_blocked")
            for k in ("guard_injection_suspected", "guard_pii_scrubbed", "guard_truncated", "guard_model_error"):
                if st.get(k):
                    trace[k.removeprefix("guard_")] = st[k]
            if res.review is not None and not (isinstance(res.review, dict) and res.review.get("approved")):
                res.blocked = res.blocked or "rejected by safety_reviewer: " + "; ".join((res.review or {}).get("issues", []) if isinstance(res.review, dict) else [])
            res.ok = res.output not in (None, "") and not res.blocked
            if spec.get("schema") and not isinstance(res.output, dict):
                res.ok, res.blocked = False, res.blocked or "output was not valid JSON for the schema"
        except Exception as exc:
            trace["error"] = f"{type(exc).__name__}: {str(exc)[:300]}"
            res.ok = False
            raise
        finally:
            trace.update(ms=round((time.perf_counter() - t0) * 1000), ok=res.ok, blocked=res.blocked,
                         review=res.review if review_key else None)
            TRACES.appendleft(trace)
            log.info("[adk] skill=%s agent=%s ok=%s ms=%s%s", skill, agent.name, res.ok, trace["ms"],
                     f" blocked={res.blocked}" if res.blocked else "")
            try:
                await self.sessions.delete_session(app_name=self.app, user_id=uid, session_id=sid)
            except Exception:
                pass
        return res
