"""
Admin API (/api/admin/*): control the agents, skills, guardrails, content pipeline, review queue, fact cards and evaluations.
Access: a Google session whose verified email is in ADMIN_EMAILS, or header X-Admin-Token (the jobs token).
Every change is validated, versioned (core/overrides) and written to the audit log. Nothing here needs a redeploy.
"""
from __future__ import annotations

import asyncio
import re
import time
from typing import Any, Optional

from fastapi import APIRouter, Body, Depends, HTTPException

from ..agents import config as acfg
from ..agents.evals import service as evals
from ..agents.factory import AgentFactory
from ..ai.llm import agent_runtime_name, get_llm
from ..auth import require_admin
from ..config import get_settings
from ..core import audit, overrides
from ..core.settings import get_platform
from ..engine import cards as C
from ..engine.generator import POSTS
from ..pipeline import config as pcfg
from ..pipeline import scheduler
from ..services import clock, users
from ..store.base import get_db

router = APIRouter(prefix="/api/admin", tags=["admin"])
STARTED = time.time()
STATUSES = ("live", "pending", "unpublished", "rejected")
_bg: set = set()


def _bad(msg: str) -> HTTPException:
    return HTTPException(400, msg)


# =============================================================== overview
@router.get("/overview")
async def overview(actor: str = Depends(require_admin)):
    db = get_db()
    posts = db.query(POSTS)
    by_status: dict[str, int] = {}
    for p in posts:
        by_status[p.get("status", "live")] = by_status.get(p.get("status", "live"), 0) + 1
    today = clock.today().isoformat()
    made_today = 0
    for p in posts:
        if p.get("origin") == "pipeline":
            try:
                made_today += clock.local_date_of(p["createdAt"]).isoformat() == today
            except Exception:
                pass
    cutoff = time.time() - 86400
    traces = [t for t in db.query_ex(scheduler.TRACES, order_by="ts", desc=True, limit=1000) if t.get("ts", 0) >= cutoff]
    skills: dict[str, dict] = {}
    for t in traces:
        s = skills.setdefault(t["skill"], {"runs": 0, "ok": 0, "blocked": 0, "errors": 0, "ms": 0})
        s["runs"] += 1
        s["ok"] += 1 if t.get("ok") else 0
        s["blocked"] += 1 if t.get("blocked") else 0
        s["errors"] += 1 if t.get("error") else 0
        s["ms"] += t.get("ms", 0)
    for s in skills.values():
        s["avgMs"] = round(s.pop("ms") / s["runs"]) if s["runs"] else 0
    llm = get_llm()
    st = get_settings()
    return {"app": "wotnow", "version": st.VERSION, "uptimeS": round(time.time() - STARTED), "actor": actor, "now": clock.now_local().isoformat(timespec="seconds"),
            "timezone": st.TIMEZONE, "ai": {"provider": llm.name, "runtime": agent_runtime_name(), "geminiReady": llm.available, "model": st.GEMINI_MODEL, "vertex": st.use_vertex},
            "db": db.name, "authMode": get_platform().auth_mode, "posts": {"byStatus": by_status, "total": len(posts), "madeByPipelineToday": made_today},
            "people": {"students": db.count("users"), "accounts": db.count("accounts")},
            "agentRuns24h": {"total": len(traces), "bySkill": skills}, "pipeline": scheduler.status(),
            "reviewedOnly": C.reviewed_only(), "cards": {"total": len(C.all_cards_admin()), "reviewed": sum(1 for c in C.all_cards_admin() if c.get("reviewed"))}}


# =============================================================== pipeline
def _pipeline_payload() -> dict:
    cfg = pcfg.load()
    base = pcfg.defaults()
    ov = overrides.get(pcfg.KEY) or {}
    return {"config": cfg, "defaults": base, "overridden": sorted(ov.keys()), "status": scheduler.status(), "schedule": scheduler.schedule_today(cfg),
            "now": clock.now_local().strftime("%H:%M"), "timezone": get_settings().TIMEZONE, "formats": list(pcfg.FORMATS),
            "experts": [{"id": a["id"], "name": a["name"], "domain": a["domainLabel"], "emoji": a["emoji"]} for a in C.agents()]}


