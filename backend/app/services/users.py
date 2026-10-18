"""Student profiles: XP, levels, streaks, skills, badges, activity log, parent limits."""
from __future__ import annotations

import re
from datetime import timedelta

from fastapi import HTTPException

from ..engine import cards as C
from ..judge import scoring
from ..store.base import get_db
from . import clock

USERS = "users"
PUBLIC = ("id", "nickname", "avatar", "grade", "band", "city", "country", "school", "className", "xp", "level", "levelName",
          "nextLevelXp", "streak", "answers", "avgScore", "skills", "badges", "follows")
ALL_DOMAINS = ["fire", "road", "firstaid", "nutrition", "civic", "environment", "digital", "careers"]
DEMO_SCHOOL = "Sunrise Public School"   # new demo users join the seeded school so leaderboards are populated

BADGES = [
    ("first", "✨", "First Answer", lambda u: u["answers"] >= 1),
    ("streak7", "🔥", "7-Day Streak", lambda u: u.get("bestStreak", 0) >= 7),
    ("fire", "🧯", "Fire Ready", lambda u: u["skills"].get("fire", 0) >= 80),
    ("road", "🚑", "Road Rescuer", lambda u: u["skills"].get("road", 0) >= 80),
    ("scam", "🕵️", "Scam Spotter", lambda u: u["counts"].get("scamCorrect", 0) >= 3),
    ("fast", "⚡", "Fastest Finger", lambda u: u["counts"].get("quizBest", 0) >= 60),
    ("green", "🌱", "Green Week", lambda u: u["counts"].get("checkins", 0) >= 5),
    ("aid", "🩹", "First Responder", lambda u: u["skills"].get("firstaid", 0) >= 80),
]


def default_settings(grade: int) -> dict:
    return {"dailyLimit": 30, "quietHours": "", "weeklyEmail": True,
            "topics": {d: (d != "careers" or grade >= 9) for d in ALL_DOMAINS}}


def auto_class(grade: int) -> str:
    return f"Class {grade} A"


def new_user(uid: str) -> dict:
    grade = 8
    return {"id": uid, "nickname": "NewLearner", "avatar": "🦊", "grade": grade, "band": C.band_for_grade(grade),
            "city": "Pune", "country": "India",
            "school": DEMO_SCHOOL, "className": auto_class(grade), "xp": 0, "streak": 0, "bestStreak": 0, "lastActiveDate": None,
            "answers": 0, "scoreSum": 0, "skillHistory": {}, "counts": {},
            "follows": [a["id"] for a in C.agents() if a["minGrade"] <= grade],
            "weekXp": {}, "parentSettings": default_settings(grade), "createdAt": clock.utc_iso()}


def get_user(uid: str, create: bool = True) -> dict:
    db = get_db()
    u = db.get(USERS, uid)
    if u is None:
        if not create:
            raise HTTPException(404, "user not found")
        u = new_user(uid)
        db.put(USERS, uid, u)
    return u


def save(u: dict) -> dict:
    get_db().put(USERS, u["id"], u)
    return u


def skills_of(u: dict) -> dict:
    return {d: round(sum(v) / len(v)) for d, v in u.get("skillHistory", {}).items() if v}


def public(u: dict) -> dict:
    lvl, name, nxt = scoring.level_for(u["xp"])
    view = dict(u)
    view.setdefault("country", u.get("country") or "India")
    view.update(level=lvl, levelName=name, nextLevelXp=nxt, skills=skills_of(u),
                avgScore=round(u["scoreSum"] / u["answers"]) if u.get("answers") else 0)
    view["badges"] = [{"id": b, "emoji": e, "name": n, "earned": bool(f(view | {"counts": u.get("counts", {})}))} for b, e, n, f in BADGES]
    return {k: view.get(k) for k in PUBLIC}


def is_nickname_taken(nickname: str, exclude_uid: Optional[str] = None) -> bool:
    clean = re.sub(r"[^A-Za-z0-9]", "", str(nickname)).strip().lower()
    if not clean:
        return False
    db = get_db()
    for doc in db.query(USERS):
        if exclude_uid and doc.get("id") == exclude_uid:
            continue
        existing = str(doc.get("nickname") or "").strip().lower()
        if existing == clean:
            return True
    return False


EDITABLE = {"nickname", "avatar", "grade", "city", "country", "school", "className", "follows"}


