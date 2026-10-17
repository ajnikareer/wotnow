"""
The sign-in / sign-up / sign-out flow: test sign-in (DEV_LOGIN), session refresh, sign out everywhere, editing children,
guest profiles, the protected shared demo student, derived session secret, and the demo's per-visitor rate limits.
"""
import time

import pytest

from app.core import security
from app.core.settings import get_platform
from app.store.base import get_db


@pytest.fixture()
def client(v3_client):
    return v3_client


@pytest.fixture()
def devlogin(monkeypatch):
    monkeypatch.setenv("DEV_LOGIN", "true")
    get_platform.cache_clear()


def dev(client, email="Mum@Example.com", name="Mum"):
    r = client.post("/api/auth/dev-login", json={"email": email, "name": name})
    assert r.status_code == 200, r.text
    return {"Authorization": "Bearer " + r.json()["token"]}, r.json()["account"]


# ------------------------------------------------------------------ test sign-in
def test_dev_login_is_off_by_default(client):
    assert client.post("/api/auth/dev-login", json={"email": "a@b.co"}).status_code == 404
    assert client.get("/api/auth/config").json()["devLogin"] is False
    assert client.get("/api/info").json()["devLogin"] is False


def test_dev_login_creates_one_account_per_email(client, devlogin):
    assert client.get("/api/auth/config").json()["devLogin"] is True
    h1, a1 = dev(client, "Mum@Example.com")
    assert a1["email"] == "mum@example.com" and a1["name"] == "Mum" and a1["provider"] == "dev" and a1["isAdmin"] is False and a1["children"] == []
    h2, a2 = dev(client, "mum@example.com")                                   # same email, any capitalisation → the same account
    assert a2["id"] == a1["id"]
    _, a3 = dev(client, "dad@example.com", "")
    assert a3["id"] != a1["id"] and a3["name"] == "dad"                       # the name defaults to the part before the @
    for bad in ("nope", "a@b", "@b.co", "a b@c.co", "x" * 200 + "@b.co"):
        assert client.post("/api/auth/dev-login", json={"email": bad}).status_code in (422,), bad


def test_dev_login_never_runs_on_cloud_run(client, monkeypatch):
    monkeypatch.setenv("DEV_LOGIN", "true")
    monkeypatch.setenv("K_SERVICE", "wotnow")                                  # Cloud Run sets this
    get_platform.cache_clear()
    assert get_platform().dev_login is True and get_platform().dev_login_enabled is False
    assert client.post("/api/auth/dev-login", json={"email": "a@b.co"}).status_code == 404
    assert client.get("/api/auth/config").json()["devLogin"] is False


def test_dev_accounts_are_never_admin(client, devlogin, monkeypatch):
    monkeypatch.setenv("ADMIN_EMAILS", "boss@example.com")
    get_platform.cache_clear()
    h, acc = dev(client, "boss@example.com")
    assert acc["isAdmin"] is False
    assert client.get("/api/admin/overview", headers=h).status_code == 403
    assert client.get("/api/admin/overview", headers={"X-Admin-Token": "t"}).status_code == 200      # the token still works


def test_full_signup_flow_with_the_test_sign_in(client, devlogin):
    """sign up → add a child → use the app as that child → switch child → sign out everywhere → sign in again."""
    h, acc = dev(client)
    assert client.get("/api/me", headers=h).status_code == 409                # signed in, but no child yet
    kid = client.post("/api/account/children", headers=h, json={"nickname": "CleverFox", "grade": 8, "city": "Pune"}).json()["child"]
    assert client.get("/api/me", headers=h).json()["id"] == kid["id"]
    kid2 = client.post("/api/account/children", headers=h, json={"nickname": "BraveOwl", "grade": 10}).json()["child"]
    assert client.get("/api/me", headers={**h, "X-Child": kid2["id"]}).json()["nickname"] == "BraveOwl"
    assert [c["nickname"] for c in client.get("/api/account", headers=h).json()["children"]] == ["CleverFox", "BraveOwl"]
    # the same email signing in again (another device / a later visit) gets the same family back
    h_again, acc_again = dev(client)
    assert acc_again["id"] == acc["id"] and len(acc_again["children"]) == 2


# ------------------------------------------------------------------ sessions
def test_logout_all_invalidates_every_token_but_only_for_that_account(client, devlogin):
    h_phone, acc = dev(client, "mum@example.com")
    h_laptop, _ = dev(client, "mum@example.com")                               # a second device
    h_other, _ = dev(client, "dad@example.com")
    assert client.get("/api/account", headers=h_phone).status_code == 200 and client.get("/api/account", headers=h_laptop).status_code == 200
    assert client.post("/api/auth/logout-all", headers=h_phone).json() == {"ok": True}
    for h in (h_phone, h_laptop):
        r = client.get("/api/account", headers=h)
        assert r.status_code == 401 and "signed out" in r.json()["detail"].lower()
    assert client.get("/api/account", headers=h_other).status_code == 200      # dad is unaffected
    h_new, _ = dev(client, "mum@example.com")                                  # signing in again works
    assert client.get("/api/account", headers=h_new).status_code == 200
    assert client.post("/api/auth/logout-all").status_code == 401              # needs a session


