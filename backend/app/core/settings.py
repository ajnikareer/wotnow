"""Platform settings that sit next to the v1 config: auth, security, pipeline switches. All from environment variables."""
from __future__ import annotations

import hashlib
import logging
import os
from dataclasses import dataclass, field
from functools import lru_cache

log = logging.getLogger("wotnow.core")


def _b(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


def _i(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


@dataclass
class PlatformSettings:
    auth_mode: str = "dev"                  # dev = demo/test identities · google = Google sign-in (+ the demo student if ALLOW_DEMO)
    allow_demo: bool = True                 # "Try the student demo": the one shared, read-mostly demo student
    allow_guests: bool = True               # arbitrary guest profiles through the X-Demo-User header (dev only; OFF with Google)
    dev_login: bool = False                 # test-only "sign in with any email" (never on Cloud Run, see dev_login_enabled)
    on_cloud_run: bool = False              # K_SERVICE is set by Cloud Run
    google_client_id: str = ""
    session_secret: str = ""
    session_ttl_days: int = 14
    admin_emails: frozenset = field(default_factory=frozenset)
    admin_token_login: bool = True          # allow the jobs token as an admin password (handy on the build-host)
    cors_origins: list = field(default_factory=list)
    trust_proxy: bool = False               # read client IP from X-Forwarded-For (only behind your own LB / Cloud Run)
    max_body_bytes: int = 65536
    rl_general_per_min: int = 240
    rl_answers_per_min: int = 12
    rl_answers_per_day: int = 150
    rl_auth_per_min: int = 20
    rl_admin_per_min: int = 180
    pipeline_enabled: bool = True
    pipeline_tick_seconds: int = 60
    llm_concurrency: int = 6
    max_children: int = 3
    feed_cache_ttl_s: int = 20              # how long the "newest posts" window is cached in memory (0 = off)
    overrides_ttl_s: int = 10               # how often admin-edited settings are re-read from the database

    @property
    def google_enabled(self) -> bool:
        return self.auth_mode == "google" and bool(self.google_client_id)

    @property
    def dev_login_enabled(self) -> bool:
        """The test sign-in exists only when asked for AND never on Cloud Run, whatever the environment says."""
        return self.dev_login and not self.on_cloud_run


def _session_secret(mode: str) -> str:
    """SESSION_SECRET if set. Otherwise a stable secret derived from JOBS_TOKEN, so sign-ins survive container restarts
    (a random secret per start would sign everyone out on every restart)."""
    s = os.getenv("SESSION_SECRET", "").strip()
    if s:
        return s
    jobs = os.getenv("JOBS_TOKEN", "dev-jobs-token")
    if mode == "google":
        log.warning("SESSION_SECRET is not set: deriving the session key from JOBS_TOKEN. Set SESSION_SECRET for a separate key.")
    return hashlib.sha256(("wotnow-session-v1:" + jobs).encode()).hexdigest()


@lru_cache
def get_platform() -> PlatformSettings:
    mode = os.getenv("AUTH_MODE", "dev").strip().lower()
    mode = "google" if mode in ("google", "firebase") else "dev"
    return PlatformSettings(
        auth_mode=mode,
        allow_demo=_b("ALLOW_DEMO", True),
        allow_guests=_b("ALLOW_GUESTS", mode == "dev"),
        dev_login=_b("DEV_LOGIN", False),
        on_cloud_run=bool(os.getenv("K_SERVICE")),
        google_client_id=os.getenv("GOOGLE_CLIENT_ID", "").strip(),
        session_secret=_session_secret(mode),
        session_ttl_days=_i("SESSION_TTL_DAYS", 14),
        admin_emails=frozenset(e.strip().lower() for e in os.getenv("ADMIN_EMAILS", "").split(",") if e.strip()),
        admin_token_login=_b("ADMIN_TOKEN_LOGIN", True),
        cors_origins=[o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()],
        trust_proxy=_b("TRUST_PROXY", False),
        max_body_bytes=_i("MAX_BODY_BYTES", 65536),
        rl_general_per_min=_i("RL_GENERAL_PER_MIN", 240),
        rl_answers_per_min=_i("RL_ANSWERS_PER_MIN", 12),
        rl_answers_per_day=_i("RL_ANSWERS_PER_DAY", 150),
        rl_auth_per_min=_i("RL_AUTH_PER_MIN", 20),
        rl_admin_per_min=_i("RL_ADMIN_PER_MIN", 180),
        pipeline_enabled=_b("PIPELINE_ENABLED", True),
        pipeline_tick_seconds=max(10, _i("PIPELINE_TICK_SECONDS", 60)),
        llm_concurrency=max(1, _i("LLM_CONCURRENCY", 6)),
        max_children=max(1, _i("MAX_CHILDREN", 3)),
        feed_cache_ttl_s=max(0, _i("FEED_CACHE_TTL_S", 20)),
        overrides_ttl_s=max(0, _i("OVERRIDES_TTL_S", 10)),
    )
