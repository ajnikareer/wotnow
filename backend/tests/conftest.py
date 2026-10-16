"""Test configuration (superset of the v1/v2 one): offline mode, an isolated state for every test, and two client fixtures."""
import os

import pytest

for k, v in {"LLM_PROVIDER": "mock", "DATA_MODE": "mock", "DB_BACKEND": "memory", "AUTH_MODE": "dev", "JOBS_TOKEN": "t",
             "AUTO_SEED": "true", "DEMO_CROWD": "50", "MAX_GEN_ATTEMPTS": "8", "PIPELINE_ENABLED": "false",
             "SESSION_SECRET": "test-session-secret", "TIMEZONE": "Asia/Kolkata"}.items():
    os.environ[k] = v


@pytest.fixture(autouse=True)
def _isolated_state():
    """Fresh settings, database, LLM provider, overrides and rate limiter for every test."""
    from app.ai.llm import reset_llm
    from app.config import get_settings
    from app.core import overrides
    from app.core.security import limiter
    from app.core.settings import get_platform
    from app.store.base import reset_db
    get_settings.cache_clear(); get_platform.cache_clear(); reset_db(); reset_llm(); overrides.invalidate(); limiter.hits.clear()
    yield


@pytest.fixture()
def client():
    """v1 fixture: the app with demo data seeded."""
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def v3_client(monkeypatch):
    """The app with an empty database (no demo seed), for admin / auth / pipeline tests."""
    from fastapi.testclient import TestClient
    from app import main
    monkeypatch.setattr(main.s, "AUTO_SEED", False)
    with TestClient(main.app) as c:
        yield c
