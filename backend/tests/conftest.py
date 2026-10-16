import os
import pytest

for k, v in {"LLM_PROVIDER": "mock", "DATA_MODE": "mock", "DB_BACKEND": "memory", "AUTH_MODE": "dev",
             "JOBS_TOKEN": "t", "AUTO_SEED": "true", "DEMO_CROWD": "50", "MAX_GEN_ATTEMPTS": "8"}.items():
    os.environ[k] = v


@pytest.fixture()
def client():
    from fastapi.testclient import TestClient
    from app.config import get_settings
    from app.store.base import reset_db
    from app.ai.llm import reset_llm
    get_settings.cache_clear(); reset_db(); reset_llm()
    from app.main import app
    with TestClient(app) as c:
        yield c
