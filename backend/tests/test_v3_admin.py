"""Admin API: overview, pipeline control, review queue, agents/skills, guardrails, fact cards, evaluations, traces, audit."""
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.engine import generator
from app.store.base import get_db

H = {"X-Admin-Token": "t"}


@pytest.fixture()
def client(v3_client):
    return v3_client


def wait_for(fn, timeout=6.0):
    end = time.time() + timeout
    while time.time() < end:
        v = fn()
        if v:
            return v
        time.sleep(0.05)
    raise AssertionError("timed out waiting")


def add_post(pid, **kw):
    p = {"id": pid, "agentId": "ember", "type": "poll", "createdAt": datetime.now(ZoneInfo("UTC")).isoformat(), "bands": ["middle"], "title": f"Post {pid}",
         "body": "b", "question": "q?", "options": [{"id": "a", "text": "x"}, {"id": "b", "text": "y"}], "answerKey": "a", "explanation": "because",
         "status": "live", "origin": "pipeline", "source": "gemini", "rubric": [{"id": "r1", "point": "p"}], "sourceCards": [], "stats": {"responses": 0}}
    p.update(kw)
    get_db().put(generator.POSTS, pid, p)
    return p


def test_overview(client):
    add_post("p1"); add_post("p2", status="pending"); add_post("p3", status="rejected", origin="seed")
    get_db().put("users", "u1", {"id": "u1"}); get_db().put("accounts", "a1", {"id": "a1"})
    now = time.time()
    get_db().put("agent_traces", "t1", {"id": "t1", "ts": now, "skill": "judge", "ok": True, "ms": 100})
    get_db().put("agent_traces", "t2", {"id": "t2", "ts": now, "skill": "judge", "ok": False, "blocked": "x", "ms": 300})
    get_db().put("agent_traces", "t3", {"id": "t3", "ts": now - 3 * 86400, "skill": "judge", "ok": True, "ms": 1})       # older than 24h
    o = client.get("/api/admin/overview", headers=H).json()
    assert o["posts"]["byStatus"] == {"live": 1, "pending": 1, "rejected": 1} and o["posts"]["madeByPipelineToday"] == 2
    assert o["people"] == {"students": 1, "accounts": 1} and o["db"] == "memory" and o["ai"]["provider"] == "mock"
    j = o["agentRuns24h"]["bySkill"]["judge"]
    assert j == {"runs": 2, "ok": 1, "blocked": 1, "errors": 0, "avgMs": 200}
    assert o["pipeline"]["paused"] is False and o["cards"]["total"] >= 8 and o["cards"]["reviewed"] == 0 and o["reviewedOnly"] is False
    assert client.get("/api/admin/overview").status_code == 403


def test_pipeline_settings_pause_and_audit(client):
    p = client.get("/api/admin/pipeline", headers=H).json()
    assert p["config"]["posts_per_expert_per_day"] == 1 and len(p["schedule"]) >= 8 and p["formats"] and p["overridden"] == []
    r = client.put("/api/admin/pipeline", headers=H, json={"posts_per_expert_per_day": 3, "approve_first": True, "experts": {"compass": False}})
    assert r.status_code == 200 and r.json()["config"]["posts_per_expert_per_day"] == 3 and r.json()["overridden"] != []
    assert next(x for x in r.json()["schedule"] if x["agent"] == "compass")["enabled"] is False
    bad = client.put("/api/admin/pipeline", headers=H, json={"posts_per_expert_per_day": 50})
    assert bad.status_code == 400 and "between" in bad.json()["detail"]
    assert client.put("/api/admin/pipeline", headers=H, json={"mystery": 1}).status_code == 400
    assert client.post("/api/admin/pipeline/pause", headers=H, json={"paused": True}).json()["config"]["paused"] is True
    assert client.post("/api/admin/pipeline/pause", headers=H, json={"paused": False}).json()["config"]["paused"] is False
    assert client.post("/api/admin/pipeline/reset", headers=H).json()["config"]["posts_per_expert_per_day"] == 1
    actions = [a["action"] for a in client.get("/api/admin/audit", headers=H).json()["audit"]]
    assert actions[:3] == ["pipeline.reset", "pipeline.resume", "pipeline.pause"] and "pipeline.update" in actions


