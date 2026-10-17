"""Sessions, Google sign-in (verifier patched), accounts/children, demo identities, admin auth, rate limits, headers."""
import pytest

from app.core import security
from app.core.settings import get_platform


@pytest.fixture()
def google(monkeypatch):
    monkeypatch.setenv("AUTH_MODE", "google")
    monkeypatch.setenv("GOOGLE_CLIENT_ID", "test-client.apps.googleusercontent.com")
    monkeypatch.setenv("ADMIN_EMAILS", "boss@example.com")
    get_platform.cache_clear()
    people = {"tok-parent": {"sub": "g-1", "email": "parent@example.com", "email_verified": True, "name": "Pat Parent", "picture": ""},
              "tok-parent2": {"sub": "g-2", "email": "other@example.com", "email_verified": True, "name": "Olly Other", "picture": ""},
              "tok-boss": {"sub": "g-3", "email": "boss@example.com", "email_verified": True, "name": "Bo Boss", "picture": ""},
              "tok-unverified": {"sub": "g-4", "email": "boss@example.com", "email_verified": False, "name": "Fake", "picture": ""}}

    def fake_verify(credential):
        credential = credential.rstrip("-")             # tests pad credentials to satisfy the request model's min length
        if credential not in people:
            raise ValueError("Token used too late or bad signature")
        return people[credential]
    monkeypatch.setattr(security, "verify_google_credential", fake_verify)


@pytest.fixture()
def client(v3_client):
    return v3_client


def _cred(name):
    return name + "-" * max(0, 20 - len(name))        # satisfy min_length of the request model


def sign_in(client, name="tok-parent"):
    r = client.post("/api/auth/google", json={"credential": _cred(name)})
    assert r.status_code == 200, r.text
    return {"Authorization": "Bearer " + r.json()["token"]}, r.json()["account"]


# ---------------- sessions ----------------
def test_session_token_roundtrip_tamper_and_expiry():
    tok = security.issue_session({"id": "a_1", "email": "x@y.z"})
    assert security.verify_session(tok)["sub"] == "a_1"
    v, body, sig = tok.split(".")
    assert security.verify_session(f"{v}.{body}.{sig[:-2]}AA") is None
    assert security.verify_session(f"{v}.{body}x.{sig}") is None
    assert security.verify_session("garbage") is None and security.verify_session("v1..") is None
    assert security.verify_session(security.issue_session({"id": "a_1"}, ttl_days=-1)) is None


# ---------------- dev mode ----------------
def test_dev_mode_demo_identity_and_reserved_ids(client):
    assert client.get("/api/auth/config").json()["googleEnabled"] is False
    assert client.get("/api/me").json()["id"] == "demo-student"                            # default identity (v1 behaviour)
    assert client.get("/api/me", headers={"X-Demo-User": "guest-abc"}).json()["id"] == "guest-abc"
    for bad in ("c_123", "a_456", "has space", "x" * 70, "semi;colon"):
        assert client.get("/api/me", headers={"X-Demo-User": bad}).status_code == 400, bad
    assert client.post("/api/auth/google", json={"credential": "x" * 30}).status_code == 503


