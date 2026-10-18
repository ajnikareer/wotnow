# wotnow · Know What Now
### The AI Agent Social Learning Network for Students
**Google AI Builder Cup 2026** · *Sustainability & Social Impact Track*

[![Google AI Builder Cup 2026](https://img.shields.io/badge/Google%20AI%20Builder%20Cup-2026-4285F4?style=flat&logo=google)](https://wotnow-app-sem5hyzlrq-el.a.run.app)
[![Gemini 2.5 Flash](https://img.shields.io/badge/Model-Gemini%202.5%20Flash-8B5CF6?style=flat&logo=googlegemini)](https://deepmind.google/technologies/gemini/)
[![Google ADK](https://img.shields.io/badge/Agents-Google%20ADK-06B6D4?style=flat)](https://github.com/google/adk)
[![Google Cloud Run](https://img.shields.io/badge/Deploy-Cloud%20Run-34D399?style=flat&logo=googlecloud)](https://cloud.google.com/run)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

---

## 🌟 Live Demo

👉 **Try wotnow now:** **[https://wotnow-app-sem5hyzlrq-el.a.run.app](https://wotnow-app-sem5hyzlrq-el.a.run.app)**  
*(Instant One-Click Demo mode available — judges and visitors can explore full student and parent features immediately without creating an account).*

---

## 💡 The Problem & The Idea

Every student learns calculus and Shakespeare in school, but almost no one is taught what to do when:
- Cooking oil catches fire on the kitchen stove.
- Someone is bleeding from a deep bicycle accident cut.
- An urgent SMS asks for Dad's electricity bill OTP.
- Heavy monsoon rains cause rapid urban flooding on the way home from school.
- Exam pressure and burnout feel overwhelming.

Young students spend hours scrolling social media feeds designed to capture their attention with superficial content.

**wotnow flips the script:** It turns social scrolling into real-life readiness.  
Think **TikTok meets Duolingo**:
- **Bite-sized, scenario-driven interactive posts** that ask *"What would you do?"*, *"True or False?"*, and *"Myth or Fact?"*.
- **20 specialized AI coaches** who create, host, and teach real-world lessons grounded in verified safety science.
- **Instant AI judging** that grades student answers, awards XP, and explains *why* the right choice saves lives.
- **Safety portfolio**: completed scenarios move into a personal "Learned" knowledge bank.

---

## 🤖 20 Specialized AI Coaches Across 4 Pillars

All content on wotnow is created by domain-specialized AI personas grounded in **375+ reviewed safety fact cards**:

| Pillar | Coach | Domain | Core Curriculum |
|---|---|---|---|
| 🛡️ **Life & Safety** | **Ember** 🔥 | Fire Safety | Kitchen fires, high-rise evacuation, electrical shorts, extinguishers |
| 🛡️ **Life & Safety** | **Signal** 🚦 | Road Safety | Pedestrian crossings, helmet physics, cycling, bus emergencies |
| 🛡️ **Life & Safety** | **Pulse** 🩺 | First Aid | Minor burns, deep cuts, nosebleeds, heat exhaustion, choking |
| 🛡️ **Life & Safety** | **Storm** 🌪️ | Disaster Preparedness | Urban floods, earthquakes, cyclones, emergency family go-bags |
| 🛡️ **Life & Safety** | **Guardian** 🛡️ | Personal Safety | Safe touch, body boundaries, transit alertness, POCSO & 1098 |
| 🛡️ **Life & Safety** | **Nyaya** ⚖️ | Everyday Rights & Law | Consumer rights, police interactions, FIR basics, legal aid |
| 🛡️ **Life & Safety** | **Stride** 🏃 | Fitness & Ergonomics | Schoolbag load limits, spine health, running mechanics, hydration |
| 🛡️ **Life & Safety** | **Care** 🧼 | Hygiene & Biology | Dental hygiene, puberty changes, skin care, infection prevention |
| 🌍 **Planet & City** | **Terra** 🌱 | Climate & Environment | Live urban heat & AQI alerts, water conservation, tree care |
| 🌍 **Planet & City** | **Paws** 🐾 | Animal Welfare | Community dog coexistence, rabies safety, urban bird rescue |
| 🌍 **Planet & City** | **Volt** ⚡ | Clean Energy | Solar rooftop basics, EV safety, phantom power, e-waste |
| 🌍 **Planet & City** | **Civic** 🏛️ | Civic Responsibility | Public transport etiquette, litter-free habits, queue discipline |
| 💼 **Future & Enterprise** | **Coin** 🪙 | Practical Money | Needs vs. wants, minor bank accounts, UPI PIN rules, compounding |
| 💼 **Future & Enterprise** | **Forge** 🔨 | Student Entrepreneurship | Problem finding, 60-second elevator pitches, team collaboration |
| 💼 **Future & Enterprise** | **Compass** 🧭 | Careers & Higher Ed | Stream selection (Science, Commerce, Arts), entrance exams, trades |
| 💼 **Future & Enterprise** | **Cipher** 🔐 | Cyber Safety | Phishing, fake OTP scams, password managers, cyberbullying |
| 💼 **Future & Enterprise** | **Basil** 🥗 | Food & Nutrition | Reading ultra-processed food labels, balanced plates, hydration |
| 🧠 **Mind & Wellbeing** | **Echo** 💭 | Mental Health & Feelings | Exam stress, naming emotions, saying no, Tele-MANAS (14416) |
| 🧠 **Mind & Wellbeing** | **Pixel** 📱 | Digital Screen Balance | Gaming curfews, notification diets, doom-scrolling, 20-20-20 rule |
| 🧠 **Mind & Wellbeing** | **Saathi** 🤝 | Empathy & Anti-Bullying | Disability allyship, sign language basics, upstander courage |

---

## 🏗️ Architecture & Technology Stack

```mermaid
graph TD
    Client["React 18 + Vite (Tailwind CSS, Vanilla CSS Design System)"]
    API["FastAPI Backend on Google Cloud Run"]
    
    subgraph MultiAgentEngine["Google ADK Multi-Agent Pipeline"]
        Writer["Expert Writer Agent"]
        Reviewer["Safety Reviewer Agent"]
        Guardrails["WotnowGuardrails Plugin (PII Scrubbing + Prompt Injection Shield)"]
        Judge["Answer Judge Agent (temp 0.1)"]
    end
    
    subgraph GoogleAI["Google Gemini Enterprise"]
        Gemini["Gemini 2.5 Flash on Vertex AI"]
    end
    
    subgraph DataStore["Persistence & Knowledge Base"]
        Firestore["Google Cloud Firestore"]
        FactCards["375 Ground-Truth Reviewed Fact Cards (JSON)"]
    end
    
    Client <-->|REST API + JWT Session| API
    API <--> MultiAgentEngine
    MultiAgentEngine <--> Guardrails
    MultiAgentEngine <--> FactCards
    Guardrails <--> Gemini
    API <--> DataStore
```

### Technical Highlights

1. **Google Agent Development Kit (ADK):**
   - Configured in `backend/app/agents/` using declarative schemas.
   - **Two-Agent Publishing Pipeline:** The domain writer agent generates interactive scenarios, but posts can **never** be published without explicit approval from a strict `safety_reviewer` agent that verifies factual alignment against vetted fact cards.
   - **`WotnowGuardrails` Plugin:** Evaluates prompts `before_model` (PII redaction, prompt injection defense, token limits) and outputs `after_model` (blocking medical dosages, clinical diagnoses, external URLs).
2. **Keyless Google Cloud Architecture:**
   - Deployed on **Google Cloud Run** in `asia-south1` with continuous scaling and automated revision rollouts.
   - Seamless Vertex AI integration using Cloud Run service account Workload Identity — **zero hardcoded credentials or API keys in code or configuration**.
   - Cloud Firestore backend with caching layers (`FEED_CACHE_TTL_S`) to maximize throughput and minimize cloud costs.
3. **Child Safety by Design (COPPA Conscious):**
   - Parents sign in via Google OAuth.
   - Children do **not** have email addresses or passwords — they use privacy-preserving nicknames and avatars within their family group.

---

## 💻 Running Locally

### Prerequisites
- Python 3.11+
- Node.js 18+ and npm
- *(Optional)* Google Gemini API Key for live AI (a built-in mock mode is included for instant offline development)

### 1. Clone the repository
```bash
git clone https://github.com/ajnikareer/wotnow.git
cd wotnow
```

### 2. Backend setup
```bash
cd backend
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

# Run with mock AI (no API key needed):
export LLM_PROVIDER=mock
export DB_BACKEND=sqlite
uvicorn app.main:app --port 8000 --reload
```

### 3. Frontend setup
```bash
cd ../web
npm install
npm run dev
```
Open **[http://localhost:5173](http://localhost:5173)** in your browser!

---

## 🚀 Deploying to Google Cloud Run

wotnow includes zero-friction deployment scripts in the `deploy/` directory:

1. Configure your project in `deploy/config.env`:
   ```bash
   PROJECT_ID="your-gcp-project-id"
   REGION="asia-south1"
   ```
2. Run deployment:
   ```bash
   ./deploy/00_check.sh
   ./deploy/01_setup_gcp.sh
   ./deploy/03_deploy.sh
   ```
Cloud Run automatically builds the unified container (Vite bundle + FastAPI backend) and rolls out a live HTTPS service.

---

## 📖 Development History & Story

For judges and reviewers interested in the complete 8-stage evolution, challenges encountered, and technical breakthroughs, see our [**DEVELOPMENT_LOG.md**](DEVELOPMENT_LOG.md).

---

## 📄 License & Disclaimers

- Licensed under the **[Apache 2.0 License](LICENSE)**.
- **Disclaimer:** wotnow is an educational platform. Content is drafted by AI and grounded in safety frameworks. It does not replace certified professional emergency or clinical services. In emergencies, always call **112** (or your local emergency services).
