"""
Validation for AI-generated posts. Anything that fails is rejected and regenerated.
Some issues are auto-fixed (weights normalised, emoji count, masked numbers); real problems reject.
"""
from __future__ import annotations

import re

MEDICAL = re.compile(r"\b\d+\s?(mg|ml|mcg|tablets?|pills?)\b|\b(paracetamol|ibuprofen|aspirin|antibiotic|dose|dosage|crocin|dolo)\b", re.I)
UNSAFE = re.compile(r"\b(kill|suicide|blood everywhere|dead body|weapon|gun|knife attack|alcohol|beer|cigarette|vape|girlfriend|boyfriend|date night)\b", re.I)
URL = re.compile(r"https?://|www\.", re.I)
PHONE = re.compile(r"(?<![\d•])(\+?91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}(?!\d)")
ALLOWED_NUMBERS = {"112", "101", "108", "1930", "1098"}


def _words(s: str) -> int:
    return len(re.findall(r"\w+", s or ""))


def _common(p: dict, errs: list[str]) -> None:
    text = " ".join(str(p.get(k, "")) for k in ("title", "body", "question", "statement", "explanation", "modelAnswer"))
    text += " " + " ".join(o["text"] for o in p.get("options") or [])
    if MEDICAL.search(text):
        errs.append("medical/medicine content")
    if UNSAFE.search(text):
        errs.append("unsuitable content for children")
    if p["type"] != "scam_legit" and URL.search(text):
        errs.append("contains a URL")
    if not p.get("title") or len(p["title"]) > 80:
        errs.append("title missing/too long")


def mask_numbers(text: str) -> str:
    return PHONE.sub(lambda m: (m.group(0)[:-6] + "••••" + m.group(0)[-2:]) if len(m.group(0)) >= 8 else m.group(0), text)


def validate(p: dict, allowed_cards: set[str]) -> tuple[dict | None, list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    _common(p, errs)
    t = p["type"]
    if t == "scenario":
        if not (25 <= _words(p.get("body", "")) <= 140):
            errs.append(f"body length {_words(p.get('body', ''))} words")
        q = (p.get("question") or "").strip()
        if not q.endswith("?"):
            errs.append("question must end with '?'")
        rub = p.get("rubric") or []
        if not 3 <= len(rub) <= 5:
            errs.append(f"rubric must have 3-5 items, got {len(rub)}")
        else:
            for r in rub:
                if r.get("card") not in allowed_cards:
                    warns.append(f"rubric card {r.get('card')} not allowed -> reassigned")
                    r["card"] = sorted(allowed_cards)[0]
                r["weight"] = max(5, min(60, int(r.get("weight") or 0)))
            total = sum(r["weight"] for r in rub)
            for r in rub:
                r["weight"] = round(r["weight"] * 100 / total)
            rub[0]["weight"] += 100 - sum(r["weight"] for r in rub)
            for i, r in enumerate(rub):
                r["id"] = f"r{i + 1}"
            if not any(r.get("critical") for r in rub):
                warns.append("no critical item")
        em = [e for e in (p.get("scene") or {}).get("emojis", []) if e][:3]
        while len(em) < 3:
            em.append("✨")
        p["scene"] = {"emojis": em, "bubble": ((p.get("scene") or {}).get("bubble") or "")[:48] or None}
    elif t == "poll":
        opts = p.get("options") or []
        if len(opts) != 4 or len({o["text"].strip().lower() for o in opts}) != 4:
            errs.append("poll needs 4 distinct options")
        if p.get("answerKey") not in {o["id"] for o in opts}:
            errs.append("answerKey not an option")
        if not (p.get("question") or "").strip().endswith(("?", "…", ":")):
            errs.append("question must end with '?'")
    elif t == "myth_fact":
        if p.get("answerKey") not in ("myth", "fact"):
            errs.append("answer must be myth/fact")
        if not (4 <= _words(p.get("statement", "")) <= 30):
            errs.append("statement length")
    elif t == "scam_legit":
        if p.get("answerKey") not in ("scam", "legit"):
            errs.append("answer must be scam/legit")
        msg = p.get("message") or {}
        if not msg.get("text"):
            errs.append("message missing")
        else:
            msg["text"] = mask_numbers(msg["text"])
            msg["from"] = mask_numbers(msg.get("from") or "Unknown")
    if t in ("poll", "myth_fact", "scam_legit") and len(p.get("explanation") or "") < 15:
        errs.append("explanation too short")
    p.setdefault("_warnings", []).extend(warns)
    return (None, errs) if errs else (p, warns)