# ---------------- google mode ----------------
def test_google_login_children_and_isolation(client, google):
    cfg = client.get("/api/auth/config").json()
    assert cfg["googleEnabled"] and cfg["googleClientId"].startswith("test-client") and cfg["allowDemo"]
    h, acc = sign_in(client)
    assert acc["email"] == "parent@example.com" and acc["children"] == [] and acc["isAdmin"] is False
    assert client.get("/api/me", headers=h).status_code == 409                              # no child yet

    r = client.post("/api/account/children", headers=h, json={"nickname": "CleverFox", "avatar": "🦊", "grade": 8, "city": "Pune"})
    assert r.status_code == 200 and r.json()["child"]["nickname"] == "CleverFox" and r.json()["child"]["id"].startswith("c_")
    first = r.json()["child"]["id"]
    assert client.get("/api/me", headers=h).json()["id"] == first
    r2 = client.post("/api/account/children", headers=h, json={"nickname": "BraveOwl", "grade": 10})
    second = r2.json()["child"]["id"]
    assert r2.json()["child"]["band"] == "senior"
    assert client.get("/api/me", headers={**h, "X-Child": second}).json()["id"] == second
    assert client.get("/api/me", headers={**h, "X-Child": "c_doesnotexist"}).json()["id"] == first   # unknown → default child

    # another parent can neither see nor select these children
    h2, _ = sign_in(client, "tok-parent2")
    client.post("/api/account/children", headers=h2, json={"nickname": "OtherKid"})
    mine2 = client.get("/api/me", headers={**h2, "X-Child": first}).json()
    assert mine2["id"] != first and mine2["nickname"] == "OtherKid"

    client.post("/api/account/children", headers=h, json={"nickname": "ThirdKid"})
    assert client.post("/api/account/children", headers=h, json={"nickname": "FourthKid"}).status_code == 409      # MAX_CHILDREN=3
    assert client.post("/api/account/children", headers=h, json={"nickname": "ab"}).status_code == 422             # too short
    assert client.post("/api/account/children", headers=h, json={"nickname": "Okay", "grade": 2}).status_code == 422

    acc_now = client.delete(f"/api/account/children/{second}", headers=h).json()
    assert second not in [c["id"] for c in acc_now["children"]]
    assert client.delete("/api/account/children/c_nope", headers=h).status_code == 404
    assert client.delete(f"/api/account/children/{mine2['id']}", headers=h).status_code == 404                       # not yours

    assert client.delete("/api/account", headers=h).json() == {"deleted": True}
    assert client.get("/api/account", headers=h).status_code == 401                                                  # account gone
    from app.store.base import get_db
    assert get_db().get("users", first) is None


def test_deleted_child_is_not_recreated(client, google):
    h, _ = sign_in(client)
    cid = client.post("/api/account/children", headers=h, json={"nickname": "OnlyKid"}).json()["child"]["id"]
    assert client.get("/api/me", headers=h).json()["id"] == cid
    from app.store.base import get_db
    get_db().delete("users", cid)                                    # e.g. the child profile was removed through DELETE /api/me
    assert client.get("/api/me", headers=h).status_code == 409       # not silently re-created as an empty profile
    assert client.get("/api/account", headers=h).json()["children"] == []


def test_google_failures(client, google):
    assert client.post("/api/auth/google", json={"credential": _cred("nobody")}).status_code == 401
    assert client.post("/api/auth/google", json={"credential": _cred("tok-unverified")}).status_code == 401
    assert client.post("/api/auth/google", json={"credential": "short"}).status_code == 422
    assert client.get("/api/account").status_code == 401
    assert client.get("/api/account", headers={"Authorization": "Bearer nonsense"}).status_code == 401


def test_demo_identities_in_google_mode(client, google, monkeypatch):
    assert client.get("/api/me", headers={"X-Demo-User": "demo-student"}).status_code == 200             # the shared demo student
    assert client.get("/api/me", headers={"X-Demo-User": "guest-1"}).status_code == 403                   # invented guest ids are refused
    assert client.get("/api/me").status_code == 401                                                       # no default identity in google mode
    assert client.get("/api/me", headers={"X-Demo-User": "c_abc"}).status_code == 400                     # cannot impersonate a real child
    monkeypatch.setenv("ALLOW_GUESTS", "true")                                                            # explicit opt-in brings guests back
    get_platform.cache_clear()
    assert client.get("/api/me", headers={"X-Demo-User": "guest-1"}).status_code == 200
    monkeypatch.setenv("ALLOW_DEMO", "false")
    get_platform.cache_clear()
    assert client.get("/api/me", headers={"X-Demo-User": "demo-student"}).status_code == 401


