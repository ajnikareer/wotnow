"""Terra's daily local alert per city: live conditions → (Gemini or rules) → validated post."""
from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import AlertDraft
from ..config import get_settings
from ..conditions.live import conditions, locate_cached
from ..store.base import get_db
from .cards import source_cards
from .generator import POSTS, now_iso

STEP_LIB = {
    "heat":  [("💧", "Carry a water bottle and sip often"), ("🧢", "Wear a cap and stay in shade at noon"), ("🪴", "Water plants early, before 8 AM")],
    "air":   [("🏠", "Keep outdoor games light today"), ("🚫", "Remind adults not to burn dry leaves"), ("🚌", "Share a ride or take the bus")],
    "dry":   [("🚿", "Take a bucket bath instead of a shower"), ("🪥", "Turn the tap off while brushing"), ("♻️", "Reuse RO water for mopping")],
    "rain":  [("☂️", "Carry an umbrella and avoid puddles near wires"), ("🦟", "Empty standing water in pots and coolers"), ("🧹", "Keep drains free of litter")],
    "nice":  [("🚶", "Walk or cycle for a short trip"), ("🌳", "Water a tree or plant near you"), ("💡", "Switch off lights and fans you don't need")],
}


def _signals(c: dict) -> list[str]:
    sig = []
    if c["feels_like_c"] >= 35 or c["max_c"] >= 37:
        sig.append("heat")
    if (c["aqi"] or 0) > 100:
        sig.append("air")
    if c["rain_7d_mm"] >= 25:
        sig.append("rain")
    elif c["rain_7d_mm"] <= 2 and c["max_c"] >= 30:
        sig.append("dry")
    return sig or ["nice"]


def _chips(c: dict) -> list[str]:
    chips = [f"🌡️ {c['temp_c']}°C (feels {c['feels_like_c']}°C)", f"😷 AQI {c['aqi']} · {c['aqi_band']}"]
    chips.append(f"🌧️ {c['rain_7d_mm']} mm rain this week")
    return chips


def _title(c: dict, sig: list[str]) -> str:
    words = {"heat": "Hot", "air": "hazy", "dry": "dry", "rain": "Rainy", "nice": "Pleasant"}
    if sig == ["nice"]:
        return f"Pleasant day in {c['city']}"
    if "heat" in sig and "air" in sig:
        return f"Hot and hazy in {c['city']} today"
    return f"{words[sig[0]].capitalize()} day in {c['city']}"


async def build_alert(city: str, publish: bool = True) -> dict:
    loc = await locate_cached(city)
    tz = ZoneInfo(get_settings().TIMEZONE)
    day = datetime.now(tz).date().isoformat()
    pid = f"alert-{loc['slug']}-{day}"
    db = get_db()
    existing = db.get(POSTS, pid)
    if existing:
        return existing
    c = await conditions(city, loc)
    sig = _signals(c)
    steps = (STEP_LIB[sig[0]] + sum((STEP_LIB[s] for s in sig[1:]), []))[:3]
    title, body = _title(c, sig), "Pick one small thing to do today:"
    source = "rules"
    llm = get_llm()
    if llm.available:
        d = await llm.generate_json(prompts.SYSTEM_ALERT, f"CONDITIONS: {c}\nMAIN SIGNALS: {sig}", AlertDraft, temperature=0.6)
        if d and len(d.get("steps", [])) == 3 and len(d.get("step_emojis", [])) == 3 and len(d.get("title", "")) <= 60:
            title, body = d["title"], d["body"]
            steps = list(zip(d["step_emojis"], d["steps"]))
            source = "gemini"
    post = {"id": pid, "agentId": "terra", "type": "local_alert", "createdAt": now_iso(), "bands": ["junior", "middle", "senior"],
            "city": c["city"], "citySlug": c["slug"], "title": title, "body": body, "chips": _chips(c),
            "steps": [{"emoji": e, "text": t} for e, t in steps], "sourceCards": source_cards(["ENV-004", "ENV-001"]),
            "status": "live", "source": source, "conditions": c, "stats": {"responses": 0, "avgScore": None}, "checkins": 0}
    if publish:
        db.put(POSTS, pid, post)
    return post
