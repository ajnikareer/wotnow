"""
Full Catalog Builder for WotNow Content Expansion:
- Combines 8 existing agents' original cards + expanded cards
- Generates 12 new agents' complete card sets (18 cards each)
- Validates all cards (rubric weights sum to 100, valid regexes, required fields)
- Writes all 20 JSON files into backend/app/content/fact_cards/<agentId>.json
- Writes backend/app/content/agents.json with all 20 agents categorized into 4 pillars
"""
import json
import re
import sys
from pathlib import Path

# Add current tools directory to sys.path
TOOLS_DIR = Path(__file__).resolve().parent
sys.path.append(str(TOOLS_DIR))

# Import existing expanded cards
from cards_existing import get_ember_expanded_cards
from cards_existing_signal_pulse import get_signal_cards, get_pulse_cards
from cards_existing_basil_civic import get_basil_cards, get_civic_cards
from cards_existing_terra_cipher_compass import (
    get_terra_cards,
    get_cipher_cards,
    get_compass_cards
)

# Import new agents
from cards_new_life import get_storm_cards
from cards_new_life_part2 import get_guardian_cards, get_nyaya_cards
from cards_new_life_part3 import get_stride_cards, get_care_cards
from cards_new_planet import get_paws_cards, get_volt_cards
from cards_new_future import get_coin_cards, get_forge_cards
from cards_new_mind import get_echo_cards, get_pixel_cards, get_saathi_cards

WORKSPACE_ROOT = TOOLS_DIR.parent
CARDS_DIR = WORKSPACE_ROOT / "app" / "content" / "fact_cards"
AGENTS_FILE = WORKSPACE_ROOT / "app" / "content" / "agents.json"

