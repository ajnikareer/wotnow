"""
The content pipeline: keeps the platform alive with a steady, spread-out flow of new posts, city alerts and live quizzes.

Every PIPELINE_TICK_SECONDS (default 60) tick() looks at the admin-editable schedule (pipeline/config.py) and, if an
expert is "behind" for today, runs the content studio once for that expert: plan → write (ADK writer) → safety review
(ADK reviewer) → validate → dedupe, then publishes it live or into the review queue. Only one worker runs a tick at a
time (database lease). Cloud Scheduler can call POST /jobs/tick instead of (or as well as) the in-app loop.

Cost: an idle tick reads a handful of small documents (per-expert daily counters, state flags) and never scans the posts,
users or traces collections, so it stays cheap on Firestore (billed per document read).
"""
from __future__ import annotations

import asyncio
import hashlib
import logging
import os
import random
import time
import uuid
from typing import Optional

from ..ai.llm import get_llm
from ..core.settings import get_platform
from ..engine import cards as C
from ..engine import dedupe, generator, local_alerts
from ..engine import quiz as quiz_mod
from ..services import clock
from ..services import feed as feedcache
from ..store.base import get_db
from . import config as pcfg

log = logging.getLogger("wotnow.pipeline")
RUNS = "pipeline_runs"
STATE = "pipeline_state"
COUNTS = "pipeline_counts"          # one small document per expert: {day, count} of pipeline posts made today
TRACES = "agent_traces"
LEASE = "pipeline_tick"
LEASE_TTL = 900
CITY_RECHECK_S = 3600               # re-read the users' cities at most this often once today's alerts are done
CITY_RETRY_S = 600                  # …or this often while some city's alert failed


# ---------------- schedule maths ----------------
def slots_for(expert_id: str, cfg: dict) -> list[int]:
    """Minutes-since-midnight at which this expert's posts become due today. Experts are staggered by a stable offset."""
    n = int(cfg["posts_per_expert_per_day"])
    if n <= 0:
        return []
    start, end = pcfg.minutes(cfg["active_start"]), pcfg.minutes(cfg["active_end"])
    frac = (int(hashlib.sha1(expert_id.encode()).hexdigest()[:8], 16) % 1000) / 1000
    return [int(start + (i + frac) * (end - start) / n) for i in range(n)]


def _hhmm(m: int) -> str:
    return f"{m // 60:02d}:{m % 60:02d}"


def _count_from_posts(agent_id: str, today: str) -> int:
    n = 0
    for p in get_db().query(generator.POSTS, agentId=agent_id):
        if p.get("origin") == "pipeline":
            try:
                if clock.local_date_of(p["createdAt"]).isoformat() == today:
                    n += 1
            except Exception:
                continue
    return n


def posts_today(agent_id: str, today: str) -> int:
    """Pipeline posts this expert made on `today` (any status, so admin-rejected posts don't trigger endless regeneration).

    Read from a tiny per-expert counter. If there is none for today (first tick of the day, or right after an upgrade) the
    posts are counted once and the counter is created. Asking about a day other than the current one never writes."""
    db = get_db()
    c = db.get(COUNTS, agent_id)
    if c and c.get("day") == today:
        return int(c.get("count", 0))
    n = _count_from_posts(agent_id, today)
    if today == clock.today().isoformat():
        db.put(COUNTS, agent_id, {"id": agent_id, "day": today, "count": n})
    return n


def schedule_today(cfg: Optional[dict] = None) -> list[dict]:
    cfg = cfg or pcfg.load()
    now = clock.now_local()
    today, now_min = now.date().isoformat(), now.hour * 60 + now.minute
    rows = []
    for a in C.agents():
        on = bool(cfg["experts"].get(a["id"], True))
        slots = slots_for(a["id"], cfg) if on else []
        done = posts_today(a["id"], today)
        due = sum(1 for s in slots if s <= now_min)
        rows.append({"agent": a["id"], "name": a["name"], "enabled": on, "slots": [_hhmm(s) for s in slots],
                     "due": due, "done": done, "behind": max(0, due - done)})
    return rows


# ---------------- one expert, one post ----------------
async def _publish(post: dict, cfg: dict) -> dict:
    db = get_db()
    today = clock.today().isoformat()
    counter = db.get(COUNTS, post["agentId"])
    had_counter = bool(counter and counter.get("day") == today)
    agent_info = C.agent(post["agentId"]) or {}
    needs_approval = bool(cfg.get("approve_first") or agent_info.get("approveFirst", False))
    post["origin"] = "pipeline"
    post["status"] = "pending" if needs_approval else "live"
    if post["status"] == "live":
        post["publishedAt"] = clock.utc_iso()
    db.put(generator.POSTS, post["id"], post)
    if had_counter:
        db.put(COUNTS, post["agentId"], {"id": post["agentId"], "day": today, "count": int(counter.get("count", 0)) + 1})
    else:
        posts_today(post["agentId"], today)         # recounts from the stored posts (this one included) and remembers
    feedcache.invalidate()
    try:
        vec = await get_llm().embed(dedupe.post_text(post))
        dedupe.save_vector(post["id"], post["agentId"], vec)
    except Exception as exc:  # dedupe memory is nice-to-have
        log.warning("could not save embedding for %s: %s", post["id"], exc)
    return post


