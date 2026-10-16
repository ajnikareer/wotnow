"""SQLite persistence store, query_ex, leases."""
import threading

from app.store.memory_db import MemoryDatabase
from app.store.sqlite_db import SqliteDatabase


def _fill(db):
    for i in range(6):
        db.put("posts", f"p{i}", {"id": f"p{i}", "agentId": "ember" if i % 2 == 0 else "pulse", "status": "live" if i != 3 else "pending",
                                  "createdAt": f"2026-10-0{i + 1}T10:00:00", "n": i, "flag": i % 2 == 0})
    db.put("users/u1/activity", "a1", {"id": "a1", "kind": "answer"})
    db.put("users", "u1", {"id": "u1"})


def test_sqlite_basic_and_collections_do_not_mix(tmp_path):
    db = SqliteDatabase(str(tmp_path / "w.db"))
    _fill(db)
    assert db.get("posts", "p2")["agentId"] == "ember" and db.get("posts", "nope") is None
    assert [d["id"] for d in db.query("users")] == ["u1"]              # not users/u1/activity
    assert len(db.query("users/u1/activity")) == 1
    db.update("posts", "p2", {"title": "x"})
    assert db.get("posts", "p2")["title"] == "x" and db.get("posts", "p2")["agentId"] == "ember"
    db.delete("posts", "p2")
    assert db.get("posts", "p2") is None


def test_sqlite_query_filters_and_ordering(tmp_path):
    db = SqliteDatabase(str(tmp_path / "w.db"))
    _fill(db)
    assert {d["id"] for d in db.query("posts", agentId="ember")} == {"p0", "p2", "p4"}
    assert {d["id"] for d in db.query("posts", flag=True)} == {"p0", "p2", "p4"}            # bool filter handled in Python
    assert db.count("posts", status="pending") == 1 and db.count("posts") == 6
    top = db.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=2)
    assert [d["id"] for d in top] == ["p5", "p4"]
    asc = db.query_ex("posts", {"agentId": "pulse"}, order_by="n")
    assert [d["id"] for d in asc] == ["p1", "p3", "p5"]
    mixed = db.query_ex("posts", {"flag": True}, order_by="n", desc=True, limit=2)
    assert [d["id"] for d in mixed] == ["p4", "p2"]


def test_sqlite_survives_restart_and_handles_unicode(tmp_path):
    path = str(tmp_path / "keep" / "w.db")          # folder is created automatically
    db = SqliteDatabase(path)
    db.put("users", "u1", {"id": "u1", "nickname": "CleverFox", "avatar": "🦊", "text": "नमस्ते"})
    db.close()
    again = SqliteDatabase(path)
    assert again.get("users", "u1")["avatar"] == "🦊" and again.get("users", "u1")["text"] == "नमस्ते"


def test_sqlite_threads(tmp_path):
    db = SqliteDatabase(str(tmp_path / "w.db"))

    def work(k):
        for i in range(40):
            db.put("t", f"{k}-{i}", {"id": f"{k}-{i}", "k": k})
    ts = [threading.Thread(target=work, args=(k,)) for k in range(5)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    assert db.count("t") == 200 and db.count("t", k=3) == 40


def test_lease_is_exclusive_and_expires(tmp_path):
    for db in (SqliteDatabase(str(tmp_path / "l.db")), MemoryDatabase()):
        assert db.acquire_lease("tick", "A", 60) is True
        assert db.acquire_lease("tick", "B", 60) is False        # held by A
        assert db.acquire_lease("tick", "A", 60) is True         # owner can renew
        db.release_lease("tick", "B")                            # not the owner: no effect
        assert db.acquire_lease("tick", "B", 60) is False
        db.release_lease("tick", "A")
        assert db.acquire_lease("tick", "B", 0.01) is True
        import time
        time.sleep(0.05)
        assert db.acquire_lease("tick", "C", 60) is True         # expired lease can be taken


def test_default_query_ex_on_memory_store():
    db = MemoryDatabase()
    _fill(db)
    assert [d["id"] for d in db.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=2)] == ["p5", "p4"]


def test_get_db_selects_sqlite_by_env(tmp_path, monkeypatch):
    monkeypatch.setenv("DB_BACKEND", "sqlite")
    monkeypatch.setenv("DB_PATH", str(tmp_path / "env.db"))
    from app.config import get_settings
    from app.store import base
    get_settings.cache_clear(); base.reset_db()
    db = base.get_db()
    assert db.name == "sqlite"
    db.put("a", "b", {"x": 1})
    assert (tmp_path / "env.db").exists()
    base.reset_db(); get_settings.cache_clear()