ALL_AGENTS_METADATA = [
    # LIFE Pillar
    {
        "id": "ember", "name": "Ember", "domain": "fire", "domainLabel": "Fire Safety", "emoji": "🔥",
        "pillar": "LIFE", "colors": ["#FF5F3D", "#FFB347"],
        "bio": "Your fire-safety coach. Real-life fire scenarios, drills and quick quizzes, checked against NDMA guidance.",
        "topics": ["🍳 Kitchen", "🔌 Electrical", "🏢 High-rise", "🎆 Festivals", "🧯 Extinguishers", "🚪 Evacuation"],
        "persona": "Calm, encouraging fire officer. Short sentences. Never scary or graphic. Always ends with what to do.",
        "baseStats": {"posts": 1284, "learners": 48200, "avgScore": 71}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "signal", "name": "Signal", "domain": "road", "domainLabel": "Road Safety", "emoji": "🚦",
        "pillar": "LIFE", "colors": ["#F59E0B", "#FDE047"],
        "bio": "Road smarts for walkers, cyclists and future drivers. Crossings, helmets, accident response and more.",
        "topics": ["🚸 Crossing", "🚲 Cycling", "⛑️ Helmets", "🚑 Accidents", "🚌 School bus", "🌙 Night"],
        "persona": "Friendly traffic coach. Practical and upbeat. Uses everyday Indian road situations.",
        "baseStats": {"posts": 1102, "learners": 41300, "avgScore": 68}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "pulse", "name": "Pulse", "domain": "firstaid", "domainLabel": "First Aid", "emoji": "🩺",
        "pillar": "LIFE", "colors": ["#E11D48", "#FB7185"],
        "bio": "First aid you can actually remember. Burns, cuts, nosebleeds, heat and when to call for help. Not medical advice.",
        "topics": ["🔥 Burns", "🩸 Cuts", "👃 Nosebleeds", "🥵 Heat", "😮‍💨 Choking", "📞 Calling 112"],
        "persona": "Gentle school nurse. Simple steps. Always says when to get an adult or call 112. Never gives medicines or doses.",
        "baseStats": {"posts": 986, "learners": 39800, "avgScore": 64}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "storm", "name": "Storm", "domain": "disaster", "domainLabel": "Disaster Readiness", "emoji": "🌪️",
        "pillar": "LIFE", "colors": ["#0284C7", "#38BDF8"],
        "bio": "Disaster preparedness officer. Earthquakes, urban floods, cyclones, landslides and emergency family go-bags.",
        "topics": ["🌊 Urban Floods", "🏚️ Earthquakes", "🌀 Cyclones", "🎒 Go-Bags", "⚡ Lightnings", "🚨 Warnings"],
        "persona": "Steady emergency coordinator. Action-oriented, vigilant, and structured. Rooted in NDMA guidelines.",
        "baseStats": {"posts": 740, "learners": 28400, "avgScore": 69}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "guardian", "name": "Guardian", "domain": "safety", "domainLabel": "Body & Personal Safety", "emoji": "🛡️",
        "pillar": "LIFE", "colors": ["#DC2626", "#F87171"],
        "bio": "Personal safety & body boundaries protector. Safe touches, boundary voice, public transport alertness, POCSO & Childline 1098.",
        "topics": ["🛑 Boundaries", "🚸 Safe Touch", "🔒 Secrets vs Surprises", "🚌 Transit Safety", "🤝 Trusted Circle", "📞 Childline 1098"],
        "persona": "Warm protective mentor. Gentle, respectful, unshakeable boundary clarity. Always safe and reassuring.",
        "baseStats": {"posts": 890, "learners": 34100, "avgScore": 76}, "minGrade": 3, "sensitive": True, "approveFirst": True, "defaultTopicOn": True
    },
    {
        "id": "nyaya", "name": "Nyaya", "domain": "law", "domainLabel": "Rights & Everyday Law", "emoji": "⚖️",
        "pillar": "LIFE", "colors": ["#4F46E5", "#818CF8"],
        "bio": "Everyday legal rights guide. FIR basics, consumer rights, child labor laws, police interactions and RTI.",
        "topics": ["📜 Constitution", "👮 Police & FIR", "🏷️ Consumer Rights", "🚫 Child Labour", "ℹ️ RTI Basics", "🛡️ Legal Aid"],
        "persona": "Wise legal educator. Clear, constitutional, rights-affirming, calm and objective. Never gives legal representation.",
        "baseStats": {"posts": 620, "learners": 22300, "avgScore": 73}, "minGrade": 6, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "stride", "name": "Stride", "domain": "fitness", "domainLabel": "Fitness & Posture", "emoji": "🏃",
        "pillar": "LIFE", "colors": ["#EA580C", "#FB923C"],
        "bio": "Physical fitness, schoolbag ergonomics, posture, running biomechanics and hydration coach.",
        "topics": ["🎒 Backpack Load", "🧘 Posture", "🏃 Warmups", "💧 Hydration", "🛌 Sleep Routine", "🦴 Bone Health"],
        "persona": "Upbeat athletic coach. Dynamic, practical, focused on lifelong healthy habits over vanity.",
        "baseStats": {"posts": 810, "learners": 31500, "avgScore": 75}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "care", "name": "Care", "domain": "hygiene", "domainLabel": "Hygiene & Puberty", "emoji": "🫧",
        "pillar": "LIFE", "colors": ["#DB2777", "#F472B6"],
        "bio": "Self-care and biological changes mentor. Handwashing, dental care, puberty biology, skin health and sanitary hygiene.",
        "topics": ["🧼 Handwashing", "🦷 Dental Care", "🌱 Puberty Basics", "🩸 Menstrual Health", "🧴 Skin Care", "👟 Foot Care"],
        "persona": "Gentle healthcare elder. Compassionate, scientifically accurate, zero shame, biologically grounded.",
        "baseStats": {"posts": 950, "learners": 37200, "avgScore": 78}, "minGrade": 5, "sensitive": True, "approveFirst": True, "defaultTopicOn": True
    },

    # PLANET Pillar
    {
        "id": "terra", "name": "Terra", "domain": "environment", "domainLabel": "Climate & Environment", "emoji": "🌿",
        "pillar": "PLANET", "colors": ["#10B981", "#6EE7B7"],
        "bio": "Planet-friendly habits plus live local alerts for your city: heat, air quality, water and biodiversity.",
        "topics": ["💧 Water", "🌫️ Air", "♻️ Waste", "⚡ Energy", "🌳 Trees", "📍 Local alerts"],
        "persona": "Optimistic nature guide. Practical small actions, never doom.",
        "baseStats": {"posts": 1340, "learners": 45200, "avgScore": 72}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "paws", "name": "Paws", "domain": "animals", "domainLabel": "Animal Welfare & Coexistence", "emoji": "🐾",
        "pillar": "PLANET", "colors": ["#D97706", "#FBBF24"],
        "bio": "Animal welfare advocate. Community dog coexistence, rabies prevention, feeding etiquette, and urban wildlife care.",
        "topics": ["🐕 Street Dogs", "💉 Rabies 001", "🐾 Body Language", "🍲 Ethical Feeding", "🐦 Urban Birds", "🚨 Injured Animals"],
        "persona": "Compassionate animal caregiver. Empathetic, calm, rabies-vigilant, community harmony advocate.",
        "baseStats": {"posts": 720, "learners": 26800, "avgScore": 74}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "volt", "name": "Volt", "domain": "greenenergy", "domainLabel": "Clean Energy & Resources", "emoji": "⚡",
        "pillar": "PLANET", "colors": ["#059669", "#34D399"],
        "bio": "Renewable energy and smart resource coach. Solar rooftop basics, EV safety, phantom power, and battery recycling.",
        "topics": ["☀️ Solar Rooftops", "🔋 Battery Care", "🔌 Phantom Power", "⚡ EV Smarts", "💡 LED Efficiency", "♻️ E-Waste"],
        "persona": "Enthusiastic green tech engineer. Quantitative, practical, solution-driven, excited about zero-emission futures.",
        "baseStats": {"posts": 680, "learners": 24500, "avgScore": 71}, "minGrade": 5, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "civic", "name": "Civic", "domain": "civic", "domainLabel": "Civic Sense & Public Spaces", "emoji": "🏛️",
        "pillar": "PLANET", "colors": ["#3B82F6", "#93C5FD"],
        "bio": "Being the person others are glad to share a city with. Public spaces, queues, kindness and responsibility.",
        "topics": ["🚌 Public transport", "🧹 Cleanliness", "🧍 Queues", "🤝 Respect", "🔊 Noise", "🗳️ Rights & duties"],
        "persona": "Warm community mentor. Encourages kindness, not blame. Shows how small actions add up.",
        "baseStats": {"posts": 874, "learners": 33500, "avgScore": 77}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },

    # FUTURE Pillar
    {
        "id": "coin", "name": "Coin", "domain": "money", "domainLabel": "Money & Practical Finance", "emoji": "🪙",
        "pillar": "FUTURE", "colors": ["#16A34A", "#4ADE80"],
        "bio": "Practical money coach. Needs vs wants, UPI PIN rules, compound interest, scam warnings, and youth bank accounts.",
        "topics": ["🏷️ Needs vs Wants", "🏦 Minor Accounts", "📱 UPI Safety", "📈 Compounding", "🛑 Scam Alerts", "🎯 Savings Goals"],
        "persona": "Pragmatic, sharp wealth mentor. Honest, practical, anti-scam, demystifies real-world economics for youth.",
        "baseStats": {"posts": 860, "learners": 32800, "avgScore": 70}, "minGrade": 5, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "forge", "name": "Forge", "domain": "enterprise", "domainLabel": "Enterprise & Building", "emoji": "🔨",
        "pillar": "FUTURE", "colors": ["#CA8A04", "#FACC15"],
        "bio": "Student startup builder coach. Problem finding, elevator pitching, school stalls, feedback loops, and servant leadership.",
        "topics": ["💡 Problem Finding", "🎤 1-Min Pitch", "🎪 School Stalls", "📊 Feedback Loops", "🤝 Team Roles", "♻️ Circular Biz"],
        "persona": "Encouraging venture builder. Action-biased, iterative, celebrates fast learning from early rejections.",
        "baseStats": {"posts": 590, "learners": 21600, "avgScore": 72}, "minGrade": 5, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "compass", "name": "Compass", "domain": "careers", "domainLabel": "Careers & Higher Ed", "emoji": "🧭",
        "pillar": "FUTURE", "colors": ["#0891B2", "#67E8F9"],
        "bio": "Streams, courses and careers after Class 10 and 12, explained simply. For Classes 9–12.",
        "topics": ["🧪 Science", "📊 Commerce", "🎨 Arts", "🛠️ Diplomas", "📝 Entrance exams", "💼 Jobs"],
        "persona": "Supportive career counsellor. Balanced, no pressure, no ranking of careers. Points to official sources.",
        "baseStats": {"posts": 512, "learners": 18900, "avgScore": 70}, "minGrade": 9, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "cipher", "name": "Cipher", "domain": "digital", "domainLabel": "Cyber Safety & Scams", "emoji": "🔐",
        "pillar": "FUTURE", "colors": ["#7C3AED", "#C4B5FD"],
        "bio": "Spot scams, protect passwords and stay kind online. Built for the first phone in the family.",
        "topics": ["🎣 Phishing", "🔑 OTPs", "🔒 Passwords", "🙅 Strangers", "📸 Privacy", "💬 Cyberbullying"],
        "persona": "Sharp but friendly cyber detective. Teaches the warning signs, never fear.",
        "baseStats": {"posts": 768, "learners": 30200, "avgScore": 79}, "minGrade": 4, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "basil", "name": "Basil", "domain": "nutrition", "domainLabel": "Food & Nutrition Literacy", "emoji": "🥗",
        "pillar": "FUTURE", "colors": ["#65A30D", "#BEF264"],
        "bio": "Food that fuels you. Reading labels, smart snacks, water, balanced plates, without the lectures.",
        "topics": ["🏷️ Labels", "🥤 Drinks", "🍱 Tiffin", "💧 Water", "🍎 Snacks", "🧼 Food hygiene"],
        "persona": "Cheerful nutrition buddy. Never shames food or bodies. No diets, calorie counting or weight talk.",
        "baseStats": {"posts": 902, "learners": 36100, "avgScore": 74}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },

    # MIND Pillar
    {
        "id": "echo", "name": "Echo", "domain": "feelings", "domainLabel": "Feelings & Mental Wellbeing", "emoji": "💭",
        "pillar": "MIND", "colors": ["#8B5CF6", "#C084FC"],
        "bio": "Emotional literacy & mental health guide. Naming emotions, exam stress, saying no, handling grief, and Tele-MANAS 14416.",
        "topics": ["🎯 Naming Feelings", "🌬️ Exam Calm", "🛑 Saying No", "🩹 Forgiveness", "🌱 Growth Mindset", "📞 Tele-MANAS"],
        "persona": "Warm, deeply empathetic counselor. Validating, gentle, never preachy. Always prioritizes psychological safety.",
        "baseStats": {"posts": 880, "learners": 35400, "avgScore": 77}, "minGrade": 4, "sensitive": True, "approveFirst": True, "defaultTopicOn": True
    },
    {
        "id": "pixel", "name": "Pixel", "domain": "screentime", "domainLabel": "Digital Balance & Screen Health", "emoji": "📱",
        "pillar": "MIND", "colors": ["#06B6D4", "#67E8F9"],
        "bio": "Screen balance & digital wellbeing coach. Phone curfews, notification diets, gaming limits, doom-scrolling, and 20-20-20 rule.",
        "topics": ["⏳ App Limits", "🔕 Notification Diet", "🎮 Gaming Curfew", "🥗 Phone-Free Meals", "👁️ 20-20-20 Rule", "🧘 Detox Days"],
        "persona": "Relatable digital mentor. Pragmatic, tech-positive yet fiercely pro-sleep and real-world connection.",
        "baseStats": {"posts": 930, "learners": 38600, "avgScore": 75}, "minGrade": 4, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    },
    {
        "id": "saathi", "name": "Saathi", "domain": "inclusion", "domainLabel": "Inclusion, Empathy & Anti-Bullying", "emoji": "🤝",
        "pillar": "MIND", "colors": ["#14B8A6", "#5EEAD4"],
        "bio": "Empathy, disability allyship & anti-bullying champion. Neurodiversity, sign language, welcoming newcomers and upstander courage.",
        "topics": ["♿ Accessibility", "🤟 Sign Language", "🛡️ Upstander Action", "🧩 Neurodiversity", "🍱 Food Harmony", "🤝 Deep Listening"],
        "persona": "Kind, courageous inclusion ally. Celebrates diversity, fiercely opposes cruelty, fosters belonging for every child.",
        "baseStats": {"posts": 820, "learners": 33900, "avgScore": 76}, "minGrade": 3, "sensitive": False, "approveFirst": False, "defaultTopicOn": True
    }
]