def test_refresh_gives_a_working_new_token(client, devlogin):
    h, acc = dev(client)
    r = client.post("/api/auth/refresh", headers=h)
    assert r.status_code == 200
    fresh = {"Authorization": "Bearer " + r.json()["token"]}
    assert client.get("/api/account", headers=fresh).json()["id"] == acc["id"]
    assert client.post("/api/auth/refresh").status_code == 401
    assert client.post("/api/auth/refresh", headers={"Authorization": "Bearer junk"}).status_code == 401
    client.post("/api/auth/logout-all", headers=h)
    assert client.post("/api/auth/refresh", headers=fresh).status_code == 401  # a signed-out session can't be refreshed


def test_token_carries_the_epoch_and_old_tokens_without_one_still_work(client, devlogin):
    h, acc = dev(client)
    payload = security.verify_session(h["Authorization"].split(" ", 1)[1])
    assert payload["ep"] == 0 and payload["sub"] == acc["id"]
    old = security.issue_session({"id": acc["id"], "email": acc["email"]})     # an account dict without an epoch → ep 0
    assert client.get("/api/account", headers={"Authorization": "Bearer " + old}).status_code == 200


def test_session_secret_survives_restarts_without_session_secret(monkeypatch):
    monkeypatch.delenv("SESSION_SECRET")
    monkeypatch.setenv("JOBS_TOKEN", "my-jobs-token")
    get_platform.cache_clear()
    s1 = get_platform().session_secret
    tok = security.issue_session({"id": "a_1"})
    get_platform.cache_clear()                                                 # "container restart"
    assert get_platform().session_secret == s1 and security.verify_session(tok)["sub"] == "a_1"
    monkeypatch.setenv("JOBS_TOKEN", "another-token")
    get_platform.cache_clear()
    assert get_platform().session_secret != s1 and security.verify_session(tok) is None
    monkeypatch.setenv("SESSION_SECRET", "explicit")
    get_platform.cache_clear()
    assert get_platform().session_secret == "explicit"


# ------------------------------------------------------------------ children
def test_edit_child(client, devlogin):
    h, _ = dev(client)
    cid = client.post("/api/account/children", headers=h, json={"nickname": "CleverFox", "grade": 6, "city": "Pune"}).json()["child"]["id"]
    r = client.put(f"/api/account/children/{cid}", headers=h, json={"nickname": "SwiftOtter", "grade": 10, "city": "Hyderabad", "avatar": "🦦"})
    assert r.status_code == 200
    kid = r.json()["children"][0]
    assert (kid["nickname"], kid["grade"], kid["band"], kid["city"], kid["avatar"]) == ("SwiftOtter", 10, "senior", "Hyderabad", "🦦")
    assert client.put(f"/api/account/children/{cid}", headers=h, json={}).status_code == 200                # nothing to change is fine
    assert client.put(f"/api/account/children/{cid}", headers=h, json={"city": "Delhi"}).json()["children"][0]["nickname"] == "SwiftOtter"
    for bad in ({"nickname": "ab"}, {"nickname": "x" * 17}, {"grade": 2}, {"grade": 13}):
        assert client.put(f"/api/account/children/{cid}", headers=h, json=bad).status_code == 422, bad
    assert client.put("/api/account/children/c_nope", headers=h, json={"city": "x"}).status_code == 404
    other, _ = dev(client, "dad@example.com")
    assert client.put(f"/api/account/children/{cid}", headers=other, json={"city": "x"}).status_code == 404   # not your child
    assert client.put(f"/api/account/children/{cid}", json={"city": "x"}).status_code == 401


def test_delete_account_removes_children_and_logs_everyone_out(client, devlogin):
    h, _ = dev(client)
    cid = client.post("/api/account/children", headers=h, json={"nickname": "CleverFox"}).json()["child"]["id"]
    assert client.delete("/api/account", headers=h).json() == {"deleted": True}
    assert get_db().get("users", cid) is None
    assert client.get("/api/account", headers=h).status_code == 401
    h2, acc = dev(client)                                                       # signing up again starts a new, empty family
    assert acc["children"] == []


# ------------------------------------------------------------------ guests and the shared demo student
def test_guest_profiles_follow_the_auth_mode(client, monkeypatch):
    ps = get_platform()
    assert ps.auth_mode == "dev" and ps.allow_guests is True                   # build-host / local: guests allowed
    assert client.get("/api/me", headers={"X-Demo-User": "guest-1"}).status_code == 200
    monkeypatch.setenv("AUTH_MODE", "google")
    get_platform.cache_clear()
    assert get_platform().allow_guests is False
    assert client.get("/api/me", headers={"X-Demo-User": "guest-1"}).status_code == 403
    assert client.get("/api/me", headers={"X-Demo-User": "demo-student"}).status_code == 200
    assert client.get("/api/info").json()["guestProfiles"] is False


