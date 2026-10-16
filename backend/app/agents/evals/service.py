"""
Judge-agent evaluations, runnable from the admin UI (and the CLI).
Cases are scored through the SAME path as production (judge.judge: Gemini via the ADK judge agent, or the rule-based
fallback when Gemini is off), so the numbers show what students actually get.
"""
from __future__ import annotations

import asyncio
import json
import time
import uuid
from pathlib import Path
from typing import Optional

from ...core import overrides
from ...store.base import get_db

HERE = Path(__file__).resolve().parent
RUNS = "eval_runs"
KEY = "evals:cases"
_tasks: set = set()


def default_cases() -> dict:
    d = json.loads((HERE / "judge_cases.json").read_text(encoding="utf-8"))
    d.pop("_doc", None)
    return d


def load_cases() -> dict:
    return overrides.get(KEY) or default_cases()


def validate_cases(data: dict) -> dict:
    if not isinstance(data, dict) or not isinstance(data.get("scenarios"), dict) or not isinstance(data.get("cases"), list):
        raise ValueError("expected {scenarios: {...}, cases: [...]}")
    if not 1 <= len(data["cases"]) <= 300:
        raise ValueError("between 1 and 300 cases are allowed")
    for name, sc in data["scenarios"].items():
        for f in ("body", "question", "rubric", "dangerous"):
            if f not in sc:
                raise ValueError(f"scenario '{name}' is missing '{f}'")
        ids = [r.get("id") for r in sc["rubric"]]
        if not ids or len(set(ids)) != len(ids) or not all(isinstance(r.get("point"), str) for r in sc["rubric"]):
            raise ValueError(f"scenario '{name}' needs rubric items with unique ids and a 'point'")
    for i, c in enumerate(data["cases"], 1):
        sc = data["scenarios"].get(c.get("scenario"))
        if sc is None:
            raise ValueError(f"case {i}: unknown scenario '{c.get('scenario')}'")
        if not isinstance(c.get("answer"), str) or not c["answer"].strip() or len(c["answer"]) > 600:
            raise ValueError(f"case {i}: answer must be 1-600 characters")
        ids = {r["id"] for r in sc["rubric"]}
        if not isinstance(c.get("expected_hits"), list) or not set(c["expected_hits"]) <= ids:
            raise ValueError(f"case {i}: expected_hits must be rubric ids of '{c['scenario']}'")
        if not isinstance(c.get("dangerous"), bool):
            raise ValueError(f"case {i}: dangerous must be true or false")
    return {"scenarios": data["scenarios"], "cases": data["cases"]}


def _post_for(sc: dict) -> dict:
    n = max(1, len(sc["rubric"]))
    return {"id": "eval", "type": "scenario", "body": sc["body"], "question": sc["question"],
            "rubric": [{"id": r["id"], "point": r["point"], "note": r.get("note", ""), "weight": round(100 / n), "critical": False} for r in sc["rubric"]],
            "dangerousActions": sc["dangerous"], "dangerPatterns": []}


async def _one(i: int, case: dict, sc: dict, sem: asyncio.Semaphore) -> dict:
    from ...judge.judge import judge
    t0 = time.perf_counter()
    async with sem:
        try:
            ev = await judge(_post_for(sc), case["answer"], "middle")
            got = {c["id"] for c in ev["checklist"] if c["hit"]}
            danger, by, err = bool(ev["dangerous"]), ev.get("judgedBy", "?"), None
        except Exception as exc:
            got, danger, by, err = set(), False, "error", f"{type(exc).__name__}: {str(exc)[:120]}"
    exp = set(case["expected_hits"])
    return {"i": i, "scenario": case["scenario"], "answer": case["answer"], "expected": sorted(exp), "got": sorted(got),
            "expectedDanger": case["dangerous"], "gotDanger": danger, "judgedBy": by, "error": err,
            "ok": err is None and got == exp and danger == case["dangerous"], "ms": round((time.perf_counter() - t0) * 1000)}


def summarize(results: list[dict]) -> dict:
    tp = sum(len(set(r["got"]) & set(r["expected"])) for r in results)
    fp = sum(len(set(r["got"]) - set(r["expected"])) for r in results)
    fn = sum(len(set(r["expected"]) - set(r["got"])) for r in results)
    n = len(results) or 1
    by: dict[str, int] = {}
    for r in results:
        by[r["judgedBy"]] = by.get(r["judgedBy"], 0) + 1
    return {"total": len(results), "exact": sum(1 for r in results if r["ok"]),
            "precision": round(tp / (tp + fp), 3) if tp + fp else 1.0, "recall": round(tp / (tp + fn), 3) if tp + fn else 1.0,
            "dangerAccuracy": round(sum(1 for r in results if r["gotDanger"] == r["expectedDanger"]) / n, 3),
            "avgMs": round(sum(r["ms"] for r in results) / n), "judgedBy": by}


async def run(run_id: str, actor: str = "system", concurrency: int = 4) -> dict:
    db = get_db()
    data = load_cases()
    cases = data["cases"]
    doc = {"id": run_id, "ts": time.time(), "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "actor": actor,
           "status": "running", "total": len(cases), "done": 0, "metrics": None, "results": []}
    db.put(RUNS, run_id, doc)
    sem = asyncio.Semaphore(concurrency)
    results: list[dict] = []

    async def worker(i, c):
        r = await _one(i, c, data["scenarios"][c["scenario"]], sem)
        results.append(r)
        if len(results) % 5 == 0:
            db.put(RUNS, run_id, {**doc, "done": len(results)})
    try:
        await asyncio.gather(*[worker(i, c) for i, c in enumerate(cases, 1)])
        results.sort(key=lambda r: r["i"])
        doc.update(status="done", done=len(results), metrics=summarize(results), results=results)
    except Exception as exc:
        doc.update(status="failed", error=f"{type(exc).__name__}: {str(exc)[:200]}", results=results)
    db.put(RUNS, run_id, doc)
    return doc


def start(actor: str) -> str:
    run_id = f"{int(time.time() * 1000)}-{uuid.uuid4().hex[:4]}"
    t = asyncio.create_task(run(run_id, actor))
    _tasks.add(t)
    t.add_done_callback(_tasks.discard)
    return run_id


def recent_runs(limit: int = 10) -> list[dict]:
    rows = get_db().query_ex(RUNS, order_by="ts", desc=True, limit=limit)
    return [{k: r.get(k) for k in ("id", "at", "actor", "status", "total", "done", "metrics")} for r in rows]


def get_run(run_id: str) -> Optional[dict]:
    return get_db().get(RUNS, run_id)
