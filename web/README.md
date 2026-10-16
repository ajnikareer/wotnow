# wotnow · Web app (frontend)

The safe social feed for students (Classes 3–12): AI experts post real-life scenarios, students respond, and AI scores them.
React 18 + Vite + TypeScript + Tailwind CSS. Light/dark mode. Mobile-first and responsive. Fonts are bundled locally (no Google Fonts call).

## Run (no backend needed)
```bash
cd web
npm install
npm run dev          # http://localhost:5173  (also on your LAN IP for phone testing)
```
By default the app runs in **mock mode**: every screen works with sample data stored in your browser.
Scenario answers are scored by a keyword stand-in for Gemini (live mode uses the real backend).

### Demo paths
| URL | What |
|---|---|
| `#/` | Landing page (judges start here) |
| `#/start` | Parent-led signup → child profile → pick experts |
| `#/feed` | Feed: local alert, scenarios, polls, myth or fact, scam or legit |
| `#/post/oil-fire` | Answer a scenario → mascot "thinking" → AI feedback card |
| `#/live` | Live fastest-finger quiz (5 questions) |
| `#/leaderboard` | Class / school / city, with class-vs-class teams |
| `#/me` | Profile, skills, badges, **theme switch** (Light / Dark / Auto) |
| `#/parent` | Parent dashboard: time limit, weekly activity, dinner-table talking points, controls |

Use **Profile → Reset demo data** to start fresh.

## Live mode (with backend)
```bash
cp .env.example .env        # set VITE_API_MODE=live
npm run dev                 # /api is proxied to http://localhost:8080
```
API contract: `src/lib/types.ts` + `src/lib/api.ts` (the backend must follow these shapes).

## Build & deploy
```bash
npm run build               # → dist/
npm run typecheck           # optional strict type check
```
`dist/` is static. Deploy to Firebase Hosting with a rewrite of `/api/**` to the Cloud Run service (infra bundle).

## Structure
```
src/
  main.tsx, App.tsx           entry + hash routes
  index.css                   theme tokens (light/dark CSS variables) + component classes
  lib/   api · types · router · theme · session · toast · hooks · env
  mocks/ data.ts (experts, posts, answer keys) · mockApi.ts (in-browser fake backend)
  components/ Brand (Logo, Mascot moods) · AppShell · PostCard · ui · Icon
  pages/ Landing · Start · Feed · PostDetail · Experts · ExpertProfile · Leaderboard · Profile · Parent · LiveQuiz
```

## Design notes
- Brand: outline speech-bubble logo with eyes, and a bubble mascot with 4 moods (think, look, happy, wow).
- Theme follows the device by default; the choice is saved in `localStorage` (`wn_theme`) and applied before first paint.
- Kids are shown only as nicknames + emoji avatars. No DMs, no user posts.
- Safety content in `mocks/data.ts` follows widely published guidance but must be reviewed before launch.
