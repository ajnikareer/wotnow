"""
wotnow API (FastAPI on Cloud Run) + the built web app (served from STATIC_DIR when present).
AI calls run through Google ADK agents (app/agents) when AGENT_RUNTIME=adk.
Local:  uvicorn app.main:app --reload --port 8080   →  http://localhost:8080/docs
"""
from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from .agents.api import router as agents_router
from .ai.llm import agent_runtime_name, get_llm
from .config import get_settings
from .routers import api, jobs

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
s = get_settings()
STATIC_DIR = Path(os.getenv("STATIC_DIR", str(Path(__file__).resolve().parent.parent / "static"))).resolve()
INDEX = STATIC_DIR / "index.html"


@asynccontextmanager
async def lifespan(_: FastAPI):
    if s.AUTO_SEED:
        from .seed import seed_all
        r = await seed_all()
        logging.getLogger("wotnow").info("seed: %s", r)
    llm = get_llm()
    logging.getLogger("wotnow").info("ai provider=%s runtime=%s ready=%s vertex=%s web=%s",
                                     llm.name, agent_runtime_name(), llm.available, s.use_vertex, INDEX.exists())
    yield


app = FastAPI(title="wotnow API", version=s.VERSION, lifespan=lifespan,
              description="The safe social feed where AI experts post real-life scenarios and students learn by responding.")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(api.router)
app.include_router(jobs.router)
app.include_router(agents_router)


def _info() -> dict:
    llm = get_llm()
    return {"app": "wotnow", "version": s.VERSION, "llm": s.LLM_PROVIDER, "geminiReady": llm.available,
            "agentRuntime": agent_runtime_name(), "provider": llm.name,
            "model": s.GEMINI_MODEL, "vertex": s.use_vertex, "vertexLocation": s.GOOGLE_CLOUD_LOCATION if s.use_vertex else None,
            "dataMode": s.DATA_MODE, "db": s.DB_BACKEND, "auth": s.AUTH_MODE, "web": INDEX.exists(), "docs": "/docs",
            "agents": "/api/ai/agents"}


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
    NO_CACHE = {"Cache-Control": "no-cache"}
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
