"""Content pipeline settings: defaults in code, admin edits stored as the 'pipeline' override."""
from __future__ import annotations

import re
from typing import Any

from ..core import overrides
from ..engine import cards as C

TIME_RE = re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")
FORMATS = ("scenario", "poll", "myth_fact", "scam_legit")
KEY = "pipeline"


def defaults() -> dict:
    return {
        "enabled": True,                    # master switch (also PIPELINE_ENABLED env)
        "paused": False,                    # admin pause button: stop all automatic posting
        "posts_per_expert_per_day": 8,
        "active_start": "06:00",            # posts are spread across this window (server timezone)
        "active_end": "23:00",
        "experts": {a["id"]: True for a in C.agents()},
        "formats": {f: True for f in FORMATS},
        "approve_first": False,             # True: new posts wait in the review queue ("pending")
        "reviewed_only": False,             # True: experts only use fact cards marked reviewed
        "max_pending": 60,                  # stop generating when this many posts wait for review
        "max_per_tick": 2,                  # up to 2 posts per scheduler tick
        "alerts_enabled": True, "alerts_time": "06:30",
        "quizzes_enabled": True, "quiz_times": ["12:45", "19:45"],
        "failure_backoff_min": 20,
        "trace_retention_days": 14,
        "run_retention": 300,
    }


def load() -> dict:
    cfg = defaults()
    ov = overrides.get(KEY) or {}
    for k, v in ov.items():
        if k in ("experts", "formats") and isinstance(v, dict):
            cfg[k] = {**cfg[k], **{kk: bool(vv) for kk, vv in v.items() if kk in cfg[k]}}
        elif k in cfg:
            cfg[k] = v
    return cfg


def _int(v: Any, lo: int, hi: int, name: str) -> int:
    try:
        n = int(v)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a whole number")
    if not lo <= n <= hi:
        raise ValueError(f"{name} must be between {lo} and {hi}")
    return n


def _time(v: Any, name: str) -> str:
    if not isinstance(v, str) or not TIME_RE.match(v):
        raise ValueError(f"{name} must look like 08:30")
    return v


def minutes(hhmm: str) -> int:
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def validate(patch: dict) -> dict:
    """Returns the cleaned subset of settings from `patch`; raises ValueError on bad input."""
    base = defaults()
    out: dict = {}
    for k, v in patch.items():
        if k not in base:
            raise ValueError(f"unknown setting '{k}'")
        if k in ("enabled", "paused", "approve_first", "reviewed_only", "alerts_enabled", "quizzes_enabled"):
            out[k] = bool(v)
        elif k == "posts_per_expert_per_day":
            out[k] = _int(v, 0, 6, k)
        elif k == "max_pending":
            out[k] = _int(v, 1, 200, k)
        elif k == "max_per_tick":
            out[k] = _int(v, 1, 5, k)
        elif k == "failure_backoff_min":
            out[k] = _int(v, 1, 720, k)
        elif k == "trace_retention_days":
            out[k] = _int(v, 1, 365, k)
        elif k == "run_retention":
            out[k] = _int(v, 20, 5000, k)
        elif k in ("active_start", "active_end", "alerts_time"):
            out[k] = _time(v, k)
        elif k == "quiz_times":
            if not isinstance(v, list) or len(v) > 4:
                raise ValueError("quiz_times must be a list of up to 4 times")
            out[k] = sorted({_time(t, "quiz time") for t in v})
        elif k in ("experts", "formats"):
            if not isinstance(v, dict):
                raise ValueError(f"{k} must be an object")
            bad = [x for x in v if x not in base[k]]
            if bad:
                raise ValueError(f"unknown {k}: {', '.join(map(str, bad))}")
            out[k] = {x: bool(y) for x, y in v.items()}
    start = out.get("active_start") or load()["active_start"]
    end = out.get("active_end") or load()["active_end"]
    if minutes(start) >= minutes(end):
        raise ValueError("active_start must be earlier than active_end")
    return out


def save(patch: dict, actor: str) -> dict:
    clean = validate(patch)
    cur = overrides.get(KEY) or {}
    merged = dict(cur)
    for k, v in clean.items():
        merged[k] = {**cur.get(k, {}), **v} if k in ("experts", "formats") else v
    overrides.put(KEY, merged, actor)
    return load()


def reset(actor: str) -> dict:
    overrides.delete(KEY, actor)
    return load()
