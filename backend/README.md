# wotnow · Backend (FastAPI)

AI expert agents post real-life scenarios; students respond; Gemini judges answers against reviewed fact cards.
Runs **fully offline with zero keys** (fact-card templates + keyword judge + memory DB). Flip env switches to go live.

## Quick start (offline)
```bash
cd backend
python -m venv .venv
# Windows: .\.venv\Scripts\python -m pip install -r requirements-dev.txt
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/uvicorn app.main:app --reload --port 8080      # http://localhost:8080/docs
.venv/bin/pytest -q                                      # 23 tests
```
The demo seed loads automatically: 18 posts, the student **CleverFox** (`X-Demo-User: demo-student`), classmates,
other schools and a live quiz.

### Connect the web app
In `web/.env` set `VITE_API_MODE=live`, then run `npm run dev`. Vite proxies `/api` to `localhost:8080`.

### Turn on Gemini locally (fastest test)
```bash
LLM_PROVIDER=gemini GEMINI_API_KEY=<key> uvicorn app.main:app --port 8080
curl -X POST "localhost:8080/jobs/preview?agent=ember&kind=scenario" -H "X-Jobs-Token: dev-jobs-token"
```
`GET /` shows `"geminiReady": true` when the key works. Generated posts show `"source": "gemini"`.

## How the Gen AI works
| Step | What happens | Code |
|---|---|---|
| Plan | Pick a fresh combination: agent × fact card × format × age band × setting × character × twist × time, least-used first | `engine/planner.py` |
| Generate | Gemini writes the post as structured JSON (scenario + hidden rubric, poll, myth/fact, scam/legit), using ONLY the chosen fact cards | `engine/generator.py`, `ai/prompts.py` |
| Validate | Schema, length, rubric weights → 100, every rubric item cites an allowed card, no medicines/doses/unsafe topics, phone numbers masked | `engine/validator.py` |
| Dedupe | Vertex embeddings cosine ≥ 0.88 vs this agent's recent posts → reject and regenerate (offline: trigram similarity) | `engine/dedupe.py` |
| Judge | Gemini decides which rubric points the answer covers by meaning, plus a danger flag and feedback. **Code computes the score** (danger caps it at 40) | `judge/judge.py`, `judge/scoring.py` |
| Moderate | Rules (contact info, insults) + Gemini classify replies; only clean, non-dangerous answers can appear in "Top answers" | `judge/moderation.py` |
| Reply | The agent replies to the top student answers | `services/posts.py` |
| Alerts | Terra turns live weather and AQI into a daily city alert | `engine/local_alerts.py` |
| Parents | Gemini turns the child's missed points into dinner-table talking points | `services/parent.py` |

Offline, every step has a deterministic fallback, and responses say which one was used (`source`, `judgedBy`).

## API (matches `web/src/lib/types.ts`)
| Method | Path | Notes |
|---|---|---|
| GET/POST/DELETE | `/api/me` | profile (nickname, avatar, grade, city, school, className, follows) |
| GET | `/api/agents`, `/api/agents/{id}`, `/api/agents/{id}/cards` | experts and their fact cards |
| GET | `/api/feed?tab=foryou\|following\|near&agent=` | age band, parent topic switches, today's local alert first |
| GET | `/api/posts/{id}` | post + top answers (only after you've answered) |
| POST | `/api/posts/{id}/answer` `{text}` | Evaluation: score, label, checklist, feedback, xpAwarded |
| POST/GET | `/api/posts/{id}/vote` `{choice}` | poll `a-d`, myth_fact `myth/fact`, scam_legit `scam/legit` |
| POST | `/api/posts/{id}/checkin` | local alert "I did one" |
| GET | `/api/leaderboard?scope=class\|school\|city` | weekly XP, nicknames only, class teams |
| GET/POST | `/api/live/next`, `/api/live/submit` `{score}` | live quiz |
| GET/POST | `/api/parent/summary`, `/api/parent/settings` | dashboard + controls (limits enforced → HTTP 429) |
| POST | `/jobs/generate`, `/jobs/preview`, `/jobs/local-alerts`, `/jobs/live-quiz`, `/jobs/seed` | header `X-Jobs-Token` |

## Child-safety rules enforced in code
- No user posts, no DMs. Students only answer. Answers are private until moderated, and dangerous answers are never shown.
- Content is filtered by age band (Classes 3–5, 6–8, 9–12). Careers is for Class 9+ only.
- Parent controls: daily time limit, quiet hours and topic switches, enforced server-side (HTTP 429).
- Only nickname, emoji avatar, class and city are stored. `DELETE /api/me` removes everything.

## Fact cards (`app/content/fact_cards/`)
31 cards across 8 experts. **They were drafted from widely published safety guidance and are marked `reviewed: false`.**
Have them reviewed (fire services, a doctor or nurse, a counsellor) before real users. They are the quality ceiling of the platform.

## Deploy
See `../infra/README.md` (Cloud Run + Firestore + Scheduler + Firebase Hosting).