@router.get("/pipeline")
async def get_pipeline(actor: str = Depends(require_admin)):
    return _pipeline_payload()


@router.put("/pipeline")
async def put_pipeline(patch: dict = Body(...), actor: str = Depends(require_admin)):
    try:
        pcfg.save(patch, actor)
    except ValueError as e:
        raise _bad(str(e))
    audit.log(actor, "pipeline.update", "pipeline", patch)
    return _pipeline_payload()


@router.post("/pipeline/reset")
async def reset_pipeline(actor: str = Depends(require_admin)):
    pcfg.reset(actor)
    audit.log(actor, "pipeline.reset", "pipeline")
    return _pipeline_payload()


@router.post("/pipeline/pause")
async def pause_pipeline(body: dict = Body(...), actor: str = Depends(require_admin)):
    paused = bool(body.get("paused", True))
    pcfg.save({"paused": paused}, actor)
    audit.log(actor, "pipeline.pause" if paused else "pipeline.resume", "pipeline")
    return _pipeline_payload()


@router.post("/pipeline/run-now")
async def run_now(body: dict = Body(default={}), actor: str = Depends(require_admin)):
    agents = body.get("agents")
    kind = body.get("kind")
    if agents is not None and (not isinstance(agents, list) or any(not C.agent(a) for a in agents)):
        raise _bad("agents must be a list of expert ids")
    if kind is not None and kind not in pcfg.FORMATS:
        raise _bad(f"kind must be one of {', '.join(pcfg.FORMATS)}")
    lease = get_db().get("locks", scheduler.LEASE)
    if lease and lease.get("expires", 0) > time.time():
        raise HTTPException(409, "A pipeline run is already in progress")
    t = asyncio.create_task(scheduler.generate_now(agents, kind))
    _bg.add(t)
    t.add_done_callback(_bg.discard)
    audit.log(actor, "pipeline.run_now", ",".join(agents or ["all"]), {"kind": kind})
    return {"started": True, "agents": agents or [a["id"] for a in C.agents() if pcfg.load()["experts"].get(a["id"], True)]}


@router.get("/pipeline/runs")
async def pipeline_runs(limit: int = 20, actor: str = Depends(require_admin)):
    return {"runs": get_db().query_ex(scheduler.RUNS, order_by="ts", desc=True, limit=max(1, min(limit, 200)))}


# =============================================================== posts / review queue
def _post_row(p: dict, full: bool = False) -> dict:
    row = {k: p.get(k) for k in ("id", "agentId", "type", "title", "status", "origin", "source", "createdAt", "publishedAt", "city", "bands", "sourceCards", "stats")}
    row["quality"] = p.get("quality")
    row["status"] = row["status"] or "live"
    if full:
        row.update({k: p.get(k) for k in ("body", "question", "statement", "message", "options", "answerKey", "explanation", "rubric", "dangerousActions",
                                          "modelAnswer", "scene", "chips", "steps", "combo", "voteCounts")})
    return row


@router.get("/posts")
async def list_posts(status: Optional[str] = None, agent: Optional[str] = None, type: Optional[str] = None, origin: Optional[str] = None,
                     limit: int = 50, offset: int = 0, actor: str = Depends(require_admin)):
    rows = get_db().query(POSTS)
    rows = [p for p in rows if (not status or p.get("status", "live") == status) and (not agent or p.get("agentId") == agent)
            and (not type or p.get("type") == type) and (not origin or p.get("origin", "seed") == origin)]
    rows.sort(key=lambda p: p.get("createdAt", ""), reverse=True)
    return {"total": len(rows), "posts": [_post_row(p) for p in rows[max(0, offset): max(0, offset) + max(1, min(limit, 200))]]}


@router.get("/posts/{post_id}")
async def get_post(post_id: str, actor: str = Depends(require_admin)):
    p = get_db().get(POSTS, post_id)
    if not p:
        raise HTTPException(404, "post not found")
    return _post_row(p, full=True)


