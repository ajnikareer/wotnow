"""
Agents + reviewed fact cards (app/content), with admin edits layered on top (core/overrides, keys 'card:<ID>').
Cards are the ONLY source of truth agents may teach from.

Admin edits: title, facts, do, dont, reviewed, disabled. Disabled cards are never used for generation.
When the pipeline setting 'reviewed_only' is on, only cards marked reviewed are used for new content.
"""
from __future__ import annotations

import copy
import json
import threading
from functools import lru_cache

from ..config import get_settings
from ..core import overrides

BANDS = ("junior", "middle", "senior")
EDITABLE_LISTS = ("facts", "do", "dont")
EDITABLE_FIELDS = ("title", "reviewed", "disabled", "reviewedBy", "reviewedAt", "reviewNote")


@lru_cache
def agents() -> list[dict]:
    return json.loads((get_settings().CONTENT_DIR / "agents.json").read_text(encoding="utf-8"))


def agent(agent_id: str) -> dict | None:
    return next((a for a in agents() if a["id"] == agent_id), None)


def agent_by_domain(domain: str) -> dict | None:
    return next((a for a in agents() if a["domain"] == domain), None)


@lru_cache
def _base_cards() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((get_settings().CONTENT_DIR / "fact_cards").glob("*.json")):
        for c in json.loads(f.read_text(encoding="utf-8"))["cards"]:
            out[c["id"]] = c
    return out


_lock = threading.RLock()
_eff: tuple[str, dict[str, dict]] = ("", {})


def _effective() -> dict[str, dict]:
    global _eff
    ver = overrides.version()
    with _lock:
        if _eff[0] == ver and _eff[1]:
            return _eff[1]
        out = {}
        for cid, base in _base_cards().items():
            c = copy.deepcopy(base)
            ov = overrides.get(f"card:{cid}") or {}
            for k in EDITABLE_LISTS:
                if isinstance(ov.get(k), list):
                    c[k] = [str(x) for x in ov[k]]
            for k in EDITABLE_FIELDS:
                if k in ov:
                    c[k] = ov[k]
            c["edited"] = bool(ov)
            out[cid] = c
        _eff = (ver, out)
        return out


def reviewed_only() -> bool:
    return bool((overrides.get("pipeline") or {}).get("reviewed_only", False))


def _usable(c: dict) -> bool:
    return not c.get("disabled") and (c.get("reviewed", False) or not reviewed_only())


def all_cards() -> list[dict]:
    """Cards agents may use for new content (excludes disabled; honours reviewed-only mode)."""
    return [c for c in _effective().values() if _usable(c)]


def all_cards_admin() -> list[dict]:
    """Every card with its effective (edited) values, for the admin UI."""
    return list(_effective().values())


def card(card_id: str) -> dict | None:
    return _effective().get(card_id)


def base_card(card_id: str) -> dict | None:
    return _base_cards().get(card_id)


def cards_for(agent_id: str, band: str | None = None) -> list[dict]:
    return [c for c in _effective().values() if c["agentId"] == agent_id and _usable(c) and (band is None or band in c["bands"])]


@lru_cache
def combos() -> dict:
    return json.loads((get_settings().CONTENT_DIR / "combos.json").read_text(encoding="utf-8"))


def band_for_grade(grade: int) -> str:
    return "junior" if grade <= 5 else "middle" if grade <= 8 else "senior"


def source_cards(ids: list[str]) -> list[dict]:
    return [{"id": i, "title": card(i)["title"]} for i in ids if card(i)]
