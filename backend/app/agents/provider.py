"""
AdkProvider: the app's LLM interface implemented with ADK agents.

Existing callers (content engine, judge, moderation, alerts, quiz, parent tips, expert replies) are unchanged:
they call generate_json(system, prompt, schema). The provider maps the schema to a SKILL (registry.json),
works out which expert and audience the call is for, and runs the matching ADK agent / workflow.
The `system` text from the caller is only used to detect expert + audience. Instructions come from
agents/instructions/*.md and the global policy from rules.json.
"""
from __future__ import annotations

import logging
import os
import re
from typing import Optional

from ..ai.llm import GeminiProvider, LLMProvider
from ..config import get_settings
from ..engine import cards as C
from . import config as cfg

log = logging.getLogger("wotnow.agents")

_EXPERT = re.compile(r"You are (\w+), (?:an AI|a friendly AI)")
_BANDS = [("Classes 3-5", "junior"), ("Classes 6-8", "middle"), ("Classes 9-12", "senior"),
          ("young (8-10", "junior"), ("middle-school", "middle"), ("high-school", "senior")]


def derive_meta(system: str) -> dict:
    meta: dict = {}
    m = _EXPERT.search(system or "")
    if m:
        a = next((x for x in C.agents() if x["name"].lower() == m.group(1).lower()), None)
        if a:
            meta["agent_id"] = a["id"]
    for needle, band in _BANDS:
        if needle in (system or ""):
            meta["band"] = band
            break
    return meta


def _configure_genai_env() -> None:
    """ADK's Gemini client reads these environment variables."""
    s = get_settings()
    if s.use_vertex:
        os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "TRUE")
        os.environ.setdefault("GOOGLE_CLOUD_PROJECT", s.GOOGLE_CLOUD_PROJECT)
        os.environ.setdefault("GOOGLE_CLOUD_LOCATION", s.GOOGLE_CLOUD_LOCATION)
    elif s.GEMINI_API_KEY:
        os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")
        os.environ.setdefault("GOOGLE_API_KEY", s.GEMINI_API_KEY)


class AdkProvider(LLMProvider):
    name = "adk"

    def __init__(self, runtime=None, direct: Optional[LLMProvider] = None):
        _configure_genai_env()
        self.direct = direct if direct is not None else GeminiProvider()
        if runtime is None:
            from .runtime import AgentRuntime
            runtime = AgentRuntime()
        self.runtime = runtime
        self.fallback_direct = os.getenv("ADK_FALLBACK_DIRECT", "true").lower() == "true"
        self.available = bool(getattr(self.direct, "available", False)) or os.getenv("ADK_FORCE_AVAILABLE") == "1"

    async def _run(self, skill: str, prompt: str, system: str, meta: Optional[dict]):
        m = {**derive_meta(system), **(meta or {})}
        res = await self.runtime.run(skill, prompt, m)
        if res.blocked:
            log.warning("[adk] %s blocked: %s", skill, res.blocked)
            return None
        return res.output if res.ok else None

    async def generate_json(self, system, prompt, schema, temperature=0.4, skill=None, meta=None, **kw):
        skill = skill or cfg.registry()["schema_to_skill"].get(getattr(schema, "__name__", ""))
        if not skill:
            return await self.direct.generate_json(system, prompt, schema, temperature)
        try:
            return await self._run(skill, prompt, system, meta)
        except Exception as exc:
            log.warning("[adk] %s failed: %s", skill, exc)
            return await self.direct.generate_json(system, prompt, schema, temperature) if self.fallback_direct else None

    async def generate_text(self, system, prompt, temperature=0.4, skill=None, meta=None, **kw):
        skill = skill or ("expert_reply" if "replying to a student" in (system or "") else None)
        if not skill:
            return await self.direct.generate_text(system, prompt, temperature)
        try:
            out = await self._run(skill, prompt, system, meta)
            return out.strip() if isinstance(out, str) and out.strip() else None
        except Exception as exc:
            log.warning("[adk] %s failed: %s", skill, exc)
            return await self.direct.generate_text(system, prompt, temperature) if self.fallback_direct else None

    async def embed(self, text):
        return await self.direct.embed(text)
