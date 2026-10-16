"""Platform settings that sit next to the v1 config: auth, security, pipeline switches. All from environment variables."""
from __future__ import annotations

import logging
import os
import secrets
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
    auth_mode: str = "dev"                  # dev = demo header only · google = Google sign-in (+ demo if ALLOW_DEMO)
    allow_demo: bool = True                 # "Try the student demo" / guest identities (X-Demo-User)
    google_client_id: str = ""
    session_secret: str = ""
    session_ttl_days: int = 14
    admin_emails: frozenset = field(default_factory=frozenset)
    admin_token_login: bool = True          # allow the jobs token as an admin password (handy on the build-host)
    cors_origins: list = field(default_factory=list)
    trust_proxy: bool = False               # read client IP from X-Forwarded-For (only behind your own LB)
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

    @property
    def google_enabled(self) -> bool:
        return self.auth_mode == "google" and bool(self.google_client_id)


@lru_cache
def get_platform() -> PlatformSettings:
    mode = os.getenv("AUTH_MODE", "dev").strip().lower()
    mode = "google" if mode in ("google", "firebase") else "dev"
    secret = os.getenv("SESSION_SECRET", "")
    if not secret:
        secret = secrets.token_urlsafe(32)
        if mode == "google":
            log.warning("SESSION_SECRET is not set: using a random one, so sign-ins are lost on every restart. Set SESSION_SECRET.")
    return PlatformSettings(
        auth_mode=mode,
        allow_demo=_b("ALLOW_DEMO", True),
        google_client_id=os.getenv("GOOGLE_CLIENT_ID", "").strip(),
        session_secret=secret,
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
    )
