"""Agents + reviewed fact cards (app/content). Cards are the ONLY source of truth agents may teach from."""
from __future__ import annotations

import json
from functools import lru_cache

from ..config import get_settings

BANDS = ("junior", "middle", "senior")


@lru_cache
def agents() -> list[dict]:
    return json.loads((get_settings().CONTENT_DIR / "agents.json").read_text(encoding="utf-8"))


def agent(agent_id: str) -> dict | None:
    return next((a for a in agents() if a["id"] == agent_id), None)


def agent_by_domain(domain: str) -> dict | None:
    return next((a for a in agents() if a["domain"] == domain), None)


@lru_cache
def _cards() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((get_settings().CONTENT_DIR / "fact_cards").glob("*.json")):
        for c in json.loads(f.read_text(encoding="utf-8"))["cards"]:
            out[c["id"]] = c
    return out


def all_cards() -> list[dict]:
    return list(_cards().values())


def card(card_id: str) -> dict | None:
    return _cards().get(card_id)


def cards_for(agent_id: str, band: str | None = None) -> list[dict]:
    return [c for c in _cards().values() if c["agentId"] == agent_id and (band is None or band in c["bands"])]


@lru_cache
def combos() -> dict:
    return json.loads((get_settings().CONTENT_DIR / "combos.json").read_text(encoding="utf-8"))


def band_for_grade(grade: int) -> str:
    return "junior" if grade <= 5 else "middle" if grade <= 8 else "senior"


def source_cards(ids: list[str]) -> list[dict]:
    return [{"id": i, "title": card(i)["title"]} for i in ids if card(i)]
