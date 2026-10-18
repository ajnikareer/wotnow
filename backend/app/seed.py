"""
Demo seed: posts that mirror the web app's sample content, a demo student with history,
classmates and other schools for leaderboards, and the first live quiz.
Runs automatically on startup when the database is empty (AUTO_SEED=true), or via POST /jobs/seed.
"""
from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone

from .engine import cards as C
from .engine.generator import POSTS, from_card
from .engine.planner import combo_key
from .engine.quiz import QUIZZES, _from_cards
from .judge.judge import offline_judge, template_feedback
from .judge import scoring
from .services import clock, users
from .store.base import get_db

DEMO_UID = "demo-student"
SCHOOL, CITY = "Sunrise Public School", "Pune"


def _combo(agent, card, kind, band, character="Maya", relation="her younger brother", setting="home", time="8 PM", variant=0):
    c = {"agentId": agent, "cardId": card, "kind": kind, "band": band, "setting": setting, "character": character,
         "relation": relation, "twist": "", "time": time, "difficulty": "medium", "variant": variant}
    c["key"] = combo_key(c)
    return c


SEED_POSTS = [
    # id, combo, minutes ago, vote baseline (percent) or (responses, avgScore)
    ("oil-fire", _combo("ember", "FIRE-012", "scenario", "middle"), 24, (2418, 61)),
    ("cyberbullying", _combo("cipher", "DIG-029", "scenario", "middle", character="Rohan", setting="school"), 35, (4120, 84)),
    ("screenshare-scam", _combo("cipher", "DIG-028", "poll", "middle"), 45, {"a": 4, "b": 91, "c": 3, "d": 2, "_n": 5820}),
    ("road-first", _combo("signal", "ROAD-021", "poll", "senior"), 70, {"a": 27, "b": 61, "c": 4, "d": 8, "_n": 18902}),
    ("needs-wants", _combo("coin", "MON-001", "scenario", "middle", character="Kabir", setting="home"), 95, (3120, 78)),
    ("upi-pin-scam", _combo("coin", "MON-005", "myth_fact", "middle"), 105, {"myth": 94, "fact": 6, "_n": 8320}),
    ("toothpaste", _combo("pulse", "AID-002", "myth_fact", "middle"), 120, {"myth": 71, "fact": 29, "_n": 9320}),
    ("wifi-sniff", _combo("cipher", "DIG-026", "poll", "senior"), 135, {"a": 11, "b": 76, "c": 7, "d": 6, "_n": 8940}),
    ("exam-panic", _combo("echo", "FEEL-002", "scenario", "senior", character="Priya", setting="school"), 150, (4210, 72)),
    ("scam-power", _combo("cipher", "DIG-007", "scam_legit", "middle"), 180, {"scam": 83, "legit": 17, "_n": 7410}),
    ("eye-rule-20", _combo("pixel", "TECH-001", "myth_fact", "middle"), 195, {"myth": 78, "fact": 22, "_n": 8190}),
    ("upstander-lunch", _combo("saathi", "INC-001", "scenario", "junior", character="Dev", setting="school"), 215, (3840, 82)),
    ("nosebleed", _combo("pulse", "AID-011", "scenario", "middle", character="Sam", setting="school classroom"), 240, (5120, 58)),
    ("secret-surprise", _combo("guardian", "SAFE-002", "myth_fact", "junior"), 255, {"myth": 91, "fact": 9, "_n": 10420}),
    ("mrp-chips", _combo("nyaya", "LAW-003", "scenario", "middle", character="Arjun", setting="street market"), 275, (3670, 76)),
    ("drink", _combo("basil", "NUT-005", "poll", "middle"), 300, {"a": 22, "b": 64, "c": 9, "d": 5, "_n": 11240}),
    ("dog-body-lang", _combo("paws", "ANI-001", "scenario", "junior", character="Tanvi", setting="neighbourhood"), 320, (4190, 81)),
    ("phantom-charger", _combo("volt", "GRN-001", "myth_fact", "middle"), 340, {"myth": 74, "fact": 26, "_n": 7920}),
    ("bus-wrapper", _combo("civic", "CIV-003", "scenario", "junior", character="Mia", relation="her friend", setting="city bus"), 360, (3890, 79)),
    ("earthquake-desk", _combo("storm", "DIS-001", "scenario", "middle", character="Aarav", setting="school"), 380, (5120, 79)),
    ("backpack-weight", _combo("stride", "FIT-003", "poll", "junior"), 400, {"a": 11, "b": 82, "c": 5, "d": 2, "_n": 9870}),
    ("wash-20s", _combo("care", "HYG-001", "poll", "junior"), 415, {"a": 5, "b": 89, "c": 3, "d": 3, "_n": 11150}),
    ("pitch-60s", _combo("forge", "ENT-001", "poll", "senior"), 425, {"a": 14, "b": 79, "c": 4, "d": 3, "_n": 4620}),
    ("streams", _combo("compass", "CAR-001", "myth_fact", "senior"), 440, {"myth": 79, "fact": 21, "_n": 4100}),
    ("lift-fire", _combo("ember", "FIRE-003", "myth_fact", "middle"), 460, {"myth": 88, "fact": 12, "_n": 12110}),
]