def _why(a: dict) -> str:
    e = str(a.get("error") or "?")
    iss = a.get("issues")
    return (f"{e} ({'; '.join(map(str, iss))[:70]})" if iss else e)[:110]


async def _generate_for(agent_id: str, cfg: dict, run: dict, kind: Optional[str] = None) -> bool:
    db = get_db()
    kinds = [k for k, on in cfg["formats"].items() if on]
    if not kinds:
        run["errors"].append({"agent": agent_id, "error": "no post formats enabled"})
        return False
    order = [kind] if kind else random.sample(kinds, len(kinds))
    last_attempts: list = []
    for k in order[:3]:
        try:
            res = await generator.generate_one(agent_id, kind=k, publish=False)
        except Exception as exc:
            last_attempts = [{"error": f"{type(exc).__name__}: {str(exc)[:160]}"}]
            continue
        if res.get("ok"):
            post = await _publish(res["post"], cfg)
            run["actions"].append({"type": "post", "agent": agent_id, "postId": post["id"], "kind": post["type"], "status": post["status"],
                                   "source": post.get("source"), "title": post.get("title")})
            db.put(STATE, agent_id, {"id": agent_id, "lastOk": time.time(), "backoffUntil": 0})
            return True
        last_attempts = res.get("attempts", [])
    reasons = "; ".join(_why(a) for a in last_attempts[-3:])
    run["errors"].append({"agent": agent_id, "error": f"could not generate a post: {reasons}"})
    db.put(STATE, agent_id, {"id": agent_id, "lastFail": time.time(), "backoffUntil": time.time() + cfg["failure_backoff_min"] * 60})
    return False


# ---------------- alerts, quizzes, housekeeping ----------------
def _cities() -> list[str]:
    counts: dict[str, int] = {"Pune": 1}
    for u in get_db().query("users"):
        c = (u.get("city") or "").strip()
        if c and len(c) <= 40:
            counts[c] = counts.get(c, 0) + 1
    return [c for c, _ in sorted(counts.items(), key=lambda kv: -kv[1])][:8]


async def _alerts(cfg: dict, run: dict, today: str, now_min: int) -> None:
    if not cfg["alerts_enabled"] or now_min < pcfg.minutes(cfg["alerts_time"]):
        return
    db = get_db()
    st = db.get(STATE, "alerts") or {}
    same_day = st.get("day") == today
    done = set(st.get("cities", [])) if same_day else set()
    wait = CITY_RECHECK_S if st.get("complete") else CITY_RETRY_S
    if same_day and time.time() - st.get("checkedAt", 0) < wait:
        return                                     # don't re-read all users every minute
    failed = False
    for city in _cities():
        if city in done:
            continue
        try:
            p = await local_alerts.build_alert(city)
            run["actions"].append({"type": "alert", "city": city, "postId": p.get("id"), "source": p.get("source")})
            done.add(city)
        except Exception as exc:
            failed = True
            run["errors"].append({"city": city, "error": f"alert failed: {str(exc)[:120]}"})
    if run["actions"]:
        feedcache.invalidate()
    db.put(STATE, "alerts", {"id": "alerts", "day": today, "cities": sorted(done), "complete": not failed, "checkedAt": time.time()})


async def _quizzes(cfg: dict, run: dict, today: str, now_min: int) -> None:
    if not cfg["quizzes_enabled"]:
        return
    due = sum(1 for t in cfg["quiz_times"] if pcfg.minutes(t) <= now_min)
    db = get_db()
    st = db.get(STATE, "quizzes") or {}
    done = int(st.get("done", 0)) if st.get("day") == today else 0
    if due > done:
        try:
            q = await quiz_mod.build_quiz()
            run["actions"].append({"type": "quiz", "quizId": q.get("id"), "title": q.get("title")})
            db.put(STATE, "quizzes", {"id": "quizzes", "day": today, "done": due})
        except Exception as exc:
            run["errors"].append({"error": f"quiz failed: {str(exc)[:120]}"})


