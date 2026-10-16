"""
WotnowGuardrails: an ADK plugin applied to EVERY agent the runtime runs.

before_model  · appends the global safety policy (rules.json) to the system instruction
              · scrubs phone numbers / emails / handles from student text for agents with pii_scrub
              · flags prompt-injection attempts in student text (recorded in the trace)
              · truncates oversized input
after_model   · scans generated text for blocked patterns (medicine, unsuitable topics, links)
                on agents with guard_output; a hit marks the run as blocked (the caller then falls back)
on_model_error· records the error for the trace
"""
from __future__ import annotations

import logging
import re
from typing import Optional

from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.plugins.base_plugin import BasePlugin
from google.genai import types

from . import config as cfg

log = logging.getLogger("wotnow.guardrails")


class WotnowGuardrails(BasePlugin):
    def __init__(self, agent_flags: dict[str, dict]):
        """agent_flags: agent name -> {"pii_scrub": bool, "guard_output": bool, "skill": str}"""
        super().__init__(name="wotnow_guardrails")
        r = cfg.rules()
        self.flags = agent_flags
        self.policy = cfg.policy_text()
        self.max_chars = int(r.get("max_input_chars", 12000))
        self.blocked = {k: re.compile(v, re.I) for k, v in r["blocked_output_patterns"].items()}
        self.pii = {k: re.compile(v) for k, v in r["pii_patterns"].items()}
        self.injection = [m.lower() for m in r.get("injection_markers", [])]

    # ---------- helpers ----------
    @staticmethod
    def _append_system(llm_request: LlmRequest, text: str) -> None:
        cfg_ = llm_request.config
        if cfg_ is None:
            llm_request.config = cfg_ = types.GenerateContentConfig()
        si = cfg_.system_instruction
        if si is None:
            cfg_.system_instruction = text
        elif isinstance(si, str):
            cfg_.system_instruction = si + "\n\n" + text
        elif isinstance(si, types.Content):
            si.parts = (si.parts or []) + [types.Part(text=text)]
        else:  # list of parts / strings
            cfg_.system_instruction = list(si) + [text]

    def _flags(self, ctx: CallbackContext) -> dict:
        return self.flags.get(ctx.agent_name, {})

    # ---------- callbacks ----------
    async def before_model_callback(self, *, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        flags = self._flags(callback_context)
        self._append_system(llm_request, self.policy)
        total = 0
        for content in llm_request.contents or []:
            if content.role != "user":
                continue
            for part in content.parts or []:
                if not part.text:
                    continue
                low = part.text.lower()
                if any(m in low for m in self.injection):
                    callback_context.state["guard_injection_suspected"] = True
                if flags.get("pii_scrub"):
                    t = part.text
                    for kind, rx in self.pii.items():
                        t = rx.sub(f"[{kind} removed]", t)
                    if t != part.text:
                        callback_context.state["guard_pii_scrubbed"] = True
                        part.text = t
                total += len(part.text)
                if total > self.max_chars:
                    part.text = part.text[: max(0, len(part.text) - (total - self.max_chars))]
                    callback_context.state["guard_truncated"] = True
        return None

    async def after_model_callback(self, *, callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
        flags = self._flags(callback_context)
        if not flags.get("guard_output") or not llm_response.content:
            return None
        text = " ".join(p.text for p in (llm_response.content.parts or []) if getattr(p, "text", None))
        for kind, rx in self.blocked.items():
            m = rx.search(text)
            if m:
                reason = f"{callback_context.agent_name}: blocked {kind} ('{m.group(0)}')"
                callback_context.state["guard_blocked"] = reason
                log.warning("[guardrails] %s", reason)
                break
        return None

    async def on_model_error_callback(self, *, callback_context: CallbackContext, llm_request: LlmRequest, error: Exception) -> Optional[LlmResponse]:
        callback_context.state["guard_model_error"] = f"{type(error).__name__}: {str(error)[:200]}"
        return None
