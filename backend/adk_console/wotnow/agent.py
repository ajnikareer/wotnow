"""
ADK developer console for wotnow (local only, not deployed).

  cd backend
  set GOOGLE_API_KEY=<AI Studio key>      (or GOOGLE_GENAI_USE_VERTEXAI=TRUE + GOOGLE_CLOUD_PROJECT/LOCATION + gcloud ADC)
  adk web adk_console                      → http://localhost:8000, choose "wotnow"

A coordinator agent routes a question to one of the 8 expert agents. Each expert has tools that read
its reviewed fact cards (the same knowledge the app's content engine uses), and the same guardrail plugin.
Use it to chat with the experts, inspect every model/tool call in the Events tab, and demo the agent design.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))   # backend/ on the path

from google.adk.agents import LlmAgent  # noqa: E402
from google.adk.apps import App  # noqa: E402

from app.agents import config as cfg  # noqa: E402
from app.agents.guardrails import WotnowGuardrails  # noqa: E402
from app.engine import cards as C  # noqa: E402

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def _tools_for(expert_id: str):
    def list_fact_cards() -> list[dict]:
        """Lists this expert's reviewed fact cards (id, title, subtopic, class bands)."""
        return [{"id": c["id"], "title": c["title"], "subtopic": c.get("subtopic"), "bands": c["bands"]} for c in C.cards_for(expert_id)]

    def get_fact_card(card_id: str) -> dict:
        """Returns one fact card: facts, do's, don'ts and myths. Use it before answering any safety question."""
        c = C.card(card_id) if hasattr(C, "card") else None
        if not c or c.get("agentId") != expert_id:
            return {"error": f"no card {card_id} for this expert"}
        return {k: c.get(k) for k in ("id", "title", "facts", "do", "dont", "myths")}
    return [list_fact_cards, get_fact_card]


def _expert(a: dict) -> LlmAgent:
    return LlmAgent(
        name=f"{a['id']}_coach", model=MODEL,
        description=f"{a['name']}: {a['domainLabel']} expert for school students.",
        instruction=(f"You are {a['name']}, the wotnow {a['domainLabel']} expert. Persona: {a.get('persona', '')}\n"
                     "Answer students' questions in 2-5 short sentences. ALWAYS call list_fact_cards and get_fact_card first, "
                     "and only use what the cards say. If the cards don't cover it, say so and suggest asking a trusted adult. "
                     "Ask one follow-up question to check understanding."),
        tools=_tools_for(a["id"]),
    )


experts = [_expert(a) for a in C.agents()]
root_agent = LlmAgent(
    name="wotnow_coordinator", model=MODEL,
    description="Routes a student's question to the right wotnow expert.",
    instruction=("You are the wotnow coordinator. Greet the student briefly, then transfer to the expert whose domain fits: "
                 + ", ".join(f"{a['id']}_coach ({a['domainLabel']})" for a in C.agents())
                 + ". Do not answer safety questions yourself."),
    sub_agents=experts,
)
flags = {e.name: {"skill": "console", "pii_scrub": True, "guard_output": True} for e in experts}
flags[root_agent.name] = {"skill": "console", "pii_scrub": True, "guard_output": True}
app = App(name="wotnow", root_agent=root_agent, plugins=[WotnowGuardrails(flags)])