def test_run_now_in_background_and_conflicts(client, monkeypatch):
    async def fake(agent_id, kind=None, band=None, publish=True, rng=None, local=None):
        return {"ok": True, "attempts": [], "post": {"id": f"{agent_id}-n", "agentId": agent_id, "type": kind or "poll", "createdAt": datetime.now(ZoneInfo("UTC")).isoformat(),
                                                      "bands": ["middle"], "title": "T", "status": "live", "sourceCards": [], "stats": {}}}
    monkeypatch.setattr(generator, "generate_one", fake)
    assert client.post("/api/admin/pipeline/run-now", headers=H, json={"agents": ["nobody"]}).status_code == 400
    assert client.post("/api/admin/pipeline/run-now", headers=H, json={"kind": "haiku"}).status_code == 400
    r = client.post("/api/admin/pipeline/run-now", headers=H, json={"agents": ["ember", "pulse"], "kind": "poll"})
    assert r.status_code == 200 and r.json() == {"started": True, "agents": ["ember", "pulse"]}
    runs = wait_for(lambda: client.get("/api/admin/pipeline/runs", headers=H).json()["runs"])
    assert runs[0]["source"] == "admin" and [a["agent"] for a in runs[0]["actions"]] == ["ember", "pulse"]
    assert wait_for(lambda: len(get_db().query(generator.POSTS)) == 2)
    get_db().acquire_lease("pipeline_tick", "other", 600)
    assert client.post("/api/admin/pipeline/run-now", headers=H, json={}).status_code == 409


def test_review_queue(client):
    add_post("a1", status="pending"); add_post("a2", status="pending", agentId="pulse"); add_post("a3", status="live", origin="seed")
    pend = client.get("/api/admin/posts?status=pending", headers=H).json()
    assert pend["total"] == 2 and {p["id"] for p in pend["posts"]} == {"a1", "a2"}
    assert client.get("/api/admin/posts?agent=pulse", headers=H).json()["total"] == 1
    assert client.get("/api/admin/posts?origin=seed", headers=H).json()["posts"][0]["id"] == "a3"
    full = client.get("/api/admin/posts/a1", headers=H).json()
    assert full["answerKey"] == "a" and full["rubric"] and full["status"] == "pending"          # admins see the hidden keys
    r = client.post("/api/admin/posts/a1/status", headers=H, json={"status": "live"})
    assert r.status_code == 200 and r.json()["status"] == "live" and r.json()["publishedAt"]
    assert get_db().get(generator.POSTS, "a1")["reviewedBy"] == "admin-token"
    assert client.post("/api/admin/posts/a2/status", headers=H, json={"status": "rejected"}).json()["status"] == "rejected"
    assert client.post("/api/admin/posts/a3/status", headers=H, json={"status": "unpublished"}).json()["status"] == "unpublished"
    assert client.post("/api/admin/posts/a3/status", headers=H, json={"status": "nonsense"}).status_code == 400
    assert client.post("/api/admin/posts/zzz/status", headers=H, json={"status": "live"}).status_code == 404
    assert client.get("/api/admin/posts/zzz", headers=H).status_code == 404
    assert client.get("/api/admin/posts?limit=1&offset=1", headers=H).json()["posts"].__len__() == 1


def test_agents_skills_and_instructions(client):
    a = client.get("/api/admin/agents", headers=H).json()
    assert a["placeholders"] and len(a["experts"]) >= 8 and {s["skill"] for s in a["skills"]} >= {"judge", "write_scenario", "review_post"}
    assert {i["file"] for i in a["instructions"]} >= {"writer.md", "judge.md", "reviewer.md"}
    assert next(i for i in a["instructions"] if i["file"] == "writer.md")["usedBy"] == ["write_scenario", "write_poll", "write_myth_fact", "write_scam_legit"]

    r = client.put("/api/admin/agents/skills/judge", headers=H, json={"temperature": 0.3})
    assert next(s for s in r.json()["skills"] if s["skill"] == "judge")["overridden"] == ["temperature"]
    assert client.put("/api/admin/agents/skills/judge", headers=H, json={"temperature": 0.1}).json()["skills"][0]                 # back to default clears the override
    assert next(s for s in client.get("/api/admin/agents", headers=H).json()["skills"] if s["skill"] == "judge")["overridden"] == []
    for bad in ({"temperature": 3}, {"temperature": "hot"}, {"timeout_s": 1}, {"review": True}, {"weird": 1}):
        assert client.put("/api/admin/agents/skills/judge", headers=H, json=bad).status_code == 400, bad
    assert client.put("/api/admin/agents/skills/write_scenario", headers=H, json={"review": False}).status_code == 200
    assert client.put("/api/admin/agents/skills/nope", headers=H, json={"temperature": 0.2}).status_code == 404
    assert client.delete("/api/admin/agents/skills/write_scenario", headers=H).status_code == 200

    good = "You are the wotnow Answer Judge, extra gentle. Audience: {audience}. Judge by meaning and never score."
    r = client.put("/api/admin/agents/instructions/judge.md", headers=H, json={"text": good})
    assert next(i for i in r.json()["instructions"] if i["file"] == "judge.md")["overridden"] is True
    for bad in ("too short", "Hello {nobody} this is a long enough instruction text", "A long enough instruction with {audience} and a stray { brace",
                "x" * 7000, "A long enough instruction that has a JSON {\"a\": 1} example inside it"):
        assert client.put("/api/admin/agents/instructions/judge.md", headers=H, json={"text": bad}).status_code == 400, bad[:30]
    assert client.put("/api/admin/agents/instructions/nope.md", headers=H, json={"text": good}).status_code == 404
    hist = client.get("/api/admin/config-history?key=instr:judge.md", headers=H).json()["history"]
    assert hist and hist[0]["version"] == 1 and "extra gentle" in hist[0]["value"]["text"]
    r = client.delete("/api/admin/agents/instructions/judge.md", headers=H)
    assert next(i for i in r.json()["instructions"] if i["file"] == "judge.md")["overridden"] is False
    same = next(i for i in r.json()["instructions"] if i["file"] == "judge.md")["default"]
    client.put("/api/admin/agents/instructions/judge.md", headers=H, json={"text": same})                           # saving the default = no override
    assert next(i for i in client.get("/api/admin/agents", headers=H).json()["instructions"] if i["file"] == "judge.md")["overridden"] is False