SEED_TITLES = {
    "oil-fire": "Oil fire in the pan",
    "cyberbullying": "Class group chat drama",
    "screenshare-scam": "Urgent gaming account unlock",
    "road-first": "First at a bike accident",
    "needs-wants": "The limited-edition hoodie",
    "upi-pin-scam": "UPI PIN safety: Enter PIN only to pay",
    "toothpaste": "Burns",
    "wifi-sniff": "Free Wi-Fi at the railway station",
    "exam-panic": "Blank mind before science exam",
    "scam-power": "A message to Dad",
    "eye-rule-20": "Screen eye strain",
    "upstander-lunch": "The new student at the lunch table",
    "nosebleed": "Nosebleed in class",
    "secret-surprise": "Secrets vs surprises",
    "mrp-chips": "Cold drink above MRP",
    "drink": "After the match",
    "dog-body-lang": "Approached by an excited street dog",
    "phantom-charger": "Phone chargers left in wall sockets",
    "bus-wrapper": "No dustbin on the bus",
    "earthquake-desk": "Tremors inside the classroom",
    "backpack-weight": "The 10% schoolbag rule",
    "wash-20s": "Why 20 seconds of soap?",
    "pitch-60s": "The 60-Second Elevator Pitch",
    "streams": "Choosing a stream after Class 10",
    "lift-fire": "Fire in a building",
}

CLASSMATES = [("BlueFalcon", "🦅", 780), ("SunnyOtter", "🦦", 705), ("MintyTiger", "🐯", 690), ("QuietPanda", "🐼", 520),
              ("BraveKoala", "🐨", 480), ("ZippyDolphin", "🐬", 410), ("WiseOwl", "🦉", 365)]
SCHOOLMATES = [("RocketLion", "🦁", "Class 10 A", 910), ("NovaCat", "🐱", "Class 9 C", 760), ("PixelBear", "🐻", "Class 11 A", 720),
               ("StarFish", "🐠", "Class 6 C", 650), ("LuckyLlama", "🦙", "Class 9 B", 540), ("CosmoBee", "🐝", "Class 10 A", 600),
               ("MangoMoose", "🫎", "Class 6 C", 380)]
OTHER_SCHOOLS = {"Green Valley School": 6, "Riverside Academy": 5, "Hilltop High": 5, "Lakeview School": 4}

