"""Weekly leaderboards: my class, my school (+ class teams), schools in my city. Nicknames only."""
from __future__ import annotations

from collections import defaultdict

from ..store.base import get_db
from . import clock
from .users import USERS


def _wxp(u: dict, wk: str) -> int:
    return (u.get("weekXp") or {}).get(wk, 0)


def _rank(rows: list[dict]) -> list[dict]:
    rows.sort(key=lambda r: r["xp"], reverse=True)
    for i, r in enumerate(rows):
        r["rank"] = i + 1
    return rows


def board(me: dict, scope: str) -> dict:
    wk = clock.week_id()
    everyone = get_db().query(USERS)
    if scope == "class":
        pool = [u for u in everyone if u.get("school") == me.get("school") and u.get("className") == me.get("className")]
        rows = _rank([{"nickname": u["nickname"], "avatar": u["avatar"], "xp": _wxp(u, wk), "me": u["id"] == me["id"], "_id": u["id"]} for u in pool])
    elif scope == "school":
        pool = [u for u in everyone if u.get("school") == me.get("school")]
        rows = _rank([{"nickname": u["nickname"], "avatar": u["avatar"], "xp": _wxp(u, wk), "sub": u.get("className"), "me": u["id"] == me["id"], "_id": u["id"]} for u in pool])
    else:
        by_school = defaultdict(int)
        for u in everyone:
            if u.get("city") == me.get("city") and u.get("school"):
                by_school[u["school"]] += _wxp(u, wk)
        rows = _rank([{"nickname": s, "avatar": "🏫", "xp": x, "me": s == me.get("school")} for s, x in by_school.items()])
    mine = next((r for r in rows if r.get("me")), {"rank": len(rows) + 1, "nickname": me["nickname"], "avatar": me["avatar"], "xp": _wxp(me, wk), "me": True})
    out = {"scope": scope, "rows": [{k: v for k, v in r.items() if k != "_id"} for r in rows[:10]], "me": {k: v for k, v in mine.items() if k != "_id"}}
    if scope == "school":
        teams = defaultdict(int)
        for u in everyone:
            if u.get("school") == me.get("school") and u.get("className"):
                teams[u["className"]] += _wxp(u, wk)
        out["teams"] = _rank([{"nickname": c, "avatar": "🏆" if i == 0 else "🎯", "xp": x, "me": c == me.get("className")}
                              for i, (c, x) in enumerate(sorted(teams.items(), key=lambda kv: -kv[1]))])[:6]
    return out