def test_edited_agent_settings_reach_the_live_agents(client):
    from app.agents.factory import AgentFactory
    f = AgentFactory()
    assert f.get("judge")[0].generate_content_config.temperature == 0.1
    client.put("/api/admin/agents/skills/judge", headers=H, json={"temperature": 0.7})
    assert f.get("judge")[0].generate_content_config.temperature == 0.7


def test_guardrails_edit_test_and_reset(client):
    g = client.get("/api/admin/guardrails", headers=H).json()
    assert "link" in g["effective"]["blocked_output_patterns"] and g["overridden"] == []
    r = client.put("/api/admin/guardrails", headers=H, json={"allowed_numbers": ["112", "100"], "blocked_output_patterns": {"swear": "\\bdarn\\b", "link": "https?://"},
                                                           "injection_markers": ["jailbreak"], "policy": ["Be kind.", "Teach only from cards."], "max_input_chars": 5000})
    assert r.status_code == 200 and r.json()["overridden"] == ["allowed_numbers", "blocked_output_patterns", "injection_markers", "max_input_chars", "policy"]
    t = client.post("/api/admin/guardrails/test", headers=H, json={"text": "Darn! visit https://x.y, call 9876543210 or mail a@b.co. Jailbreak now"}).json()
    assert t["blockedOutput"] == ["swear", "link"] and t["wouldBlock"] and "[phone removed]" in t["scrubbedInput"] and "[email removed]" in t["scrubbedInput"] and t["injectionSuspected"]
    for bad in ({"policy": []}, {"policy": ["x" * 400]}, {"allowed_numbers": ["abc"]}, {"blocked_output_patterns": {"bad": "([unclosed"}}, {"blocked_output_patterns": {"bad name": "x"}},
                {"max_input_chars": 10}, {"unknown_key": 1}, {"pii_patterns": "nope"}):
        assert client.put("/api/admin/guardrails", headers=H, json=bad).status_code == 400, bad
    r = client.put("/api/admin/guardrails", headers=H, json={"policy": client.get("/api/admin/guardrails", headers=H).json()["defaults"]["policy"]})
    assert "policy" not in r.json()["overridden"]                                                                      # equal to default → override removed
    assert client.delete("/api/admin/guardrails", headers=H).json()["overridden"] == []


def test_fact_cards_review_workflow(client):
    cards = client.get("/api/admin/cards?agent=ember", headers=H).json()
    assert cards["reviewedOnly"] is False and cards["cards"] and all(c["agentId"] == "ember" for c in cards["cards"])
    cid = "FIRE-012"
    c = next(x for x in cards["cards"] if x["id"] == cid)
    assert c["reviewed"] is False and c["edited"] is False
    r = client.put(f"/api/admin/cards/{cid}", headers=H, json={"reviewed": True, "facts": ["Fact A.", "Fact B."], "title": "Kitchen oil fires (v2)"})
    assert r.status_code == 200 and r.json()["reviewed"] is True and r.json()["reviewedBy"] == "admin-token" and r.json()["facts"] == ["Fact A.", "Fact B."] and r.json()["edited"]
    assert client.put(f"/api/admin/cards/{cid}", headers=H, json={"disabled": True}).json()["disabled"] is True
    for bad in ({"facts": []}, {"facts": ["x" * 500]}, {"title": "no"}, {"colour": "red"}):
        assert client.put(f"/api/admin/cards/{cid}", headers=H, json=bad).status_code == 400, bad
    assert client.put("/api/admin/cards/NOPE-1", headers=H, json={"reviewed": True}).status_code == 404
    client.put("/api/admin/pipeline", headers=H, json={"reviewed_only": True})
    assert client.get("/api/admin/cards", headers=H).json()["reviewedOnly"] is True
    assert client.get("/api/admin/overview", headers=H).json()["reviewedOnly"] is True
    r = client.delete(f"/api/admin/cards/{cid}", headers=H)
    assert r.json()["reviewed"] is False and r.json()["edited"] is False and r.json()["disabled"] is False
    assert client.delete("/api/admin/cards/NOPE-1", headers=H).status_code == 404