def update_profile(u: dict, patch: dict) -> dict:
    was_auto_class = (u.get("className") or "") in ("", auto_class(u.get("grade", 8)))
    for k, v in patch.items():
        if k in EDITABLE and v is not None:
            u[k] = v
    if "nickname" in patch:
        raw = str(patch["nickname"]).strip()
        clean = re.sub(r"[^A-Za-z0-9]", "", raw)[:16]
        if len(clean) < 3:
            raise HTTPException(400, "Nickname must be at least 3 letters or numbers.")
        if is_nickname_taken(clean, exclude_uid=u.get("id")):
            raise HTTPException(409, f"Nickname '{clean}' is already taken. Please choose another unique nickname!")
        u["nickname"] = clean
    if "country" in patch and patch["country"]:
        u["country"] = str(patch["country"]).strip()[:50] or "India"
    if "city" in patch and patch["city"]:
        u["city"] = str(patch["city"]).strip()[:40] or "Pune"
    if "grade" in patch:
        u["grade"] = max(3, min(12, int(u["grade"])))
        u["band"] = C.band_for_grade(u["grade"])
        u["parentSettings"]["topics"]["careers"] = u["grade"] >= 9 and u["parentSettings"]["topics"].get("careers", True)
        if was_auto_class and "className" not in patch:
            u["className"] = auto_class(u["grade"])
    if not u.get("school"):
        u["school"] = DEMO_SCHOOL
    valid = {a["id"] for a in C.agents() if a["minGrade"] <= u["grade"]}
    u["follows"] = [f for f in u.get("follows", []) if f in valid]
    return save(u)


# ---------------- activity, XP, streaks ----------------
def activity(uid: str) -> list[dict]:
    return sorted(get_db().query(f"{USERS}/{uid}/activity"), key=lambda a: a["ts"])


def minutes_on(uid: str, day) -> float:
    return sum(scoring.MINUTES.get(a["kind"], 0) for a in activity(uid) if a["date"] == day.isoformat())


def enforce_limits(u: dict) -> None:
    s = u.get("parentSettings") or {}
    limit = s.get("dailyLimit")
    if limit and minutes_on(u["id"], clock.today()) >= limit:
        raise HTTPException(429, "Daily time limit reached. See you tomorrow! 🌙")
    qh = (s.get("quietHours") or "").replace("–", "-").replace(" ", "")
    if "-" in qh:
        try:
            a, b = qh.split("-")
            now = clock.now_local().strftime("%H:%M")
            inside = (a <= now < b) if a < b else (now >= a or now < b)
            if inside:
                raise HTTPException(429, "It's quiet hours right now. Come back later! 🌙")
        except HTTPException:
            raise
        except Exception:
            pass


def record(u: dict, kind: str, xp: int, *, post: dict | None = None, score: int | None = None,
           domain: str | None = None, missed: str | None = None, extra: dict | None = None) -> dict:
    """Adds XP, updates streak/skills/week XP and logs an activity row. Returns the saved user."""
    db = get_db()
    today = clock.today()
    last = u.get("lastActiveDate")
    if last != today.isoformat():
        u["streak"] = u.get("streak", 0) + 1 if last == (today - timedelta(days=1)).isoformat() else 1
        u["lastActiveDate"] = today.isoformat()
        u["bestStreak"] = max(u.get("bestStreak", 0), u["streak"])
    u["xp"] = u.get("xp", 0) + xp
    wk = clock.week_id(today)
    u["weekXp"] = {wk: u.get("weekXp", {}).get(wk, 0) + xp}
    if domain and score is not None:
        hist = u.setdefault("skillHistory", {}).setdefault(domain, [])
        hist.append(score)
        u["skillHistory"][domain] = hist[-10:]
    row = {"id": f"{clock.utc_iso()}-{kind}", "ts": clock.utc_iso(), "date": today.isoformat(), "kind": kind, "xp": xp,
           "score": score, "domain": domain, "missed": missed,
           "postId": post and post["id"], "postTitle": post and post.get("title"), "agentId": post and post.get("agentId")}
    if extra:
        row.update(extra)
    db.put(f"{USERS}/{u['id']}/activity", row["id"], row)
    return save(u)


def my_state(uid: str) -> dict:
    return {d["postId"]: d["my"] for d in get_db().query(f"{USERS}/{uid}/my")}


def set_my(uid: str, post_id: str, my: dict) -> None:
    get_db().put(f"{USERS}/{uid}/my", post_id, {"postId": post_id, "my": my})


def get_my(uid: str, post_id: str) -> dict | None:
    d = get_db().get(f"{USERS}/{uid}/my", post_id)
    return d["my"] if d else None


def delete_user(uid: str) -> None:
    db = get_db()
    for coll in (f"{USERS}/{uid}/activity", f"{USERS}/{uid}/my"):
        for d in db.query(coll):
            db.delete(coll, d.get("id") or d.get("postId"))
    db.delete(USERS, uid)
