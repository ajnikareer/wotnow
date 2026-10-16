"""
LLM port. Every AI call in the app goes through get_llm().

  AGENT_RUNTIME=adk    (default when LLM_PROVIDER=gemini) → app/agents: Google ADK agents with
                       managed skills, instructions, safety-review workflow and guardrail plugin.
  AGENT_RUNTIME=direct → v1 behaviour: direct google-genai calls (still used by ADK as a fallback, and for embeddings).
  LLM_PROVIDER=mock    → no model at all; every caller uses its deterministic fallback.

Gemini is reached on Gemini Enterprise Agent Platform (formerly Vertex AI) with the Cloud Run service
account (no key) when GOOGLE_CLOUD_PROJECT is set, otherwise with GEMINI_API_KEY.
Callers may pass skill=... and meta={...}; providers that don't need them ignore them.
"""
from __future__ import annotations

import json
import logging
import os
from typing import Optional, Type

from pydantic import BaseModel

from ..config import get_settings

log = logging.getLogger("wotnow.llm")


class LLMProvider:
    name = "base"
    available = False

    async def generate_json(self, system: str, prompt: str, schema: Type[BaseModel], temperature: float = 0.4, **kw) -> Optional[dict]:
        return None

    async def generate_text(self, system: str, prompt: str, temperature: float = 0.4, **kw) -> Optional[str]:
        return None

    async def embed(self, text: str) -> Optional[list[float]]:
        return None


class MockProvider(LLMProvider):
    name = "mock"


class GeminiProvider(LLMProvider):
    """Direct google-genai calls (v1 path)."""
    name = "gemini"

    def __init__(self) -> None:
        s = get_settings()
        self.model, self.embed_model = s.GEMINI_MODEL, s.EMBED_MODEL
        self.client = None
        try:
            from google import genai  # type: ignore
            from google.genai import types  # type: ignore
            self.types = types
            if s.use_vertex:
                self.client = genai.Client(vertexai=True, project=s.GOOGLE_CLOUD_PROJECT, location=s.GOOGLE_CLOUD_LOCATION)
            elif s.GEMINI_API_KEY:
                self.client = genai.Client(api_key=s.GEMINI_API_KEY)
            else:
                log.warning("[gemini] no GOOGLE_CLOUD_PROJECT or GEMINI_API_KEY -> fallback mode")
        except Exception as exc:
            log.warning("[gemini] SDK unavailable -> fallback mode: %s", exc)
        self.available = self.client is not None

    async def generate_json(self, system, prompt, schema, temperature=0.4, **kw):
        if not self.client:
            return None
        try:
            r = await self.client.aio.models.generate_content(
                model=self.model, contents=prompt,
                config=self.types.GenerateContentConfig(
                    system_instruction=system, temperature=temperature,
                    response_mime_type="application/json", response_schema=schema))
            return json.loads(r.text)
        except Exception as exc:
            log.warning("[gemini] generate_json failed: %s", exc)
            return None

    async def generate_text(self, system, prompt, temperature=0.4, **kw):
        if not self.client:
            return None
        try:
            r = await self.client.aio.models.generate_content(
                model=self.model, contents=prompt,
                config=self.types.GenerateContentConfig(system_instruction=system, temperature=temperature))
            return (r.text or "").strip() or None
        except Exception as exc:
            log.warning("[gemini] generate_text failed: %s", exc)
            return None

    async def embed(self, text):
        if not self.client:
            return None
        try:
            r = await self.client.aio.models.embed_content(model=self.embed_model, contents=[text])
            return list(r.embeddings[0].values)
        except Exception as exc:
            log.warning("[gemini] embed failed (falling back to trigram dedupe): %s", exc)
            return None


_PROVIDER: Optional[LLMProvider] = None


def agent_runtime_name() -> str:
    if get_settings().LLM_PROVIDER != "gemini":
        return "mock"
    return os.getenv("AGENT_RUNTIME", "adk").lower()


def get_llm() -> LLMProvider:
    global _PROVIDER
    if _PROVIDER is None:
        rt = agent_runtime_name()
        if rt == "mock":
            _PROVIDER = MockProvider()
        elif rt == "adk":
            try:
                from ..agents.provider import AdkProvider
                _PROVIDER = AdkProvider()
            except Exception as exc:
                log.error("[adk] could not start ADK runtime, using direct Gemini: %s", exc)
                _PROVIDER = GeminiProvider()
        else:
            _PROVIDER = GeminiProvider()
    return _PROVIDER


def reset_llm() -> None:
    global _PROVIDER
    _PROVIDER = None