@router.post("/posts/{post_id}/status")
async def set_status(post_id: str, body: dict = Body(...), actor: str = Depends(require_admin)):
    status = body.get("status")
    if status not in STATUSES:
        raise _bad(f"status must be one of {', '.join(STATUSES)}")
    db = get_db()
    p = db.get(POSTS, post_id)
    if not p:
        raise HTTPException(404, "post not found")
    prev = p.get("status", "live")
    p["status"] = status
    if status == "live" and prev != "live":
        p["publishedAt"] = clock.utc_iso()
    p["reviewedBy"] = actor
    db.put(POSTS, post_id, p)
    audit.log(actor, "post.status", post_id, {"from": prev, "to": status})
    return _post_row(p)


# =============================================================== agents & skills
def _instructions_view() -> list[dict]:
    cat = AgentFactory().catalogue()
    out = []
    for f in acfg.instruction_files():
        out.append({"file": f, "text": acfg.instruction(f), "default": acfg.default_instruction(f), "overridden": overrides.get(f"instr:{f}") is not None,
                    "usedBy": [c["skill"] for c in cat if c["instructionFile"] == f]})
    return out


def _agents_payload() -> dict:
    return {"runtime": agent_runtime_name(), "provider": get_llm().name, "placeholders": list(acfg.INSTRUCTION_PLACEHOLDERS),
            "experts": [{"id": a["id"], "name": a["name"], "domain": a["domainLabel"], "emoji": a["emoji"], "persona": a.get("persona", ""),
                         "cards": len(C.cards_for(a["id"]))} for a in C.agents()],
            "skills": AgentFactory().catalogue(), "instructions": _instructions_view(), "version": overrides.version()}


@router.get("/agents")
async def get_agents(actor: str = Depends(require_admin)):
    return _agents_payload()


@router.put("/agents/skills/{skill}")
async def put_skill(skill: str, body: dict = Body(...), actor: str = Depends(require_admin)):
    dreg = acfg.default_registry()["skills"]
    if skill not in dreg:
        raise HTTPException(404, "unknown skill")
    dflt = {**acfg.default_registry()["defaults"], **dreg[skill]}
    cur = dict(overrides.get(f"skill:{skill}") or {})
    for k, v in body.items():
        if k not in acfg.SKILL_PARAMS:
            raise _bad(f"unknown setting '{k}'")
        if k == "temperature":
            try:
                v = float(v)
            except (TypeError, ValueError):
                raise _bad("temperature must be a number")
            if not 0 <= v <= 2:
                raise _bad("temperature must be between 0 and 2")
        elif k == "timeout_s":
            try:
                v = int(v)
            except (TypeError, ValueError):
                raise _bad("timeout_s must be a whole number")
            if not 5 <= v <= 300:
                raise _bad("timeout_s must be between 5 and 300")
        elif k == "review":
            if "review" not in dreg[skill]:
                raise _bad("this skill has no review step option")
            v = bool(v)
        else:
            v = bool(v)
        if v == dflt.get(k):
            cur.pop(k, None)
        else:
            cur[k] = v
    if cur:
        overrides.put(f"skill:{skill}", cur, actor)
    else:
        overrides.delete(f"skill:{skill}", actor)
    audit.log(actor, "agent.skill", skill, body)
    return _agents_payload()


@router.delete("/agents/skills/{skill}")
async def reset_skill(skill: str, actor: str = Depends(require_admin)):
    overrides.delete(f"skill:{skill}", actor)
    audit.log(actor, "agent.skill.reset", skill)
    return _agents_payload()


def validate_instruction(text: str) -> str:
    text = (text or "").strip()
    if not 20 <= len(text) <= 6000:
        raise _bad("instruction must be between 20 and 6000 characters")
    allowed = set(acfg.INSTRUCTION_PLACEHOLDERS)
    for m in re.findall(r"\{([^{}]*)\}", text):
        if m not in allowed:
            raise _bad(f"unknown placeholder {{{m}}}. Allowed: " + ", ".join("{" + a + "}" for a in acfg.INSTRUCTION_PLACEHOLDERS))
    stripped = re.sub(r"\{(?:%s)\}" % "|".join(allowed), "", text)
    if "{" in stripped or "}" in stripped:
        raise _bad("curly braces are reserved for placeholders; remove stray { or } characters")
    return text


