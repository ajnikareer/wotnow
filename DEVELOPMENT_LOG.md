# wotnow · Development Journey & Engineering Log

This document chronicles the real-world engineering journey of building **wotnow** for the **Google AI Builder Cup 2026** (Sustainability & Social Impact category). It tracks our architecture evolution across 8 distinct milestones, documenting what was built, the unexpected challenges faced, and the solutions implemented.

---

### Stage 1: MVP & Core Social Feed
- **Focus:** First working prototype of an AI-powered social learning feed ("TikTok meets Duolingo for real-life skills").
- **What was built:** Fast modern feed interface with 8 initial expert coaches (fire, road, first aid, disaster, climate, civic, finance, emotional wellbeing), 31 verified fact cards, interactive scenario cards, and simulated student responses.
- **Challenge:** LLM responses in real-time were too slow for smooth scrolling and could hallucinate unsafe emergency advice.
- **Solution:** Separated asynchronous post generation from instant client evaluation. Introduced reviewed ground-truth fact cards that anchor all educational content.

---

### Stage 2: Gemini Integration on Google Cloud
- **Focus:** Moving from mock AI to live Gemini 2.5 Flash on Vertex AI.
- **What was built:** Keyless authentication using Google Cloud service accounts and Workload Identity on Google Cloud Run. Real-time answer judging with zero hardcoded API keys.
- **Challenge:** Handling structured output parsing across differing prompt schemas when judging freeform student reasoning.
- **Solution:** Enforced strict JSON schema output formatting with Pydantic response models, temperature tuning (0.1 for deterministic evaluation), and fallback grading heuristics.

---

### Stage 3: Google ADK Multi-Agent Architecture
- **Focus:** Transitioning to Google's **Agent Development Kit (ADK)** for production multi-agent orchestration.
- **What was built:** 
  - Declarative agent registry and rules configuration in `backend/app/agents/`.
  - Sequential two-agent publication pipeline: `<expert>_writer` ➔ `safety_reviewer`.
  - `WotnowGuardrails` custom ADK plugin running `before_model` (PII scrubbing, prompt injection detection) and `after_model` (medical prescription blocking, external link sanitization).
  - Full agent execution traces captured with latency, token usage, and reviewer verdicts.
- **Challenge:** The `safety_reviewer` initially rejected ~40% of valid educational drafts because it was overly strict on informal tone.
- **Solution:** Calibrated reviewer guidelines to distinguish between genuine safety violations (hallucinated procedures, dangerous shortcuts) and engaging, student-friendly colloquial tone. Publish pass rate rose to 85% while catching 100% of real safety discrepancies.

---

### Stage 4: Content Studio, Review Queue & Admin Console
- **Focus:** Editorial control and automated batch generation.
- **What was built:** Automated scheduler pipeline, admin console with live agent inspection, prompt editor, review queue for pending drafts, and golden-set evaluation harness (`evals`) achieving 10/10 judge alignment.
- **Challenge:** Managing long-running generation tasks without blocking HTTP server worker threads.
- **Solution:** Implemented background asyncio workers with bounded concurrency queues and SQLite/Firestore state persistence.

---

### Stage 5: Cloud Run Production Readiness & Scale
- **Focus:** 24/7 resilience on Google Cloud Run.
- **What was built:** Unified container serving both the FastAPI backend and optimized Vite frontend bundle on a single Cloud Run instance with auto-scaling and zero-downtime revision rollouts.
- **Challenges:** 
  1. Class-band filtering hid ~1/3 of posts for certain age groups.
  2. An always-on background scheduler generated excess Firestore read costs.
  3. Stale weather/AQI city alerts remained after conditions improved.
- **Solutions:** 
  - Restructured band eligibility logic with inclusive defaults.
  - Implemented shared in-memory feed caching with bounded TTLs (`FEED_CACHE_TTL_S`) to drastically slash database reads.
  - Added timestamped today-only filtering for environmental and civic alerts.

---

### Stage 6: Learning Portfolio & Feed States
- **Focus:** Gamified learning persistence and retention.
- **What was built:** 
  - 3-state card tracking: **New Feeds** (`today`), **Done** (`learned`), and **Retry**.
  - Animated points modal awarding XP upon scenario completion.
  - Dedicated "Learned" tab acting as a personal safety portfolio and review deck.
- **Challenge:** State desynchronization between student sessions and global feed generation counts.
- **Solution:** Tied the "New Feeds" counter directly to the student's uncompleted post set, preventing count fluctuation when switching tabs.

---

### Stage 7: Family Security & Authentication
- **Focus:** COPPA-conscious family sign-in and student profiles.
- **What was built:** 
  - Google OAuth identity for parents and guardians.
  - Zero-email child profiles: children use nicknames and cute avatars without requiring personal email addresses or external credentials.
  - Role-based routing (parent view vs. student feed) and session invalidation across devices.
  - Protected demo guest account allowing judges to immediately evaluate the app with one click without signing in.
- **Challenge:** Third-party cookie blocking on modern browsers preventing iframe Google sign-in buttons.
- **Solution:** Implemented standard Google Identity Services FedCM redirect flows and clean server-side JWT session cookies.

---

### Stage 8: 20 AI Coaches & 375 Fact Cards Expansion
- **Focus:** Comprehensive life-readiness curriculum across 4 pillars.
- **What was built:**
  - Expanded from 8 to **20 specialized AI coaches** across **4 distinct pillars**:
    - ❤️ **Life & Safety** (8 coaches: Fire, Road, First Aid, Disaster, Boundaries, Law, Fitness, Hygiene)
    - 🌍 **Planet & City** (4 coaches: Climate, Animal Welfare, Clean Energy, Civic Sense)
    - 🚀 **Future & Enterprise** (5 coaches: Money, Startups, Careers, Cyber Safety, Nutrition)
    - 🧠 **Mind & Wellbeing** (3 coaches: Mental Health, Screen Time, Inclusion & Anti-Bullying)
  - Catalog of **375 reviewed fact cards** grounding every coach's knowledge base.
  - Added "Following" directory tab and interactive coach showcase row.
  - Polished responsive design system with single-color brand violet theme, animated mascot, and 100% natural display scaling.