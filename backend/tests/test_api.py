"""Offline end-to-end tests (mock LLM, memory DB, demo seed). Shapes must match web/src/lib/types.ts."""
H = {"X-Demo-User": "demo-student"}
J = {"X-Jobs-Token": "t"}
HIDDEN = {"rubric", "answerKey", "explanation", "dangerPatterns", "modelAnswer", "voteCounts", "combo"}


def test_root_and_health(client):
    assert client.get("/healthz").json() == {"ok": True}
    r = client.get("/api/info").json()
    assert r["llm"] == "mock" and r["geminiReady"] is False


def test_me_shape(client):
    me = client.get("/api/me", headers=H).json()
    for k in ("id", "nickname", "avatar", "grade", "band", "city", "country", "school", "className", "xp", "level", "levelName",
              "nextLevelXp", "streak", "answers", "avgScore", "skills", "badges", "follows"):
        assert k in me, k
    assert me["nickname"] == "CleverFox" and me["level"] == 7 and me["levelName"] == "Prepared" and me["nextLevelXp"] == 3000
    assert me["country"] == "India"


def test_new_user_and_update(client):
    h = {"X-Demo-User": "kid-1"}
    me = client.get("/api/me", headers=h).json()
    assert me["xp"] == 0 and "compass" not in me["follows"]
    me = client.post("/api/me", headers=h, json={"nickname": "Rocket Fox!", "grade": 10, "follows": ["ember", "compass", "nope"]}).json()
    assert me["nickname"] == "RocketFox" and me["band"] == "senior" and me["follows"] == ["ember", "compass"]


def test_agents(client):
    a = client.get("/api/agents").json()
    assert [x["id"] for x in a] == ["ember", "signal", "pulse", "basil", "civic", "terra", "cipher", "compass"]
    assert a[0]["stats"]["factCards"] >= 4
    assert client.get("/api/agents/nope").status_code == 404
    assert client.get("/api/agents/ember/cards").json()[0]["id"].startswith("FIRE")


def test_feed_hides_answers_and_has_local_alert(client):
    feed = client.get("/api/feed", headers=H).json()
    assert feed[0]["type"] == "local_alert" and feed[0]["city"] == "Pune"
    assert all(not (HIDDEN & set(p)) for p in feed)
    types = {p["type"] for p in feed}
    assert {"scenario", "poll", "myth_fact", "scam_legit", "local_alert"} <= types
    # middle-school student never sees senior-only or careers content
    assert all("middle" in p["bands"] for p in feed) and not any(p["agentId"] == "compass" for p in feed)
    assert all(p["agentId"] in ("terra", "civic") for p in client.get("/api/feed?tab=near", headers=H).json())
    assert all(p["agentId"] == "ember" for p in client.get("/api/feed?agent=ember", headers=H).json())


def test_scenario_answer_good_partial_dangerous(client):
    h = {"X-Demo-User": "kid-2"}
    good = client.post("/api/posts/oil-fire/answer", headers=h, json={"text": "Do not use water. Switch off the stove and cover the pan with a lid. If it spreads, get out and call 101."}).json()
    assert good["score"] == 100 and good["label"] == "Brilliant answer!" and good["xpAwarded"] == 50
    assert all(c["hit"] for c in good["checklist"]) and good["sourceCards"][0]["id"] == "FIRE-012"
    retry = client.post("/api/posts/oil-fire/answer", headers=h, json={"text": "turn off gas"}).json()
    assert retry["xpAwarded"] == 0                       # retries only earn improvements

    h3 = {"X-Demo-User": "kid-3"}
    part = client.post("/api/posts/oil-fire/answer", headers=h3, json={"text": "Stop my brother from throwing water! Turn off the gas knob, and if it spreads take everyone out and call the fire brigade on 101."}).json()
    assert part["score"] == 70 and part["label"] == "Good. One key step missing." and not part["dangerous"]
    assert [c["hit"] for c in part["checklist"]] == [True, True, False, True]

    h4 = {"X-Demo-User": "kid-4"}
    bad = client.post("/api/posts/oil-fire/answer", headers=h4, json={"text": "Throw water on it fast and then call 101"}).json()
    assert bad["dangerous"] and bad["score"] <= 40 and "dangerous" in bad["label"]

    short = client.post("/api/posts/nosebleed/answer", headers=h4, json={"text": "idk"}).json()
    assert short["score"] <= 20


def test_top_responses_unlock_after_answer(client):
    h = {"X-Demo-User": "kid-5"}
    assert client.get("/api/posts/oil-fire", headers=h).json()["responses"] == []
    client.post("/api/posts/oil-fire/answer", headers=h, json={"text": "Never pour water. Put a lid on the pan and turn off the gas."})
    d = client.get("/api/posts/oil-fire", headers=h).json()
    assert d["post"]["my"]["answered"] and d["responses"][0]["expertPick"] and d["responses"][0]["expertReply"]
    assert set(d["responses"][0]) == {"id", "nickname", "avatar", "text", "score", "expertPick", "expertReply"}


