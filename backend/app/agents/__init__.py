"""
wotnow AI agents, built on Google's Agent Development Kit (ADK).

Everything that decides how the AI behaves lives here as configuration, not scattered code:
  registry.json        skills → agents, schemas, temperatures, review step, guardrail flags
  instructions/*.md    each agent's instructions (with {state} placeholders)
  rules.json           global child-safety policy, blocked patterns, PII patterns
  guardrails.py        ADK plugin that enforces rules.json on EVERY agent call
  factory.py           builds ADK LlmAgents / SequentialAgents from the registry + expert personas
  runtime.py           ADK Runner + session service; runs a skill and records a trace
  provider.py          plugs the runtime into the app (same interface as the old direct Gemini calls)
  api.py               /api/ai/agents (catalogue) and /api/ai/traces (recent agent runs)
"""
