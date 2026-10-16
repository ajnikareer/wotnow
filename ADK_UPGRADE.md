# wotnow · ADK upgrade (v2 agents)

This delta moves every Gemini call in wotnow onto **Google's Agent Development Kit (ADK)**, the agent framework of
**Gemini Enterprise Agent Platform** (formerly Vertex AI). Skills, instructions, the safety-review workflow and
guardrails are now **managed as configuration** in `backend/app/agents/`, not scattered through the code.

The website, API endpoints, database, XP rules and "code computes the score" are **unchanged**.

---

## 1. What changed

| Before (v1) | Now (v2, ADK) |
|---|---|
| Prompts in `ai/prompts.py`, called with direct `google-genai` | 11 **skills** in `agents/registry.json`, run as **ADK agents** (`LlmAgent`, `SequentialAgent`, `Runner`, `App`) |
| One model call writes a post | **Two-agent workflow**: `<expert>_writer` → `safety_reviewer`. The reviewer checks the draft against the fact cards and safety rules; rejected drafts are never published |
| Safety rules repeated in prompts | **Global policy** in `agents/rules.json`, injected into **every** agent by an **ADK plugin** (`WotnowGuardrails`) |
| Regex checks only after generation | Plugin `before_model`: policy, **PII scrubbing** of student text, **prompt-injection flagging**, input size limit. Plugin `after_model`: blocks medicine, unsuitable topics and links in generated text |
| No visibility into AI calls | **Trace** of every agent run (skill, agent, latency, guardrail events, reviewer verdict) at `/api/ai/traces` |
| — | **Agent catalogue** at `/api/ai/agents`: experts, skills, instructions, guardrails (great for judges) |
| — | **Golden-set evaluation** for the judge agent (`agents/evals`) |
| — | **ADK dev console** (`adk web`): chat with a coordinator that hands off to 8 expert agents using fact-card **tools** |

### Agent map
```
Content studio (per expert × format)     Single agents
┌──────────────────────────────────┐     answer_judge     (JudgeOut, temp 0.1, PII scrub)
│ ember_expert_writer_scenario     │     moderator        (ModerationOut, temp 0)
│        │ output_key=draft        │     <expert>_expert_replier (text, PII scrub, output scan)
│        ▼                         │     terra_alerts     (AlertDraft, output scan)
│ ember_..._reviewer (ReviewOut)   │     <expert>_quiz_host (QuizDraft, output scan)
└──────────────────────────────────┘     parent_coach     (StartersOut, output scan)
        all agents ── WotnowGuardrails plugin (rules.json) ── Gemini 2.5 Flash on Agent Platform
```

### Files in this delta
```
ADK_UPGRADE.md                          this guide
backend/requirements.txt                + google-adk==2.12.0
backend/app/ai/llm.py                   routes AI calls to ADK (AGENT_RUNTIME=adk) · direct Gemini kept as fallback
backend/app/main.py                     + /api/ai routes, runtime shown in /api/info
backend/app/agents/                     NEW: ADK agents
  registry.json  rules.json  instructions/*.md   ← managed behaviour (edit these, not Python)
  config.py  factory.py  runtime.py  guardrails.py  provider.py  api.py
  evals/judge_cases.json  evals/run_judge_eval.py
backend/adk_console/wotnow/agent.py     NEW: ADK dev console (local only)
backend/tests/test_adk_agents.py        NEW: 7 offline tests (fake model, real ADK wiring)
deploy/03_deploy.sh                     + AGENT_RUNTIME, GOOGLE_GENAI_USE_VERTEXAI
deploy/05_smoke_test.sh                 + ADK checks (runtime, catalogue, traces)
```
Your `deploy/config.env` is **not** overwritten. `AGENT_RUNTIME` defaults to `adk`.

---

