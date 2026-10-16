"""
Loads the declarative agent configuration: files shipped in the image (registry.json, rules.json, instructions/*.md)
with admin edits layered on top (core/overrides: 'skill:<name>', 'instr:<file>', 'rules').

Everything here is cached per overrides version, so an admin change reaches the agents within seconds.
"""
from __future__ import annotations

import copy
import json
import threading
from functools import lru_cache
from pathlib import Path

from ..core import overrides

HERE = Path(__file__).resolve().parent
SKILL_PARAMS = ("temperature", "review", "guard_output", "pii_scrub", "timeout_s")
RULE_KEYS = ("policy", "allowed_numbers", "blocked_output_patterns", "pii_patterns", "injection_markers", "max_input_chars")
INSTRUCTION_PLACEHOLDERS = ("expert_name", "expert_domain", "expert_persona", "audience", "task", "draft")


# ---------------- file defaults ----------------
@lru_cache
def default_registry() -> dict:
    return json.loads((HERE / "registry.json").read_text(encoding="utf-8"))


@lru_cache
def default_rules() -> dict:
    return json.loads((HERE / "rules.json").read_text(encoding="utf-8"))


@lru_cache
def default_instruction(name: str) -> str:
    return (HERE / "instructions" / name).read_text(encoding="utf-8").strip()


def instruction_files() -> list[str]:
    return sorted(p.name for p in (HERE / "instructions").glob("*.md"))


# ---------------- effective (defaults + admin edits) ----------------
_lock = threading.RLock()
_cache: dict = {"ver": None, "registry": None, "rules": None}


def config_version() -> str:
    return overrides.version()


def _rebuild() -> None:
    ver = overrides.version()
    with _lock:
        if _cache["ver"] == ver:
            return
        reg = copy.deepcopy(default_registry())
        for name, spec in reg["skills"].items():
            ov = overrides.get(f"skill:{name}") or {}
            for k in SKILL_PARAMS:
                if k in ov:
                    spec[k] = ov[k]
        rules = copy.deepcopy(default_rules())
        rov = overrides.get("rules") or {}
        for k in RULE_KEYS:
            if k in rov:
                rules[k] = rov[k]
        _cache.update(ver=ver, registry=reg, rules=rules)


def registry() -> dict:
    _rebuild()
    return _cache["registry"]


def rules() -> dict:
    _rebuild()
    return _cache["rules"]


def instruction(name: str) -> str:
    ov = overrides.get(f"instr:{name}")
    if isinstance(ov, dict) and (ov.get("text") or "").strip():
        return ov["text"].strip()
    return default_instruction(name)


def skill(name: str) -> dict:
    s = registry()["skills"].get(name)
    if s is None:
        raise KeyError(f"unknown skill '{name}'")
    return {**registry()["defaults"], **s}


def policy_text() -> str:
    r = rules()
    return r["policy_header"] + ":\n- " + "\n- ".join(r["policy"])