@router.put("/agents/instructions/{file}")
async def put_instruction(file: str, body: dict = Body(...), actor: str = Depends(require_admin)):
    if file not in acfg.instruction_files():
        raise HTTPException(404, "unknown instruction file")
    text = validate_instruction(body.get("text", ""))
    if text == acfg.default_instruction(file):
        overrides.delete(f"instr:{file}", actor)
    else:
        overrides.put(f"instr:{file}", {"text": text}, actor)
    audit.log(actor, "agent.instruction", file, {"chars": len(text)})
    return _agents_payload()


@router.delete("/agents/instructions/{file}")
async def reset_instruction(file: str, actor: str = Depends(require_admin)):
    overrides.delete(f"instr:{file}", actor)
    audit.log(actor, "agent.instruction.reset", file)
    return _agents_payload()


@router.get("/config-history")
async def config_history(key: str, actor: str = Depends(require_admin)):
    return {"key": key, "history": overrides.history(key)}


# =============================================================== guardrails
def _guardrails_payload() -> dict:
    ov = overrides.get("rules") or {}
    return {"effective": acfg.rules(), "defaults": acfg.default_rules(), "overridden": sorted(ov.keys())}


def _clean_patterns(d: Any, name: str) -> dict:
    if not isinstance(d, dict) or len(d) > 12:
        raise _bad(f"{name} must be an object with at most 12 patterns")
    out = {}
    for k, v in d.items():
        if not re.match(r"^[A-Za-z0-9_]{1,30}$", str(k)) or not isinstance(v, str) or not 1 <= len(v) <= 400:
            raise _bad(f"{name}: names must be simple words and patterns 1-400 characters")
        try:
            re.compile(v)
        except re.error as e:
            raise _bad(f"{name}.{k}: invalid regular expression ({e})")
        out[k] = v
    return out


def _clean_list(v: Any, name: str, max_items: int, max_len: int) -> list:
    if not isinstance(v, list) or not 1 <= len(v) <= max_items or any(not isinstance(x, str) or not x.strip() or len(x) > max_len for x in v):
        raise _bad(f"{name} must be a list of 1-{max_items} non-empty texts (max {max_len} characters each)")
    return [x.strip() for x in v]


@router.get("/guardrails")
async def get_guardrails(actor: str = Depends(require_admin)):
    return _guardrails_payload()


@router.put("/guardrails")
async def put_guardrails(body: dict = Body(...), actor: str = Depends(require_admin)):
    dflt = acfg.default_rules()
    cur = dict(overrides.get("rules") or {})
    for k, v in body.items():
        if k not in acfg.RULE_KEYS:
            raise _bad(f"unknown guardrail setting '{k}'")
        if k == "policy":
            v = _clean_list(v, k, 20, 300)
        elif k == "allowed_numbers":
            v = _clean_list(v, k, 12, 10)
            if any(not x.isdigit() for x in v):
                raise _bad("allowed_numbers must be digits only")
        elif k == "injection_markers":
            v = _clean_list(v, k, 30, 80)
        elif k in ("blocked_output_patterns", "pii_patterns"):
            v = _clean_patterns(v, k)
        elif k == "max_input_chars":
            try:
                v = int(v)
            except (TypeError, ValueError):
                raise _bad("max_input_chars must be a number")
            if not 1000 <= v <= 50000:
                raise _bad("max_input_chars must be between 1000 and 50000")
        if v == dflt.get(k):
            cur.pop(k, None)
        else:
            cur[k] = v
    if cur:
        overrides.put("rules", cur, actor)
    else:
        overrides.delete("rules", actor)
    audit.log(actor, "guardrails.update", "rules", {k: "(changed)" for k in body})
    return _guardrails_payload()