def test_demo_student_cannot_be_changed(client):
    demo = {"X-Demo-User": "demo-student"}
    assert client.get("/api/me", headers=demo).json()["id"] == "demo-student"
    for patch in ({"nickname": "Hacker"}, {"grade": 12}, {"city": "Mars"}, {"nickname": "x", "follows": []}, {"avatar": "💀"}):
        r = client.post("/api/me", headers=demo, json=patch)
        assert r.status_code == 403 and "demo student" in r.json()["detail"], patch
    assert client.get("/api/me", headers=demo).json()["nickname"] == "NewLearner"        # untouched
    assert client.post("/api/me", headers=demo, json={"follows": ["ember"]}).status_code == 200   # Follow / Unfollow still works
    assert client.delete("/api/me", headers=demo).status_code == 403
    assert client.post("/api/parent/settings", headers=demo, json={"dailyLimit": 5}).status_code == 403
    assert client.post("/api/me", json={"nickname": "Hacker"}).status_code == 403          # no header = the demo student in dev mode
    assert get_db().get("users", "demo-student") is not None


def test_everyone_else_can_still_edit_and_delete(client, devlogin):
    guest = {"X-Demo-User": "guest-edit"}
    assert client.post("/api/me", headers=guest, json={"nickname": "Renamed", "grade": 11}).json()["grade"] == 11
    assert client.post("/api/parent/settings", headers=guest, json={"dailyLimit": 45}).json()["settings"]["dailyLimit"] == 45
    assert client.delete("/api/me", headers=guest).json() == {"deleted": True}
    h, _ = dev(client)
    cid = client.post("/api/account/children", headers=h, json={"nickname": "CleverFox"}).json()["child"]["id"]
    assert client.post("/api/me", headers=h, json={"city": "Delhi"}).json()["city"] == "Delhi"
    assert client.post("/api/parent/settings", headers=h, json={"dailyLimit": 20}).json()["settings"]["dailyLimit"] == 20
    assert client.delete("/api/me", headers=h).json() == {"deleted": True}
    assert get_db().get("users", cid) is None
    assert client.get("/api/me", headers=h).status_code == 409                              # the child is gone, the account remains


def test_the_me_router_shadows_the_old_endpoints():
    from app.main import app
    for method, path in (("POST", "/api/me"), ("DELETE", "/api/me"), ("POST", "/api/parent/settings")):
        routes = [r for r in app.routes if getattr(r, "path", None) == path and method in getattr(r, "methods", set())]
        assert routes and routes[0].endpoint.__module__.endswith("routers.me_api"), (method, path)


def test_demo_defaults_are_fixed_at_startup(client):
    from app.services import demo
    assert demo.ensure_demo_defaults() is False                                  # no demo student yet: nothing to do
    u = {"id": "demo-student", "parentSettings": {"dailyLimit": 30, "quietHours": "22:00 – 06:00", "topics": {"fire": True}}}
    get_db().put("users", "demo-student", u)
    assert demo.ensure_demo_defaults() is True
    s = get_db().get("users", "demo-student")["parentSettings"]
    assert s["quietHours"] == "" and s["dailyLimit"] == 180 and s["topics"] == {"fire": True}   # other settings untouched
    assert demo.ensure_demo_defaults() is False                                  # idempotent
    get_db().update("users", "demo-student", {"parentSettings": {"dailyLimit": 500, "quietHours": ""}})
    assert demo.ensure_demo_defaults() is False                                  # an already generous limit is left alone


def test_demo_defaults_run_when_the_app_starts(monkeypatch):
    from fastapi.testclient import TestClient
    from app import main
    get_db().put("users", "demo-student", {"id": "demo-student", "parentSettings": {"dailyLimit": 30, "quietHours": "22:00 – 06:00"}})
    with TestClient(main.app):
        pass
    assert get_db().get("users", "demo-student")["parentSettings"] == {"dailyLimit": 180, "quietHours": ""}


# ------------------------------------------------------------------ rate limits
def test_the_demo_student_is_limited_per_visitor_not_for_everyone(client, monkeypatch):
    monkeypatch.setenv("RL_ANSWERS_PER_MIN", "2")
    monkeypatch.setenv("TRUST_PROXY", "true")
    get_platform.cache_clear()

    def ans(ip, who="demo-student"):
        return client.post("/api/posts/p1/answer", json={"text": "hello world"}, headers={"X-Demo-User": who, "X-Forwarded-For": ip}).status_code
    assert [ans("1.1.1.1") == 429 for _ in range(3)] == [False, False, True]     # visitor A hits the limit …
    assert ans("2.2.2.2") != 429                                                  # … visitor B is not affected
    assert [ans("3.3.3.3", "guest-x") == 429 for _ in range(3)] == [False, False, True]
    assert ans("4.4.4.4", "guest-x") == 429                                       # a named guest id is still one shared bucket


def test_sign_in_endpoints_share_the_login_rate_limit(client, devlogin, monkeypatch):
    monkeypatch.setenv("RL_AUTH_PER_MIN", "3")
    get_platform.cache_clear()
    codes = [client.post("/api/auth/dev-login", json={"email": f"p{i}@example.com"}).status_code for i in range(5)]
    assert codes == [200, 200, 200, 429, 429]
    assert client.post("/api/auth/refresh").status_code == 429                    # refresh / logout-all count too
