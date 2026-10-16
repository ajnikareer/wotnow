"""Loads the declarative agent configuration (registry.json, rules.json, instructions/*.md)."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent


@lru_cache
def registry() -> dict:
    return json.loads((HERE / "registry.json").read_text(encoding="utf-8"))


@lru_cache
def rules() -> dict:
    return json.loads((HERE / "rules.json").read_text(encoding="utf-8"))


@lru_cache
def instruction(name: str) -> str:
    return (HERE / "instructions" / name).read_text(encoding="utf-8").strip()


def skill(name: str) -> dict:
    s = registry()["skills"].get(name)
    if s is None:
        raise KeyError(f"unknown skill '{name}'")
    return {**registry()["defaults"], **s}


def policy_text() -> str:
    r = rules()
    return r["policy_header"] + ":\n- " + "\n- ".join(r["policy"])
