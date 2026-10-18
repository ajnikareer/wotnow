"""Weekly and all-time leaderboards: Global, Country, City. Real users and nicknames only."""
from __future__ import annotations

from ..store.base import get_db
from . import clock
from .users import USERS


def _user_xp(u: dict, wk: str) -> int:
    """Returns user XP for ranking. Prioritize active week XP, falling back to total XP."""
    wx = (u.get("weekXp") or {}).get(wk, 0)
    return max(wx, u.get("xp", 0))


def _is_real_user(u: dict, me_id: str) -> bool:
    uid = u.get("id", "")
    if uid and uid == me_id:
        return True
    if uid.startswith("seed-") or uid.startswith("demo-") or u.get("source") == "seed":
        return False
    return True


def _rank(rows: list[dict]) -> list[dict]:
    # Sort by XP descending, then by answers count descending, then nickname
    rows.sort(key=lambda r: (r["xp"], r.get("answers", 0), r.get("nickname", "")), reverse=True)
    for i, r in enumerate(rows):
        r["rank"] = i + 1
    return rows


def board(me: dict, scope: str) -> dict:
    wk = clock.week_id()
    # Map legacy scopes if any old client asks
    if scope in ("class", "school"):
        scope = "country" if scope == "school" else "city"
    if scope not in ("global", "country", "city"):
        scope = "global"

    my_city = (me.get("city") or "Pune").strip()
    my_country = (me.get("country") or "India").strip()

    everyone = [u for u in get_db().query(USERS) if _is_real_user(u, me.get("id", ""))]

    if scope == "city":
        pool = [
            u for u in everyone
            if (u.get("city") or "Pune").strip().lower() == my_city.lower()
        ]
        rows = _rank([
            {
                "nickname": u.get("nickname", "Learner"),
                "avatar": u.get("avatar", "🦊"),
                "xp": _user_xp(u, wk),
                "sub": f"Class {u.get('grade', 8)}",
                "city": u.get("city", my_city),
                "country": u.get("country", my_country),
                "answers": u.get("answers", 0),
                "me": u.get("id") == me.get("id"),
                "_id": u.get("id"),
            }
            for u in pool
        ])
    elif scope == "country":
        pool = [
            u for u in everyone
            if (u.get("country") or "India").strip().lower() == my_country.lower()
        ]
        rows = _rank([
            {
                "nickname": u.get("nickname", "Learner"),
                "avatar": u.get("avatar", "🦊"),
                "xp": _user_xp(u, wk),
                "sub": u.get("city") or my_city,
                "city": u.get("city", my_city),
                "country": u.get("country", my_country),
                "answers": u.get("answers", 0),
                "me": u.get("id") == me.get("id"),
                "_id": u.get("id"),
            }
            for u in pool
        ])
    else:  # global
        rows = _rank([
            {
                "nickname": u.get("nickname", "Learner"),
                "avatar": u.get("avatar", "🦊"),
                "xp": _user_xp(u, wk),
                "sub": f"{u.get('city') or my_city}, {u.get('country') or my_country}",
                "city": u.get("city", my_city),
                "country": u.get("country", my_country),
                "answers": u.get("answers", 0),
                "me": u.get("id") == me.get("id"),
                "_id": u.get("id"),
            }
            for u in everyone
        ])

    mine = next(
        (r for r in rows if r.get("me")),
        {
            "rank": len(rows) + 1,
            "nickname": me.get("nickname", "Learner"),
            "avatar": me.get("avatar", "🦊"),
            "xp": _user_xp(me, wk),
            "sub": f"{my_city}, {my_country}" if scope == "global" else (my_city if scope == "country" else f"Class {me.get('grade', 8)}"),
            "city": my_city,
            "country": my_country,
            "me": True,
        }
    )

    clean_rows = [{k: v for k, v in r.items() if k != "_id"} for r in rows[:25]]
    clean_mine = {k: v for k, v in mine.items() if k != "_id"}

    return {
        "scope": scope,
        "rows": clean_rows,
        "me": clean_mine,
        "myCity": my_city,
        "myCountry": my_country,
        "totalLearners": len(rows),
    }
