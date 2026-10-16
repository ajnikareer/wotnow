"""Code-owned numbers: scores, XP, levels. The LLM never produces these."""
from __future__ import annotations

LEVELS = ["Beginner", "Aware", "Alert", "Capable", "Skilled", "Steady", "Prepared", "Guardian", "Responder", "Life-Ready"]
THRESHOLDS = [0, 150, 350, 650, 1000, 1500, 2200, 3000, 3800, 4600]   # XP needed to reach level i+1
DANGER_CAP = 40
SHORT_CAP = 20


def level_for(xp: int) -> tuple[int, str, int]:
    lvl = sum(1 for t in THRESHOLDS if xp >= t)
    nxt = THRESHOLDS[lvl] if lvl < len(THRESHOLDS) else THRESHOLDS[-1] + 800 * (lvl - len(THRESHOLDS) + 1)
    return lvl, LEVELS[min(lvl, len(LEVELS)) - 1], nxt


def score(rubric: list[dict], hits: set[str], dangerous: bool, short: bool) -> int:
    s = sum(r["weight"] for r in rubric if r["id"] in hits)
    if dangerous:
        s = min(s, DANGER_CAP)
    if short:
        s = min(s, SHORT_CAP)
    return max(0, min(100, int(s)))


def label(score: int, dangerous: bool, missed: int) -> str:
    if dangerous:
        return "Careful! That could be dangerous."
    if score >= 90:
        return "Brilliant answer!"
    if score >= 70:
        return "Good. One key step missing." if missed == 1 else "Good answer!"
    if score >= 40:
        return "Nice try. A few steps missing."
    return "Let’s learn this one together."


XP_VOTE = {"poll": (10, 2), "myth_fact": (5, 2), "scam_legit": (5, 2)}   # (correct, wrong)
XP_CHECKIN = 5
MINUTES = {"answer": 2.0, "vote": 0.5, "checkin": 0.3, "quiz": 2.0}       # estimated time per activity


def answer_xp(score: int) -> int:
    return round(score / 2)
