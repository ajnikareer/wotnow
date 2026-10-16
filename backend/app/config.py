"""
wotnow backend configuration (environment variables).

Everything defaults to OFFLINE so it runs with zero keys:
  LLM_PROVIDER=mock  DATA_MODE=mock  DB_BACKEND=memory  AUTH_MODE=dev
Flip each switch independently to go live (see README).
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        g = os.getenv
        self.APP_NAME = "wotnow"
        self.VERSION = "0.1.0"
        self.ENV = g("ENV", "dev")

        # ---- Gen AI ----
        self.LLM_PROVIDER = g("LLM_PROVIDER", "mock").lower()          # gemini | mock
        self.GEMINI_MODEL = g("GEMINI_MODEL", "gemini-2.5-flash")
        self.EMBED_MODEL = g("EMBED_MODEL", "text-embedding-005")      # Vertex; AI Studio: gemini-embedding-001
        self.GOOGLE_CLOUD_PROJECT = g("GOOGLE_CLOUD_PROJECT", "")       # set => Vertex AI
        self.GOOGLE_CLOUD_LOCATION = g("GOOGLE_CLOUD_LOCATION", "us-central1")
        self.GEMINI_API_KEY = g("GEMINI_API_KEY", "")                   # alternative: AI Studio key
        self.GEN_TEMPERATURE = float(g("GEN_TEMPERATURE", "0.9"))       # creative post generation
        self.JUDGE_TEMPERATURE = float(g("JUDGE_TEMPERATURE", "0.1"))   # consistent judging

        # ---- Live conditions (local alerts) ----
        self.DATA_MODE = g("DATA_MODE", "mock").lower()                 # live | mock
        self.GOOGLE_MAPS_API_KEY = g("GOOGLE_MAPS_API_KEY", "")         # optional: Google Air Quality API
        self.HTTP_TIMEOUT = float(g("HTTP_TIMEOUT", "8"))

        # ---- Platform ----
        self.DB_BACKEND = g("DB_BACKEND", "memory").lower()             # firestore | memory
        self.AUTH_MODE = g("AUTH_MODE", "dev").lower()                  # firebase | dev
        self.JOBS_TOKEN = g("JOBS_TOKEN", "dev-jobs-token")
        self.AUTO_SEED = g("AUTO_SEED", "true").lower() == "true"       # seed demo content if DB is empty
        self.TIMEZONE = g("TIMEZONE", "Asia/Kolkata")                   # for streaks, quiet hours, daily limits

        # ---- Content engine ----
        self.DEDUPE_THRESHOLD = float(g("DEDUPE_THRESHOLD", "0.88"))    # cosine similarity, embeddings
        self.DEDUPE_FALLBACK_THRESHOLD = float(g("DEDUPE_FALLBACK_THRESHOLD", "0.80"))  # trigram cosine
        self.MAX_GEN_ATTEMPTS = int(g("MAX_GEN_ATTEMPTS", "3"))

        # ---- Demo ----
        self.DEMO_CROWD = int(g("DEMO_CROWD", "1200"))                  # simulated live-quiz players (0 = real only)

        self.CONTENT_DIR = Path(__file__).resolve().parent / "content"

    @property
    def use_vertex(self) -> bool:
        return bool(self.GOOGLE_CLOUD_PROJECT)


@lru_cache
def get_settings() -> Settings:
    return Settings()