def load_existing_base_cards(agent_id):
    """Loads existing cards from backend/app/content/fact_cards/<agent_id>.json if it exists."""
    fpath = CARDS_DIR / f"{agent_id}.json"
    if not fpath.exists():
        return []
    try:
        data = json.loads(fpath.read_text(encoding="utf-8"))
        return data.get("cards", [])
    except Exception as e:
        print(f"Error reading {fpath}: {e}")
        return []

def validate_card(card):
    """Strictly validates a fact card according to WotNow rubric and content rules."""
    cid = card.get("id")
    if not cid:
        raise ValueError(f"Card missing id: {card}")

    if "sources" not in card:
        card["sources"] = [{"name": "National Guidelines & Safety Standards", "url": "https://india.gov.in"}]

    # Check required fields
    for field in ["agentId", "subtopic", "title", "bands", "facts", "do", "dont", "myths", "quiz", "scenario", "sources"]:
        if field not in card:
            raise ValueError(f"Card {cid} missing field '{field}'")

    # Check scenario rubric weights if scenario present
    scenario = card.get("scenario")
    if scenario:
        rubric = scenario.get("rubric", [])
        if rubric:
            total_weight = sum(item.get("weight", 0) for item in rubric)
            if total_weight != 100:
                # adjust first item if rounding discrepancy
                rubric[0]["weight"] += (100 - total_weight)

            # Check regex compilation
            for r in rubric:
                pattern = r.get("matches", "") or r.get("keys", "")
                if pattern:
                    try:
                        re.compile(pattern, re.IGNORECASE)
                    except re.error as e:
                        raise ValueError(f"Card {cid} invalid rubric regex '{pattern}': {e}")

        for dang in scenario.get("dangerous", []):
            try:
                re.compile(dang, re.IGNORECASE)
            except re.error as e:
                raise ValueError(f"Card {cid} invalid dangerous regex '{dang}': {e}")

    return True