RESPONSES = {
    "cyberbullying": [("BraveKoala", "🐨", "Do not forward it! Take a screenshot for proof, message Rohan privately to let him know he is not alone, and report the message to the class teacher or counselor.",
                      "Outstanding maturity. Supporting the targeted student while collecting proof is the gold standard of an upstander. 🛡️")],
    "needs-wants": [("SunnyOtter", "🦦", "Buy the ₹600 school books first because they are a clear Need for exams. Save the remaining ₹900 towards the hoodie for next month.",
                    "Perfect application of Needs vs Wants. You secured your exams AND kept money in your pocket! 🪙")],
    "exam-panic": [("ZippyDolphin", "🐬", "Close the books immediately. Sit down, sip water, and do slow 4-7-8 breathing. Remind yourself that blankness is just adrenaline, and memory returns when reading question 1.",
                    "Scientifically accurate. Taking deep exhales resets the nervous system so your prefrontal cortex can think clearly again. 🧠")],
    "oil-fire": [("BlueFalcon", "🦅", "Shout no water! Turn off the stove, slide a metal lid over the pan and leave it. No lid? A damp towel. If flames reach the hood, get everyone out, close the door and call 101.",
                  "Textbook answer. Closing the kitchen door on the way out also slows the fire. 🙌"),
                 ("QuietPanda", "🐼", "Switch off the gas quickly and call an adult.", "Good start! One more step: cover the pan with a metal lid or damp cloth.")],
    "nosebleed": [("SunnyOtter", "🦦", "Tell Sam to sit and lean forward, not back. Pinch the soft part of the nose for 10 minutes and tell the teacher. If it doesn't stop, go to the nurse.",
                   "Perfect. And no peeking before the 10 minutes are up! 👏")],
    "bus-wrapper": [("MintyTiger", "🐯", "Keep it in her bag and throw it in a bin later. And tell her friend nicely not to litter.",
                     "Love the 'tell her friend nicely' part. That's how habits spread. 💙")],
}


def _ago(minutes: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(minutes=minutes)).isoformat()


