"""
wotnow API (FastAPI) + the built web app (served from STATIC_DIR when present).

  /            web app (React build)
  /api/*       student / parent / admin API        (/docs = interactive docs)
  /jobs/*      scheduled jobs (X-Jobs-Token)
Background: the content pipeline loop keeps posting on schedule (PIPELINE_ENABLED=true).
Security: rate limits, request size limit, security headers, restricted CORS, Google sign-in (AUTH_MODE=google).
"""
from __future__ import annotations

import asyncio
import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from .agents.api import router as agents_router
from .ai.llm import agent_runtime_name, get_llm
from .config import get_settings
from .core import security
from .core.settings import get_platform
from .pipeline import config as pcfg
from .pipeline import scheduler
from .routers import admin, api, auth_api, feed_api, jobs, me_api, pipeline_jobs
from .services import demo as demo_svc
from .services import feed as feedcache

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("wotnow")
s = get_settings()
STATIC_DIR = Path(os.getenv("STATIC_DIR", str(Path(__file__).resolve().parent.parent / "static"))).resolve()
INDEX = STATIC_DIR / "index.html"


@asynccontextmanager
async def lifespan(_: FastAPI):
    ps = get_platform()
    if s.AUTO_SEED:
        from .seed import seed_all
        log.info("seed: %s", await seed_all())
    try:
        n = feedcache.pin_defaults_once()
        if n:
            log.info("pinned %d demo posts so they stay in the feed", n)
        if demo_svc.ensure_demo_defaults():
            log.info("demo student: cleared quiet hours and raised the shared daily limit")
    except Exception as exc:                         # never block startup on a convenience feature
        log.warning("startup tidy-up skipped: %s", exc)
    llm = get_llm()
    log.info("ai provider=%s runtime=%s ready=%s vertex=%s web=%s db=%s auth=%s guests=%s devLogin=%s pipeline=%s",
             llm.name, agent_runtime_name(), llm.available, s.use_vertex, INDEX.exists(), s.DB_BACKEND, ps.auth_mode,
             ps.allow_guests, ps.dev_login_enabled, ps.pipeline_enabled)
    if ps.dev_login and not ps.dev_login_enabled:
        log.warning("DEV_LOGIN is set but ignored: the test sign-in never runs on Cloud Run")
    stop, task = asyncio.Event(), None
    if ps.pipeline_enabled:
        task = asyncio.create_task(scheduler.run_forever(stop))
    yield
    stop.set()
    if task:
        try:
            await asyncio.wait_for(task, timeout=5)
        except Exception:
            task.cancel()


app = FastAPI(title="wotnow API", version=s.VERSION, lifespan=lifespan,
              description="The safe social feed where AI experts post real-life scenarios and students learn by responding.")
_ps = get_platform()
if _ps.cors_origins:
    app.add_middleware(CORSMiddleware, allow_origins=_ps.cors_origins, allow_methods=["*"], allow_headers=["*"])


def _limited(retry: int, msg: str = "Too many requests. Please slow down.") -> JSONResponse:
    return JSONResponse({"detail": msg}, status_code=429, headers={"Retry-After": str(retry)})


@app.middleware("http")
async def guard(request: Request, call_next):
    ps = get_platform()
    path, method = request.url.path, request.method
    if path.startswith(("/api/", "/jobs/")):
        cl = request.headers.get("content-length")
        if cl and cl.isdigit() and int(cl) > ps.max_body_bytes:
            return JSONResponse({"detail": "Request too large"}, status_code=413)
        ip = security.client_ip(request)
        ok, retry = security.limiter.allow(f"all:{ip}", ps.rl_general_per_min, 60)
        if not ok:
            return _limited(retry)
        ident = security.identity_key(request)
        if path.startswith("/api/admin"):
            ok, retry = security.limiter.allow(f"admin:{ident}", ps.rl_admin_per_min, 60)
            if not ok:
                return _limited(retry)
        elif method == "POST" and path.endswith("/answer"):
            ok, retry = security.limiter.allow(f"ans-min:{ident}", ps.rl_answers_per_min, 60)
            if not ok:
                return _limited(retry, "Slow down a little: you're answering very fast.")
            ok, retry = security.limiter.allow(f"ans-day:{ident}", ps.rl_answers_per_day, 86400)
            if not ok:
                return _limited(retry, "Daily answer limit reached. Come back tomorrow! 🌙")
        elif method == "POST" and path.startswith("/api/auth/"):          # Google, test sign-in, refresh, sign-out-everywhere
            ok, retry = security.limiter.allow(f"auth:{ip}", ps.rl_auth_per_min, 60)
            if not ok:
                return _limited(retry)
    resp = await call_next(request)
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("Permissions-Policy", "camera=(), geolocation=(), microphone=(self)")
    if request.url.scheme == "https" or request.headers.get("x-forwarded-proto") == "https":
        resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000")
    if path.startswith("/api/") and "cache-control" not in resp.headers:
        resp.headers["Cache-Control"] = "no-store"
    return resp


# Order matters: for the same method + path the FIRST router wins.
#   feed_api  → GET /api/feed (Today tab, card states)   me_api → POST/DELETE /api/me, POST /api/parent/settings (demo student protected)
app.include_router(feed_api.router)
app.include_router(me_api.router)
app.include_router(api.router)
app.include_router(auth_api.router)
app.include_router(admin.router)
app.include_router(jobs.router)
app.include_router(pipeline_jobs.router)
app.include_router(agents_router)


def _info() -> dict:
    llm, ps = get_llm(), get_platform()
    return {"app": "wotnow", "version": s.VERSION, "llm": s.LLM_PROVIDER, "geminiReady": llm.available,
            "agentRuntime": agent_runtime_name(), "provider": llm.name,
            "model": s.GEMINI_MODEL, "vertex": s.use_vertex, "vertexLocation": s.GOOGLE_CLOUD_LOCATION if s.use_vertex else None,
            "dataMode": s.DATA_MODE, "db": s.DB_BACKEND, "auth": ps.auth_mode, "googleSignIn": ps.google_enabled, "devLogin": ps.dev_login_enabled,
            "guestProfiles": ps.allow_guests,
            "pipeline": {"enabled": ps.pipeline_enabled, "paused": pcfg.load()["paused"]},     # config only: no database scans
            "web": INDEX.exists(), "docs": "/docs", "agents": "/api/ai/agents"}


@app.get("/api/info")
async def api_info():
    return _info()


@app.get("/api/health")
async def api_health():
    return {"ok": True}


@app.get("/healthz", include_in_schema=False)
async def healthz():
    return {"ok": True}


if INDEX.exists():
    NO_CACHE = {"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Expires": "0"}
    LONG_CACHE = {"Cache-Control": "public, max-age=31536000, immutable"}
    RESERVED = ("api/", "jobs/", "docs", "redoc", "openapi.json")

    @app.get("/", include_in_schema=False)
    async def index():
        return FileResponse(INDEX, headers=NO_CACHE)

    @app.get("/{path:path}", include_in_schema=False)
    async def spa(path: str):
        if path.startswith(RESERVED):
            raise HTTPException(404, "Not found")
        f = (STATIC_DIR / path).resolve()
        if f.is_file() and STATIC_DIR in f.parents:
            return FileResponse(f, headers=LONG_CACHE if path.startswith("assets/") else NO_CACHE)
        return FileResponse(INDEX, headers=NO_CACHE)
else:
    @app.get("/")
    async def root():
        return _info()