@router.delete("/guardrails")
async def reset_guardrails(actor: str = Depends(require_admin)):
    overrides.delete("rules", actor)
    audit.log(actor, "guardrails.reset", "rules")
    return _guardrails_payload()


@router.post("/guardrails/test")
async def test_guardrails(body: dict = Body(...), actor: str = Depends(require_admin)):
    """Dry-run the current guardrails on a piece of text (no model call)."""
    text = str(body.get("text", ""))[:4000]
    r = acfg.rules()
    blocked = [k for k, rx in r["blocked_output_patterns"].items() if re.search(rx, text, re.I)]
    scrubbed = text
    for kind, rx in r["pii_patterns"].items():
        scrubbed = re.sub(rx, f"[{kind} removed]", scrubbed)
    low = text.lower()
    return {"blockedOutput": blocked, "wouldBlock": bool(blocked), "scrubbedInput": scrubbed, "injectionSuspected": any(m.lower() in low for m in r["injection_markers"])}


# =============================================================== fact cards
def _card_row(c: dict) -> dict:
    return {"id": c["id"], "agentId": c["agentId"], "title": c.get("title"), "subtopic": c.get("subtopic"), "bands": c.get("bands"),
            "facts": c.get("facts", []), "do": c.get("do", []), "dont": c.get("dont", []), "reviewed": bool(c.get("reviewed")),
            "disabled": bool(c.get("disabled")), "edited": bool(c.get("edited")), "reviewedBy": c.get("reviewedBy"), "reviewedAt": c.get("reviewedAt"),
            "hasScenario": bool(c.get("scenario")), "quizItems": len(c.get("quiz", [])), "myths": len(c.get("myths", [])), "scams": len(c.get("scams", []))}


@router.get("/cards")
async def list_cards(agent: Optional[str] = None, actor: str = Depends(require_admin)):
    rows = [_card_row(c) for c in C.all_cards_admin() if not agent or c["agentId"] == agent]
    return {"reviewedOnly": C.reviewed_only(), "cards": rows}


@router.put("/cards/{card_id}")
async def put_card(card_id: str, body: dict = Body(...), actor: str = Depends(require_admin)):
    base = C.base_card(card_id)
    if not base:
        raise HTTPException(404, "card not found")
    cur = dict(overrides.get(f"card:{card_id}") or {})
    for k, v in body.items():
        if k in C.EDITABLE_LISTS:
            v = _clean_list(v, k, 40, 400)
        elif k == "title":
            if not isinstance(v, str) or not 3 <= len(v.strip()) <= 80:
                raise _bad("title must be 3-80 characters")
            v = v.strip()
        elif k in ("reviewed", "disabled"):
            v = bool(v)
        elif k == "reviewNote":
            v = str(v)[:300]
        else:
            raise _bad(f"unknown field '{k}'")
        cur[k] = v
    if body.get("reviewed") is True:
        cur["reviewedBy"], cur["reviewedAt"] = actor, time.strftime("%Y-%m-%d", time.gmtime())
    if body.get("reviewed") is False:
        cur.pop("reviewedBy", None), cur.pop("reviewedAt", None)
    for k in list(cur):    # drop values identical to the shipped card (reviewed defaults to the shipped flag)
        if k in base and cur[k] == base[k]:
            cur.pop(k)
    if cur:
        overrides.put(f"card:{card_id}", cur, actor)
    else:
        overrides.delete(f"card:{card_id}", actor)
    audit.log(actor, "card.update", card_id, {k: ("(text)" if k in C.EDITABLE_LISTS else v) for k, v in body.items()})
    return _card_row(C.card(card_id))


@router.delete("/cards/{card_id}")
async def reset_card(card_id: str, actor: str = Depends(require_admin)):
    if not C.base_card(card_id):
        raise HTTPException(404, "card not found")
    overrides.delete(f"card:{card_id}", actor)
    audit.log(actor, "card.reset", card_id)
    return _card_row(C.card(card_id))