# ---------------- admin ----------------
def test_admin_access_rules(client, google, monkeypatch):
    assert client.get("/api/admin/overview").status_code == 403
    assert client.get("/api/admin/overview", headers={"X-Admin-Token": "wrong"}).status_code == 403
    assert client.get("/api/admin/overview", headers={"X-Admin-Token": "t"}).status_code == 200      # JOBS_TOKEN
    hp, _ = sign_in(client, "tok-parent")
    assert client.get("/api/admin/overview", headers=hp).status_code == 403                          # not on the allowlist
    hb, accb = sign_in(client, "tok-boss")
    assert accb["isAdmin"] is True and client.get("/api/admin/overview", headers=hb).json()["actor"] == "boss@example.com"
    from app.core import accounts
    acc = accounts.upsert_google({"sub": "g-9", "email": "boss@example.com", "email_verified": False})      # same email, but not verified
    hu = {"Authorization": "Bearer " + security.issue_session(acc)}
    assert client.get("/api/admin/overview", headers=hu).status_code == 403                          # unverified email never counts
    monkeypatch.setenv("ADMIN_TOKEN_LOGIN", "false")
    get_platform.cache_clear()
    assert client.get("/api/admin/overview", headers={"X-Admin-Token": "t"}).status_code == 403
    assert client.get("/api/admin/overview", headers=hb).status_code == 200


def test_jobs_token_required(client):
    assert client.post("/jobs/tick").status_code == 403
    assert client.post("/jobs/tick", headers={"X-Jobs-Token": "wrong"}).status_code == 403
    assert client.post("/jobs/tick", headers={"X-Jobs-Token": "t"}).status_code == 200


# ---------------- hardening ----------------
def test_security_headers_body_limit_and_cors(client):
    r = client.get("/api/health")
    assert r.headers["x-content-type-options"] == "nosniff" and r.headers["x-frame-options"] == "DENY" and r.headers["cache-control"] == "no-store"
    assert "access-control-allow-origin" not in client.get("/api/health", headers={"Origin": "https://evil.example"}).headers
    big = client.post("/api/posts/x/answer", content=b"x" * 70000, headers={"content-type": "application/json", "X-Demo-User": "guest-1"})
    assert big.status_code == 413


def test_answer_rate_limits(client, monkeypatch):
    monkeypatch.setenv("RL_ANSWERS_PER_MIN", "3")
    get_platform.cache_clear()
    codes = [client.post("/api/posts/p1/answer", json={"text": "hello world"}, headers={"X-Demo-User": "guest-rl"}).status_code for _ in range(5)]
    assert [c == 429 for c in codes] == [False, False, False, True, True]        # (the endpoint itself may answer 200/404/…)
    r = client.post("/api/posts/p1/answer", json={"text": "hello world"}, headers={"X-Demo-User": "guest-rl"})
    assert int(r.headers["retry-after"]) >= 1
    other = client.post("/api/posts/p1/answer", json={"text": "hello world"}, headers={"X-Demo-User": "guest-other"})
    assert other.status_code != 429                                                                  # limits are per identity


def test_daily_answer_cap_and_auth_rate_limit(client, google, monkeypatch):
    monkeypatch.setenv("RL_ANSWERS_PER_MIN", "50")
    monkeypatch.setenv("RL_ANSWERS_PER_DAY", "4")
    monkeypatch.setenv("RL_AUTH_PER_MIN", "3")
    get_platform.cache_clear()
    codes = [client.post("/api/posts/p1/answer", json={"text": "hello world"}, headers={"X-Demo-User": "guest-day"}).status_code for _ in range(6)]
    assert [c == 429 for c in codes] == [False] * 4 + [True, True]
    logins = [client.post("/api/auth/google", json={"credential": _cred("tok-parent")}).status_code for _ in range(5)]
    assert logins == [200, 200, 200, 429, 429]