## 2. Apply it (new branch)
```powershell
cd C:\dev\wotnow
git checkout -b adk-agents
```
Put `wotnow_adk_delta_bundle.html` next to the `wotnow` folder (its parent), then extract **only this bundle**:
```powershell
cd C:\dev
@'
import json, re, pathlib
src = pathlib.Path.cwd()
b = src / "wotnow_adk_delta_bundle.html"
out = src / "wotnow"
m = re.search(r'<script id="vv-data" type="application/json">\s*(.*?)\s*</script>', b.read_text(encoding="utf-8"), re.S)
files = json.loads(m.group(1))
for rel, content in files.items():
    p = out / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
print(f"Done: {len(files)} files extracted to {out}")
'@ | python -
```
Then:
```powershell
cd C:\dev\wotnow
git status            # shows the modified + new files
git add . ; git commit -m "Move AI layer to Google ADK agents"
```

## 3. Test locally
```powershell
cd C:\dev\wotnow\backend
.\.venv\Scripts\python -m pip install -r requirements-dev.txt     # installs google-adk
.\.venv\Scripts\python -m pytest -q                               # all v1 tests + 7 new ADK tests
```
With a real model (AI Studio key, quickest):
```powershell
$env:LLM_PROVIDER="gemini"; $env:AGENT_RUNTIME="adk"
$env:GEMINI_API_KEY="<YOUR_AI_STUDIO_KEY>"; $env:EMBED_MODEL="gemini-embedding-001"
.\.venv\Scripts\python -m uvicorn app.main:app --port 8080
curl.exe -s http://localhost:8080/api/info                         # "agentRuntime":"adk", "provider":"adk", "geminiReady":true
curl.exe -s -X POST "http://localhost:8080/jobs/preview?agent=ember&kind=scenario" -H "X-Jobs-Token: dev-jobs-token"
curl.exe -s http://localhost:8080/api/ai/traces -H "X-Jobs-Token: dev-jobs-token"
```
In the traces you should see `write_scenario | ember_expert_writer_scenario_studio | ok` with `review.approved: true`.

### Judge evaluation (golden set)
```powershell
.\.venv\Scripts\python -m app.agents.evals.run_judge_eval
```
Prints each case, rubric precision and recall, and danger accuracy. Use it before and after changing `judge.md`.

### ADK dev console (optional, great for the demo video)
```powershell
$env:GOOGLE_API_KEY="<YOUR_AI_STUDIO_KEY>"
.\.venv\Scripts\adk web adk_console          # http://localhost:8000 → choose "wotnow"
```
Ask “What do I do if oil catches fire?”. The coordinator hands off to `ember_coach`, which calls `list_fact_cards` / `get_fact_card`.
The **Events** tab shows every model call, tool call and transfer.

## 4. Deploy
Same steps as before, in Cloud Shell (upload the new code or `git pull`):
```bash
cd ~/wotnow/deploy && sed -i 's/\r$//' *.sh && chmod +x *.sh
./03_deploy.sh        # sets AGENT_RUNTIME=adk and GOOGLE_GENAI_USE_VERTEXAI=TRUE
./05_smoke_test.sh    # now also checks the ADK runtime, agent catalogue and traces
```
No new GCP permissions are needed: ADK uses the same Agent Platform (Vertex AI) model through the same `wotnow-run`
service account (`roles/aiplatform.user`).

## 5. How to change agent behaviour (no Python needed)
| Want to… | Edit |
|---|---|
| Change how an agent writes or judges | `backend/app/agents/instructions/<skill>.md` |
| Change temperature, add or remove the review step, toggle PII scrub or output scan | `backend/app/agents/registry.json` |
| Change global safety rules, allowed numbers, blocked words | `backend/app/agents/rules.json` |
| Change an expert's persona | `backend/app/content/agents.json` |
| Teach new facts | `backend/app/content/fact_cards/*.json` |

## 6. Rollback
Set `AGENT_RUNTIME="direct"` (in `deploy/config.env` or the environment) and redeploy. The app goes back to v1's direct Gemini calls.
If the ADK runtime fails at startup or on a call, the app falls back to direct Gemini automatically (`ADK_FALLBACK_DIRECT=true`),
and from there to the rule-based fallbacks, so the demo never breaks.

## 7. Notes
- ADK is pinned to `2.12.0`. `SequentialAgent` is still supported but marked deprecated in favour of ADK's new graph `Workflow`;
  moving to `Workflow` is a later step.
- Instructions use ADK **session state** placeholders (`{expert_name}`, `{audience}`, `{task}`, `{draft}`), filled per run.
- Every run uses a fresh, short-lived session, so agents never see another child's data.