def _housekeeping(cfg: dict) -> None:
    """Hourly clean-up that only ever reads the OLDEST few documents (bounded cost, however large the collections grow)."""
    db = get_db()
    st = db.get(STATE, "housekeeping") or {}
    if time.time() - st.get("ts", 0) < 3600:
        return
    cutoff = time.time() - cfg["trace_retention_days"] * 86400
    for t in db.query_ex(TRACES, order_by="ts", desc=False, limit=200):
        if t.get("ts", 0) < cutoff:
            db.delete(TRACES, t["id"])
    keep = int(cfg["run_retention"])
    runs = db.query_ex(RUNS, order_by="ts", desc=True, limit=keep + 200)     # trims up to 200 surplus runs per hour
    for r in runs[keep:]:
        db.delete(RUNS, r["id"])
    db.put(STATE, "housekeeping", {"id": "housekeeping", "ts": time.time()})


# ---------------- the tick ----------------
async def tick(*, source: str = "scheduler", force_agents: Optional[list[str]] = None, force_kind: Optional[str] = None) -> dict:
    cfg = pcfg.load()
    if source != "admin" and (not cfg["enabled"] or cfg["paused"]):
        return {"skipped": "paused" if cfg["paused"] else "disabled"}
    db = get_db()
    owner = f"{os.getpid()}-{uuid.uuid4().hex[:6]}"
    if not db.acquire_lease(LEASE, owner, LEASE_TTL):
        return {"skipped": "another worker is running"}
    t0 = time.perf_counter()
    run = {"id": f"{clock.utc_iso()}-{uuid.uuid4().hex[:4]}", "ts": clock.utc_iso(), "source": source, "actions": [], "errors": []}
    try:
        now = clock.now_local()
        today, now_min = now.date().isoformat(), now.hour * 60 + now.minute
        if force_agents is not None:
            for aid in force_agents:
                if C.agent(aid):
                    await _generate_for(aid, cfg, run, force_kind)
        else:
            cands = []
            for row in schedule_today(cfg):
                if row["enabled"] and row["behind"] > 0:
                    cands.append((row["behind"], row["agent"]))
            cands.sort(key=lambda x: (-x[0], x[1]))
            pending = 0
            if cands and cfg["approve_first"]:      # only needed (and only read, capped) when posts wait for approval
                pending = len(db.query_ex(generator.POSTS, {"status": "pending"}, limit=cfg["max_pending"] + 1))
            attempts = 0
            for _behind, aid in cands:
                if attempts >= cfg["max_per_tick"]:
                    break
                if (db.get(STATE, aid) or {}).get("backoffUntil", 0) > time.time():
                    continue
                if cfg["approve_first"] and pending >= cfg["max_pending"]:
                    run["errors"].append({"error": f"review queue is full ({pending} pending): approve or reject posts to continue"})
                    break
                attempts += 1
                if await _generate_for(aid, cfg, run):
                    pending += 1 if cfg["approve_first"] else 0
            await _alerts(cfg, run, today, now_min)
            await _quizzes(cfg, run, today, now_min)
        _housekeeping(cfg)
    finally:
        db.release_lease(LEASE, owner)
        run["ms"] = round((time.perf_counter() - t0) * 1000)
        db.put(STATE, "heartbeat", {"id": "heartbeat", "ts": time.time(), "at": clock.utc_iso(), "source": source})
        if run["actions"] or run["errors"] or source == "admin":
            db.put(RUNS, run["id"], run)
    return run


async def generate_now(agent_ids: Optional[list[str]] = None, kind: Optional[str] = None) -> dict:
    """Admin 'run now': generate immediately for the given experts (default: every enabled expert), ignoring the daily schedule."""
    cfg = pcfg.load()
    ids = agent_ids or [a["id"] for a in C.agents() if cfg["experts"].get(a["id"], True)]
    return await tick(source="admin", force_agents=ids, force_kind=kind)


def status() -> dict:
    db = get_db()
    hb = db.get(STATE, "heartbeat") or {}
    last = db.query_ex(RUNS, order_by="ts", desc=True, limit=1)
    cfg = pcfg.load()
    return {"enabled": cfg["enabled"] and get_platform().pipeline_enabled, "paused": cfg["paused"], "lastTickAt": hb.get("at"),
            "tickSeconds": get_platform().pipeline_tick_seconds, "lastRun": last[0] if last else None,
            "pending": db.count(generator.POSTS, status="pending")}


async def run_forever(stop: asyncio.Event) -> None:
    ps = get_platform()
    log.info("content pipeline loop started (every %ss)", ps.pipeline_tick_seconds)
    try:
        await asyncio.wait_for(stop.wait(), timeout=20)   # let the server settle first
        return
    except asyncio.TimeoutError:
        pass
    while not stop.is_set():
        try:
            r = await tick()
            if r.get("actions") or r.get("errors"):
                log.info("pipeline tick: %d actions, %d errors", len(r["actions"]), len(r["errors"]))
        except Exception as exc:
            log.exception("pipeline tick crashed: %s", exc)
        try:
            await asyncio.wait_for(stop.wait(), timeout=ps.pipeline_tick_seconds)
        except asyncio.TimeoutError:
            pass