def test_evaluations_run_and_edit_cases(client):
    e = client.get("/api/admin/evals", headers=H).json()
    assert len(e["cases"]) >= 30 and {"oil-fire", "nosebleed", "bus-wrapper", "otp-game"} <= set(e["scenarios"]) and e["customised"] is False and e["runs"] == []
    run_id = client.post("/api/admin/evals/run", headers=H).json()["runId"]
    done = wait_for(lambda: (lambda r: r if r["status"] != "running" else None)(client.get(f"/api/admin/evals/runs/{run_id}", headers=H).json()))
    assert done["status"] == "done" and done["total"] == len(e["cases"]) and len(done["results"]) == len(e["cases"])
    m = done["metrics"]
    assert set(m) >= {"total", "exact", "precision", "recall", "dangerAccuracy", "avgMs", "judgedBy"} and 0 <= m["precision"] <= 1 and 0 <= m["recall"] <= 1
    assert {"i", "scenario", "answer", "expected", "got", "ok", "judgedBy"} <= set(done["results"][0])
    assert client.get("/api/admin/evals", headers=H).json()["runs"][0]["id"] == run_id
    assert client.get("/api/admin/evals/runs/nope", headers=H).status_code == 404

    mine = {"scenarios": {"s": e["scenarios"]["oil-fire"]}, "cases": [{"scenario": "s", "answer": "Switch off the gas", "expected_hits": ["r2"], "dangerous": False}]}
    r = client.put("/api/admin/evals/cases", headers=H, json=mine)
    assert r.status_code == 200 and r.json()["customised"] is True and len(r.json()["cases"]) == 1
    for bad in ({"scenarios": {}, "cases": []}, {"scenarios": mine["scenarios"], "cases": [{"scenario": "zzz", "answer": "a", "expected_hits": [], "dangerous": False}]},
                {"scenarios": mine["scenarios"], "cases": [{"scenario": "s", "answer": "a", "expected_hits": ["r99"], "dangerous": False}]},
                {"scenarios": mine["scenarios"], "cases": [{"scenario": "s", "answer": "", "expected_hits": [], "dangerous": False}]},
                {"scenarios": mine["scenarios"], "cases": [{"scenario": "s", "answer": "a", "expected_hits": [], "dangerous": "no"}]}, "nonsense"):
        assert client.put("/api/admin/evals/cases", headers=H, json=bad).status_code in (400, 422), bad
    run2 = client.post("/api/admin/evals/run", headers=H).json()["runId"]
    d2 = wait_for(lambda: (lambda r: r if r["status"] != "running" else None)(client.get(f"/api/admin/evals/runs/{run2}", headers=H).json()))
    assert d2["total"] == 1
    assert len(client.delete("/api/admin/evals/cases", headers=H).json()["cases"]) >= 30


def test_traces_people_and_audit(client):
    now = time.time()
    for i, (skill, ok) in enumerate([("judge", True), ("judge", False), ("moderate", True)]):
        get_db().put("agent_traces", f"t{i}", {"id": f"t{i}", "ts": now + i, "skill": skill, "ok": ok, "agent": "x", "ms": 5})
    allt = client.get("/api/admin/traces", headers=H).json()["traces"]
    assert [t["id"] for t in allt] == ["t2", "t1", "t0"]
    assert [t["id"] for t in client.get("/api/admin/traces?skill=judge", headers=H).json()["traces"]] == ["t1", "t0"]
    assert [t["id"] for t in client.get("/api/admin/traces?ok=false", headers=H).json()["traces"]] == ["t1"]
    get_db().put("users", "u1", {"id": "u1", "nickname": "Fox", "xp": 50, "band": "middle", "grade": 8, "city": "Pune"})
    get_db().put("users", "u2", {"id": "u2", "nickname": "Owl", "xp": 90, "band": "senior", "grade": 10, "city": "Pune"})
    get_db().put("accounts", "a1", {"id": "a1", "email": "p@example.com", "name": "P", "children": ["u1", "u2"], "lastLogin": "2026-10-15T10:00:00"})
    p = client.get("/api/admin/people", headers=H).json()
    assert p["students"] == 2 and p["byBand"] == {"junior": 0, "middle": 1, "senior": 1} and p["top"][0]["nickname"] == "Owl" and p["accountsList"][0]["children"] == 2
    assert "audit" in client.get("/api/admin/audit", headers=H).json()