def test_dangerous_or_abusive_answers_stay_private(client):
    client.post("/api/posts/nosebleed/answer", headers={"X-Demo-User": "kid-6"}, json={"text": "tilt the head back and wait"})
    client.post("/api/posts/nosebleed/answer", headers={"X-Demo-User": "kid-7"}, json={"text": "lean forward and pinch you idiot, call me on 9876543210"})
    client.post("/api/posts/nosebleed/answer", headers={"X-Demo-User": "kid-8"}, json={"text": "Lean forward, pinch the soft part for 10 minutes and tell the teacher."})
    rs = client.get("/api/posts/nosebleed", headers={"X-Demo-User": "kid-8"}).json()["responses"]
    texts = " ".join(r["text"] for r in rs)
    assert "tilt" not in texts and "idiot" not in texts


def test_votes(client):
    h = {"X-Demo-User": "kid-9"}
    r = client.post("/api/posts/road-first/vote", headers=h, json={"choice": "b"}).json()
    assert r["isCorrect"] and r["correct"] == "b" and r["xpAwarded"] == 10 and abs(sum(r["distribution"].values()) - 100) <= 2
    again = client.post("/api/posts/road-first/vote", headers=h, json={"choice": "a"}).json()
    assert again["choice"] == "b" and again["xpAwarded"] == 0
    assert client.get("/api/posts/road-first/vote", headers=h).json()["choice"] == "b"
    m = client.post("/api/posts/toothpaste/vote", headers=h, json={"choice": "fact"}).json()
    assert not m["isCorrect"] and m["xpAwarded"] == 2 and m["explanation"].startswith("Myth")
    assert client.post("/api/posts/otp-game/vote", headers=h, json={"choice": "maybe"}).status_code == 400
    assert client.post("/api/posts/oil-fire/vote", headers=h, json={"choice": "a"}).status_code == 400


def test_checkin_xp_streak(client):
    h = {"X-Demo-User": "kid-10"}
    alert = client.get("/api/feed", headers=h).json()[0]
    assert client.post(f"/api/posts/{alert['id']}/checkin", headers=h).json() == {"xpAwarded": 5}
    assert client.post(f"/api/posts/{alert['id']}/checkin", headers=h).json() == {"xpAwarded": 0}
    me = client.get("/api/me", headers=h).json()
    assert me["xp"] == 5 and me["streak"] == 1


def test_leaderboards(client):
    g = client.get("/api/leaderboard?scope=global", headers=H).json()
    assert g["scope"] == "global" and g["me"]["nickname"] == "CleverFox" and g["myCountry"] == "India"
    assert all(not r.get("nickname", "").startswith("Learner") for r in g["rows"])
    cntry = client.get("/api/leaderboard?scope=country", headers=H).json()
    assert cntry["scope"] == "country" and cntry["me"]["me"] and cntry["myCountry"] == "India"
    city = client.get("/api/leaderboard?scope=city", headers=H).json()
    assert city["scope"] == "city" and city["me"]["me"] and city["myCity"] == "Pune"


def test_live_quiz(client):
    q = client.get("/api/live/next").json()
    assert len(q["questions"]) == 5 and all(len(x["options"]) == 4 for x in q["questions"]) and q["startsIn"] == 5
    r = client.post("/api/live/submit", headers={"X-Demo-User": "kid-11"}, json={"score": 95}).json()
    assert r["rank"] >= 1 and r["players"] >= 1 and r["xpAwarded"] == 95


def test_parent_summary_and_limits(client):
    s = client.get("/api/parent/summary", headers=H).json()
    assert s["child"]["nickname"] == "CleverFox" and len(s["week"]) == 7 and len(s["conversationStarters"]) == 3
    assert s["recent"][0]["postTitle"] and s["safety"]["dms"] == "disabled"
    assert s["settings"]["topics"]["careers"] is False
    h = {"X-Demo-User": "kid-12"}
    client.get("/api/me", headers=h)
    s2 = client.post("/api/parent/settings", headers=h, json={"dailyLimit": 5, "quietHours": "", "weeklyEmail": True,
                                                             "topics": {"fire": False}}).json()
    assert s2["settings"]["dailyLimit"] == 5 and s2["settings"]["topics"]["fire"] is False
    assert not any(p["agentId"] == "ember" for p in client.get("/api/feed", headers=h).json())
    for pid in ("oil-fire", "nosebleed", "bus-wrapper"):
        client.post(f"/api/posts/{pid}/answer", headers=h, json={"text": "I would ask an adult for help and stay calm"})
    blocked = client.post("/api/posts/seat-offer/answer", headers=h, json={"text": "offer the seat"})
    assert blocked.status_code == 429


def test_jobs(client):
    assert client.post("/jobs/generate").status_code == 403
    r = client.post("/jobs/generate", headers=J).json()
    assert r["created"] >= 5
    created = [x for x in r["report"] if x["ok"]]
    pid = created[0]["postId"]
    assert client.get(f"/api/posts/{pid}", headers=H).status_code == 200
    pv = client.post("/jobs/preview?agent=ember&kind=scenario", headers=J).json()
    assert pv["ok"] and pv["post"]["rubric"] and client.get(f"/api/posts/{pv['post']['id']}", headers=H).status_code == 404
    assert client.post("/jobs/local-alerts", headers=J).json()["alerts"]
    assert client.post("/jobs/live-quiz?agent=cipher", headers=J).json()["questions"] == 5


def test_delete_me(client):
    h = {"X-Demo-User": "kid-13"}
    client.post("/api/posts/drink/vote", headers=h, json={"choice": "b"})
    assert client.delete("/api/me", headers=h).json() == {"deleted": True}
    assert client.get("/api/me", headers=h).json()["xp"] == 0
