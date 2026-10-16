"""
Builds ADK agents from registry.json + the expert personas in content/agents.json (both with admin edits applied).

- Writer skills become a 2-agent workflow per expert: SequentialAgent[ <expert>_writer → safety_reviewer ]
- Other skills become a single LlmAgent with an output_schema (structured JSON) or plain text.
Agents are built lazily and cached; the cache is dropped automatically when an admin changes any agent setting.
"""
from __future__ import annotations

import warnings
from typing import Optional

from google.adk.agents import LlmAgent, SequentialAgent
from google.genai import types
from pydantic import BaseModel, Field

from ..ai import schemas as S
from ..config import get_settings
from ..core import overrides
from ..engine import cards as C
from . import config as cfg


class ReviewOut(BaseModel):
    approved: bool = Field(description="true only if every check passes")
    issues: list[str] = Field(description="Each problem found, briefly. Empty if approved.")


SCHEMAS = {name: getattr(S, name) for name in ("ScenarioDraft", "PollDraft", "MythDraft", "ScamDraft", "JudgeOut",
                                               "ModerationOut", "AlertDraft", "QuizDraft", "StartersOut")}
SCHEMAS["ReviewOut"] = ReviewOut


def model_for(spec: dict, override=None):
    if override is not None:          # tests inject a fake model here
        return override
    m = spec.get("model", "default")
    return get_settings().GEMINI_MODEL if m == "default" else m


def _llm_agent(name: str, spec: dict, *, output_key: str, model_override=None) -> LlmAgent:
    schema = SCHEMAS.get(spec["schema"]) if spec.get("schema") else None
    kwargs = dict(
        name=name,
        model=model_for(spec, model_override),
        description=spec.get("description", ""),
        instruction=cfg.instruction(spec["instruction"]),
        generate_content_config=types.GenerateContentConfig(temperature=float(spec.get("temperature", 0.4))),
        output_key=output_key,
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
    )
    if schema is not None:
        kwargs["output_schema"] = schema
    return LlmAgent(**kwargs)


class AgentFactory:
    def __init__(self, model_override=None):
        self.model_override = model_override
        self._cache: dict[str, object] = {}
        self.flags: dict[str, dict] = {}       # agent name -> guardrail flags (read by the plugin)
        self._ver: Optional[str] = None
        self.generation = 0                    # bumps whenever agents are rebuilt (the runtime drops its runners)

    def _sync(self) -> None:
        v = cfg.config_version()
        if v != self._ver:
            self._cache.clear()
            self._ver = v
            self.generation += 1

    def _flag(self, name: str, skill: str, spec: dict) -> None:
        self.flags[name] = {"skill": skill, "pii_scrub": bool(spec.get("pii_scrub")), "guard_output": bool(spec.get("guard_output"))}

    def get(self, skill: str, expert_id: Optional[str] = None):
        """Returns (agent, output_key, review_key_or_None)."""
        self._sync()
        spec = cfg.skill(skill)
        expert_id = expert_id if spec.get("per_expert") else None
        if spec.get("per_expert") and (not expert_id or not C.agent(expert_id)):
            expert_id = "ember"
        key = f"{skill}:{expert_id or '-'}"
        if key in self._cache:
            return self._cache[key]
        prefix = f"{expert_id}_" if expert_id else ""
        name = f"{prefix}{spec['agent']}" + (f"_{spec['task']}" if spec.get("task") else "")
        out_key = "draft" if spec.get("review") else "output"
        agent = _llm_agent(name, spec, output_key=out_key, model_override=self.model_override)
        self._flag(name, skill, spec)
        review_key = None
        if spec.get("review"):
            rspec = cfg.skill("review_post")
            rname = f"{name}_reviewer"
            reviewer = _llm_agent(rname, rspec, output_key="review", model_override=self.model_override)
            self._flag(rname, "review_post", rspec)
            with warnings.catch_warnings():   # ADK 2.x: SequentialAgent still supported; Workflow is the graph successor
                warnings.simplefilter("ignore", DeprecationWarning)
                agent = SequentialAgent(name=f"{name}_studio", description=f"Write → safety review workflow for {skill}",
                                        sub_agents=[agent, reviewer])
            review_key = "review"
        self._cache[key] = (agent, out_key, review_key)
        return self._cache[key]

    def catalogue(self) -> list[dict]:
        """Every skill with its effective settings, file defaults and which settings an admin has overridden."""
        reg, dreg = cfg.registry(), cfg.default_registry()
        out = []
        for sk, s in reg["skills"].items():
            eff = {**reg["defaults"], **s}
            dflt = {**dreg["defaults"], **dreg["skills"][sk]}
            changed = [k for k in cfg.SKILL_PARAMS if eff.get(k) != dflt.get(k)]
            ifile = eff["instruction"]
            out.append({"skill": sk, "agent": eff["agent"], "perExpert": bool(eff.get("per_expert")), "description": eff.get("description", ""),
                        "schema": eff.get("schema"), "temperature": eff.get("temperature"), "timeoutS": eff.get("timeout_s"),
                        "reviewedBy": "safety_reviewer" if eff.get("review") else None, "hasReviewOption": "review" in dreg["skills"][sk],
                        "guardrails": {"policy": True, "piiScrub": bool(eff.get("pii_scrub")), "outputScan": bool(eff.get("guard_output"))},
                        "defaults": {k: dflt.get(k) for k in cfg.SKILL_PARAMS if k in dflt},
                        "overridden": changed, "instructionFile": ifile, "instruction": cfg.instruction(ifile),
                        "instructionOverridden": overrides.get(f"instr:{ifile}") is not None})
        return out
