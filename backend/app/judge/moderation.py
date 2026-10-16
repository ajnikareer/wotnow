"""Reply moderation before anything becomes visible to other students."""
from __future__ import annotations

import re

from ..ai import prompts
from ..ai.llm import get_llm
from ..ai.schemas import ModerationOut

PROFANITY = re.compile(r"\b(stupid|idiot|dumb|shut up|hate you|loser|f+u+c+k\w*|sh+i+t\w*|bitch\w*|bastard|chutiya|madarchod|bc|mc)\b", re.I)
PERSONAL = re.compile(r"(\+?\d[\d\s-]{8,}\d)|[\w.+-]+@[\w-]+\.\w+|@\w{3,}|https?://|www\.|instagram|snapchat|whatsapp me|my address", re.I)


def rule_check(text: str) -> tuple[str, str]:
    if PROFANITY.search(text):
        return "abusive", "contains insulting or bad language"
    if PERSONAL.search(text):
        return "personal_info", "contains contact details or links"
    return "ok", ""


async def moderate(text: str) -> dict:
    label, reason = rule_check(text)
    if label != "ok":
        return {"label": label, "reason": reason, "by": "rules"}
    llm = get_llm()
    if llm.available:
        r = await llm.generate_json(prompts.SYSTEM_MOD, f"REPLY: <<<{text}>>>", ModerationOut, temperature=0)
        if r and r.get("label") in ("ok", "off_topic", "abusive", "personal_info", "unsafe_advice"):
            return {"label": r["label"], "reason": r.get("reason", ""), "by": "gemini"}
    return {"label": "ok", "reason": "", "by": "rules"}
