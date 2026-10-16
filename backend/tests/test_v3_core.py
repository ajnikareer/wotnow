"""Admin-editable overrides: cards, agent settings, instructions, guardrails (live reload, no redeploy)."""
import asyncio
import json
import os

import pytest

from app.core import overrides


def test_overrides_versioning_history_and_delete():
    v0 = overrides.version()
    overrides.put("pipeline", {"paused": True}, "alice")
    v1 = overrides.version()
    assert v1 != v0 and overrides.get("pipeline") == {"paused": True}
    assert overrides.meta("pipeline")["version"] == 1 and overrides.meta("pipeline")["updatedBy"] == "alice"
    overrides.put("pipeline", {"paused": False}, "bob")
    assert [h["version"] for h in overrides.history("pipeline")] == [2, 1]
    assert overrides.delete("pipeline", "bob") is True and overrides.get("pipeline") is None
    assert overrides.delete("pipeline", "bob") is False
    assert overrides.history("pipeline")[0].get("deleted") is True
    assert overrides.all_keys() == []


def test_overrides_never_break_when_database_fails(monkeypatch):
    from app.store import base
    monkeypatch.setattr(base, "get_db", lambda: (_ for _ in ()).throw(RuntimeError("db down")))
    monkeypatch.setattr(overrides, "get_db", lambda: (_ for _ in ()).throw(RuntimeError("db down")))
    overrides.invalidate()
    assert overrides.get("rules") is None            # falls back to file defaults instead of raising


def test_card_overrides_reviewed_only_and_disable():
    from app.engine import cards as C
    base = C.base_card("FIRE-012")
    assert C.card("FIRE-012")["facts"] == base["facts"] and not C.card("FIRE-012")["edited"]
    overrides.put("card:FIRE-012", {"facts": ["New verified fact."], "title": "Edited title"}, "admin")
    c = C.card("FIRE-012")
    assert c["facts"] == ["New verified fact."] and c["title"] == "Edited title" and c["edited"] and c["do"] == base["do"]
    assert C.base_card("FIRE-012")["facts"] == base["facts"]               # shipped card untouched
    assert "FIRE-012" in [x["id"] for x in C.cards_for("ember")]

    overrides.put("pipeline", {"reviewed_only": True}, "admin")             # none are reviewed yet
    assert C.reviewed_only() and C.cards_for("ember") == [] and C.all_cards() == []
    assert C.card("FIRE-012") is not None                                   # still readable (e.g. for old posts)
    overrides.put("card:FIRE-012", {"reviewed": True, "reviewedBy": "admin"}, "admin")
    assert [x["id"] for x in C.cards_for("ember")] == ["FIRE-012"]
    overrides.put("card:FIRE-012", {"reviewed": True, "disabled": True}, "admin")
    assert C.cards_for("ember") == [] and len(C.all_cards_admin()) >= 8


def test_agent_registry_rules_and_instruction_overrides():
    from app.agents import config as cfg
    assert cfg.skill("judge")["temperature"] == 0.1
    overrides.put("skill:judge", {"temperature": 0.3, "pii_scrub": False}, "admin")
    assert cfg.skill("judge")["temperature"] == 0.3 and cfg.skill("judge")["pii_scrub"] is False
    assert cfg.default_registry()["skills"]["judge"]["temperature"] == 0.1

    assert "Answer Judge" in cfg.instruction("judge.md")
    overrides.put("instr:judge.md", {"text": "You are the wotnow Answer Judge, now stricter. {audience}"}, "admin")
    assert "now stricter" in cfg.instruction("judge.md")
    overrides.delete("instr:judge.md", "admin")
    assert "now stricter" not in cfg.instruction("judge.md")

    overrides.put("rules", {"allowed_numbers": ["112"], "injection_markers": ["hack"]}, "admin")
    assert cfg.rules()["allowed_numbers"] == ["112"] and "wotnow GLOBAL SAFETY POLICY" in cfg.policy_text()
    assert cfg.rules()["policy"] == cfg.default_rules()["policy"]


def test_factory_rebuilds_agents_after_admin_change():
    from app.agents.factory import AgentFactory
    f = AgentFactory()
    a1, _, _ = f.get("judge")
    g1 = f.generation
    assert f.get("judge")[0] is a1 and f.generation == g1                  # cached
    overrides.put("instr:judge.md", {"text": "You are the wotnow Answer Judge, edited. Audience: {audience}"}, "admin")
    a2, _, _ = f.get("judge")
    assert a2 is not a1 and f.generation == g1 + 1 and "edited" in a2.instruction
    overrides.put("skill:judge", {"temperature": 0.5}, "admin")
    assert f.get("judge")[0].generate_content_config.temperature == 0.5
    cat = {c["skill"]: c for c in f.catalogue()}
    assert cat["judge"]["overridden"] == ["temperature"] and cat["judge"]["instructionOverridden"] is True
    assert cat["write_scenario"]["hasReviewOption"] is True and cat["judge"]["hasReviewOption"] is False


def test_guardrail_plugin_picks_up_rule_changes_live():
    from app.agents import config as cfg
    from app.agents.guardrails import WotnowGuardrails
    g = WotnowGuardrails({})
    assert g.blocked["link"].search("see http://x.y") and "112" in g.policy
    overrides.put("rules", {"blocked_output_patterns": {"swear": "\\bdarn\\b"}, "policy": ["Be kind.", "Only teach safety."]}, "admin")
    g._refresh()
    assert list(g.blocked) == ["swear"] and g.blocked["swear"].search("Darn it") and "Be kind." in g.policy
    overrides.delete("rules", "admin")
    g._refresh()
    assert "link" in g.blocked


def test_runtime_persists_traces_and_rebuilds_runners():
    from app.agents.runtime import AgentRuntime
    from app.store.base import get_db
    from tests.test_adk_agents import FakeGemini
    m = FakeGemini(); m.calls = []
    rt = AgentRuntime(model_override=m)
    r = asyncio.run(rt.run("moderate", "REPLY: <<<hello>>>", {}))
    assert r.ok and r.output["label"] == "ok"
    stored = get_db().query("agent_traces")
    assert len(stored) == 1 and stored[0]["skill"] == "moderate" and stored[0]["ok"] is True and "ms" in stored[0]
    n_runners = len(rt._runners)
    overrides.put("skill:moderate", {"temperature": 0.2}, "admin")
    asyncio.run(rt.run("moderate", "REPLY: <<<again>>>", {}))
    assert len(rt._runners) == 1 and n_runners == 1                         # old runner dropped when agents were rebuilt
    assert len(get_db().query("agent_traces")) == 2