def _mk_user(uid, nick, avatar, grade, cls, school, city, week_xp, total_xp=None):
    u = users.new_user(uid)
    u.update(nickname=nick, avatar=avatar, grade=grade, band=C.band_for_grade(grade), className=cls, school=school, city=city,
             xp=total_xp or week_xp * 4, weekXp={clock.week_id(): week_xp}, answers=week_xp // 12, scoreSum=(week_xp // 12) * 72)
    return u


async def seed_all(force: bool = False) -> dict:
    db = get_db()
    if not force and db.get(POSTS, "oil-fire"):
        return {"seeded": False}
    rng = random.Random(7)
    n_posts = 0
    for pid, combo, ago, stats in SEED_POSTS:
        p = from_card(combo)
        if p is None:
            continue
        p.update(id=pid, createdAt=_ago(ago), bands=C.card(combo["cardId"])["bands"], source="seed")
        p["title"] = SEED_TITLES.get(pid, p["title"])
        if isinstance(stats, tuple):
            p["stats"] = {"responses": stats[0], "avgScore": stats[1]}
            p["scoreSum"] = stats[0] * stats[1]
        else:
            n = stats.pop("_n")
            p["voteCounts"] = {k: round(v * n / 100) for k, v in stats.items()}
            p["stats"] = {"responses": n, "avgScore": None}
            stats["_n"] = n
        db.put(POSTS, pid, p)
        n_posts += 1

    # users
    wk = clock.week_id()
    demo = users.new_user(DEMO_UID)
    demo.update(nickname="CleverFox", avatar="🦊", grade=8, band="middle", city=CITY, school=SCHOOL, className="Class 8 B",
                xp=2340, streak=12, bestStreak=12, answers=142, scoreSum=142 * 74,
                lastActiveDate=(clock.today() - timedelta(days=1)).isoformat(), weekXp={wk: 640},
                counts={"scamCorrect": 4, "quizBest": 72, "checkins": 6},
                skillHistory={"fire": [82], "road": [64], "firstaid": [48], "nutrition": [71], "civic": [77], "environment": [69], "digital": [88]})
    demo["parentSettings"]["quietHours"] = "22:00 – 06:00"
    db.put(users.USERS, DEMO_UID, demo)
    history = [("oil-fire", "ember", 78, "Cover the pan with a metal lid or damp cloth", 0), ("road-first", "signal", 100, None, 1),
               ("nosebleed", "pulse", 45, "Sit up and lean forward (not back)", 1), ("otp-game", "cipher", 100, None, 2),
               ("bus-wrapper", "civic", 100, None, 3), ("drink", "basil", 100, None, 4), ("lift-fire", "ember", 100, None, 5)]
    for i in range(1, 7):
        day = clock.today() - timedelta(days=i)
        for j in range(rng.randint(3, 8)):
            kind = "vote" if j % 2 else "answer"
            row = {"id": f"seed-{day}-{j}", "ts": f"{day}T1{j}:00:00+00:00", "date": day.isoformat(), "kind": kind, "xp": 10,
                   "score": rng.choice([60, 80, 100]), "domain": "fire", "missed": None, "postId": None, "postTitle": "Practice", "agentId": "ember"}
            db.put(f"users/{DEMO_UID}/activity", row["id"], row)
    for pid, agent, score, missed, days in history:
        p = db.get(POSTS, pid)
        day = clock.today() - timedelta(days=days)
        row = {"id": f"seed-h-{pid}", "ts": f"{day}T18:00:00+00:00", "date": day.isoformat(), "kind": "answer", "xp": score // 2,
               "score": score, "domain": C.agent(agent)["domain"], "missed": missed, "postId": pid, "postTitle": p["title"], "agentId": agent}
        db.put(f"users/{DEMO_UID}/activity", row["id"], row)

    for i, (nick, av, wx) in enumerate(CLASSMATES):
        db.put(users.USERS, f"seed-c{i}", _mk_user(f"seed-c{i}", nick, av, 8, "Class 8 B", SCHOOL, CITY, wx))
    for i, (nick, av, cls, wx) in enumerate(SCHOOLMATES):
        g = int(cls.split()[1])
        db.put(users.USERS, f"seed-s{i}", _mk_user(f"seed-s{i}", nick, av, g, cls, SCHOOL, CITY, wx))
    animals = ["🐺", "🦒", "🐘", "🦩", "🐢", "🦜", "🐿️", "🦔"]
    k = 0
    for school, n in OTHER_SCHOOLS.items():
        for j in range(n):
            db.put(users.USERS, f"seed-o{k}", _mk_user(f"seed-o{k}", f"Learner{k}", animals[k % len(animals)], 7 + j % 5,
                                                         f"Class {7 + j % 5} A", school, CITY, rng.randint(500, 1100)))
            k += 1

    # top responses (scored by the same offline judge)
    all_users = {u["nickname"]: u for u in db.query(users.USERS)}
    for pid, rs in RESPONSES.items():
        p = db.get(POSTS, pid)
        for nick, av, text, reply in rs:
            res = offline_judge(p, text)
            sc = scoring.score(p["rubric"], res["hits"], res["dangerous"], False)
            uid = all_users[nick]["id"]
            db.put(f"{POSTS}/{pid}/responses", uid, {"id": uid, "nickname": nick, "avatar": av, "text": text, "score": sc,
                                                    "hits": sorted(res["hits"]), "dangerous": res["dangerous"],
                                                    "moderation": {"label": "ok", "by": "seed"}, "visible": not res["dangerous"],
                                                    "createdAt": _ago(60), "expertReply": reply})
            _ = template_feedback  # (kept for parity with live judging)
    for pid, _a, score, _m, _d in history:
        users.set_my(DEMO_UID, pid, {"answered": True, "score": score} if db.get(POSTS, pid)["type"] == "scenario"
                     else {"choice": db.get(POSTS, pid)["answerKey"]})

    quiz = {"id": "quiz-seed-signal", "agentId": "signal", "title": "Road Safety Blitz", "createdAt": _ago(5),
            "questions": _from_cards("signal", random.Random(3))}
    db.put(QUIZZES, quiz["id"], quiz)
    return {"seeded": True, "posts": n_posts, "users": len(db.query(users.USERS))}