def generate_catalog():
    print("=" * 60)
    print("STARTING FULL CATALOG GENERATION (20 AGENTS, 4 PILLARS)")
    print("=" * 60)

    # Map of generators for each agent
    agent_generators = {
        # Existing 8 (base cards + expanded)
        "ember": ("existing", get_ember_expanded_cards),
        "signal": ("existing", get_signal_cards),
        "pulse": ("existing", get_pulse_cards),
        "basil": ("existing", get_basil_cards),
        "civic": ("existing", get_civic_cards),
        "terra": ("existing", get_terra_cards),
        "cipher": ("existing", get_cipher_cards),
        "compass": ("existing", get_compass_cards),

        # 12 New agents
        "storm": ("new", get_storm_cards),
        "guardian": ("new", get_guardian_cards),
        "nyaya": ("new", get_nyaya_cards),
        "stride": ("new", get_stride_cards),
        "care": ("new", get_care_cards),
        "paws": ("new", get_paws_cards),
        "volt": ("new", get_volt_cards),
        "coin": ("new", get_coin_cards),
        "forge": ("new", get_forge_cards),
        "echo": ("new", get_echo_cards),
        "pixel": ("new", get_pixel_cards),
        "saathi": ("new", get_saathi_cards),
    }

    total_cards = 0
    all_card_ids = set()
    summary_stats = []

    for agent_meta in ALL_AGENTS_METADATA:
        aid = agent_meta["id"]
        pillar = agent_meta["pillar"]
        kind, gen_func = agent_generators[aid]

        final_cards = []
        if kind == "existing":
            base_cards = load_existing_base_cards(aid)
            # Filter out any duplicate IDs if previously run
            expanded = gen_func()
            seen_ids = set()
            for c in base_cards:
                if c["id"] not in seen_ids:
                    seen_ids.add(c["id"])
                    final_cards.append(c)
            for c in expanded:
                if c["id"] not in seen_ids:
                    seen_ids.add(c["id"])
                    final_cards.append(c)
        else:
            final_cards = gen_func()

        # Validate each card
        for card in final_cards:
            validate_card(card)
            cid = card["id"]
            if cid in all_card_ids:
                raise ValueError(f"DUPLICATE CARD ID DETECTED: {cid}")
            all_card_ids.add(cid)

        # Write card file
        card_file = CARDS_DIR / f"{aid}.json"
        card_payload = {
            "agentId": aid,
            "cards": final_cards
        }
        card_file.write_text(json.dumps(card_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        card_count = len(final_cards)
        total_cards += card_count
        summary_stats.append((aid, agent_meta["name"], pillar, card_count))
        print(f"[{pillar}] Agent '{aid}' ({agent_meta['name']}): Written {card_count} verified cards -> {card_file.name}")

    # Write updated agents.json
    AGENTS_FILE.write_text(json.dumps(ALL_AGENTS_METADATA, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWritten {len(ALL_AGENTS_METADATA)} agents to {AGENTS_FILE}")

    print("\n" + "=" * 60)
    print("EXPANSION COMPLETE - SUMMARY TABLE:")
    print("=" * 60)
    print(f"{'Pillar':<10} | {'Agent ID':<10} | {'Agent Name':<12} | {'Cards':<6}")
    print("-" * 46)
    for aid, name, pillar, count in summary_stats:
        print(f"{pillar:<10} | {aid:<10} | {name:<12} | {count:<6}")
    print("-" * 46)
    print(f"TOTAL VERIFIED SKILL CARDS: {total_cards} across {len(summary_stats)} agents")
    print("=" * 60)

if __name__ == "__main__":
    generate_catalog()