# =============================================================== evaluations
@router.get("/evals")
async def get_evals(actor: str = Depends(require_admin)):
    cases = evals.load_cases()
    return {"scenarios": cases["scenarios"], "cases": cases["cases"], "customised": overrides.get(evals.KEY) is not None,
            "runs": evals.recent_runs(10), "aiMode": get_llm().name}


@router.put("/evals/cases")
async def put_eval_cases(body: dict = Body(...), actor: str = Depends(require_admin)):
    try:
        clean = evals.validate_cases(body)
    except ValueError as e:
        raise _bad(str(e))
    overrides.put(evals.KEY, clean, actor)
    audit.log(actor, "evals.cases", "judge", {"cases": len(clean["cases"])})
    return await get_evals(actor)


@router.delete("/evals/cases")
async def reset_eval_cases(actor: str = Depends(require_admin)):
    overrides.delete(evals.KEY, actor)
    return await get_evals(actor)


@router.post("/evals/run")
async def run_evals(actor: str = Depends(require_admin)):
    run_id = evals.start(actor)
    audit.log(actor, "evals.run", run_id)
    return {"runId": run_id}


@router.get("/evals/runs/{run_id}")
async def get_eval_run(run_id: str, actor: str = Depends(require_admin)):
    r = evals.get_run(run_id)
    if not r:
        raise HTTPException(404, "run not found")
    return r


# =============================================================== traces, people, audit
@router.get("/traces")
async def traces(skill: Optional[str] = None, ok: Optional[bool] = None, limit: int = 100, actor: str = Depends(require_admin)):
    limit = max(1, min(limit, 500))
    rows = get_db().query_ex(scheduler.TRACES, order_by="ts", desc=True, limit=limit * 4)
    rows = [t for t in rows if (not skill or t.get("skill") == skill) and (ok is None or bool(t.get("ok")) == ok)]
    return {"traces": rows[:limit]}


@router.get("/people")
async def people(actor: str = Depends(require_admin)):
    db = get_db()
    students = db.query("users")
    accounts = db.query("accounts")
    top = sorted(students, key=lambda u: u.get("xp", 0), reverse=True)[:10]
    return {"students": len(students), "accounts": len(accounts),
            "byBand": {b: sum(1 for u in students if u.get("band") == b) for b in ("junior", "middle", "senior")},
            "top": [{"nickname": u.get("nickname"), "xp": u.get("xp", 0), "grade": u.get("grade"), "city": u.get("city")} for u in top],
            "accountsList": [{"email": a.get("email"), "name": a.get("name"), "children": len(a.get("children", [])), "lastLogin": a.get("lastLogin")}
                             for a in sorted(accounts, key=lambda a: a.get("lastLogin", ""), reverse=True)[:200]]}


@router.get("/audit")
async def get_audit(limit: int = 100, actor: str = Depends(require_admin)):
    return {"audit": audit.recent(max(1, min(limit, 500)))}


@router.post("/clean-seed-users")
async def clean_seed_users(actor: str = Depends(require_admin)):
    db = get_db()
    all_users = db.query("users")
    deleted = []
    for u in all_users:
        uid = u.get("id", "")
        if uid.startswith("seed-") or uid.startswith("demo-") or u.get("source") == "seed":
            users.delete_user(uid)
            deleted.append(uid)
    return {"deletedCount": len(deleted), "deleted": deleted}


@router.post("/clean-post-stats")
async def clean_post_stats(actor: str = Depends(require_admin)):
    db = get_db()
    posts = db.query(POSTS)
    fixed = 0
    for p in posts:
        stats = p.get("stats") or {}
        changed = False
        if stats.get("responses", 0) > 50:
            stats["responses"] = 0
            p["stats"] = stats
            changed = True
        if "voteCounts" in p and any(v > 50 for v in p["voteCounts"].values()):
            p["voteCounts"] = {k: 0 for k in p["voteCounts"]}
            changed = True
        if p.get("pinned"):
            p.pop("pinned", None)
            changed = True
        if changed:
            db.put(POSTS, p["id"], p)
            fixed += 1
    return {"fixedCount": fixed}


