"""
FirestoreDatabase against an in-memory fake of the Firestore client (the real service can't be reached from tests).
The fake enforces the rules that matter: equality+order_by needs a composite index, ORDER BY drops documents that lack the
field, and every document returned by a query or get() counts as a billed read.
"""
import pytest

from app.store.firestore_db import FirestoreDatabase
from app.store.memory_db import MemoryDatabase


class FailedPrecondition(Exception):
    """Same class name as google.api_core.exceptions.FailedPrecondition (the code matches on the name)."""


class Snap:
    def __init__(self, data): self._d = data; self.exists = data is not None
    def to_dict(self): return dict(self._d) if self._d is not None else None


class Agg:
    def __init__(self, n): self.value = n


class FakeQuery:
    def __init__(self, client, coll, wheres=(), order=None, lim=None):
        self.c, self.coll, self.wheres, self.order, self.lim = client, coll, tuple(wheres), order, lim

    def where(self, field, op, value):
        assert op == "=="
        return FakeQuery(self.c, self.coll, self.wheres + ((field, value),), self.order, self.lim)

    def order_by(self, field, direction="ASCENDING"):
        assert direction in ("ASCENDING", "DESCENDING")
        return FakeQuery(self.c, self.coll, self.wheres, (field, direction), self.lim)

    def limit(self, n):
        return FakeQuery(self.c, self.coll, self.wheres, self.order, n)

    def _rows(self):
        rows = list(self.c.data.get(self.coll, {}).values())
        for f, v in self.wheres:
            rows = [r for r in rows if r.get(f) == v]
        return rows

    def stream(self):
        if self.wheres and self.order and (self.coll, self.order[0], tuple(sorted(f for f, _ in self.wheres))) not in self.c.indexes:
            raise FailedPrecondition("The query requires an index.")
        rows = self._rows()
        if self.order:
            f, d = self.order
            rows = sorted([r for r in rows if f in r], key=lambda r: r[f], reverse=(d == "DESCENDING"))
        if self.lim:
            rows = rows[: self.lim]
        self.c.reads += len(rows)
        return iter([Snap(r) for r in rows])

    def count(self):
        n = len(self._rows())
        outer = self

        class _Agg:
            def get(self_inner):
                if outer.c.count_broken:
                    raise RuntimeError("aggregation unsupported")
                outer.c.agg_calls += 1
                return [[Agg(n)]]
        return _Agg()


class FakeDoc:
    def __init__(self, client, coll, doc_id): self.c, self.coll, self.id = client, coll, doc_id
    def get(self):
        self.c.reads += 1
        return Snap(self.c.data.get(self.coll, {}).get(self.id))
    def set(self, data): self.c.data.setdefault(self.coll, {})[self.id] = dict(data)
    def delete(self): self.c.data.get(self.coll, {}).pop(self.id, None)


class FakeCollection(FakeQuery):
    def document(self, doc_id): return FakeDoc(self.c, self.coll, doc_id)


class FakeClient:
    def __init__(self, indexes=()):
        self.data, self.reads, self.agg_calls, self.indexes, self.count_broken = {}, 0, 0, set(indexes), False
    def collection(self, path): return FakeCollection(self, path)


def make(indexes=()):
    db = FirestoreDatabase.__new__(FirestoreDatabase)
    db.client = FakeClient(indexes)
    db._no_index = set()
    return db


def fill(*dbs):
    for db in dbs:
        for i in range(30):
            db.put("posts", f"p{i:02d}", {"id": f"p{i:02d}", "status": "live" if i % 3 else "pending", "agent": "ember" if i % 2 else "pulse",
                                          "createdAt": f"2026-10-{1 + i // 2:02d}T{i:02d}:00:00"})


def ids(rows):
    return [r["id"] for r in rows]


def test_basic_ops_and_unbounded_queries():
    db = make()
    db.put("users", "u1", {"id": "u1", "x": 1})
    assert db.get("users", "u1") == {"id": "u1", "x": 1} and db.get("users", "nope") is None
    db.update("users", "u1", {"y": 2})
    assert db.get("users", "u1") == {"id": "u1", "x": 1, "y": 2}
    fill(db)
    assert len(db.query("posts")) == 30 and len(db.query("posts", status="pending")) == 10
    db.delete("users", "u1")
    assert db.get("users", "u1") is None


@pytest.mark.parametrize("indexed", [True, False])
def test_query_ex_matches_the_other_backends(indexed):
    fs = make({("posts", "createdAt", ("status",))} if indexed else ())
    mem = MemoryDatabase()
    fill(fs, mem)
    ordered = ({"filters": {"status": "live"}, "order_by": "createdAt", "desc": True, "limit": 7},
               {"filters": {"status": "live", "agent": "ember"}, "order_by": "createdAt", "desc": True, "limit": 5},
               {"filters": {"agent": "pulse"}, "order_by": "createdAt", "desc": False, "limit": 4},
               {"order_by": "createdAt", "desc": True, "limit": 6},
               {"order_by": "createdAt", "desc": False})
    for kw in ordered:
        got = fs.query_ex("posts", **kw)
        assert ids(got) == ids(mem.query_ex("posts", **kw)), kw
    for kw in ({"filters": {"status": "pending"}, "limit": 3}, {"filters": {"status": "pending"}}):
        got, want = fs.query_ex("posts", **kw), mem.query_ex("posts", **kw)
        assert all(r["status"] == "pending" for r in got) and len(got) == len(want) == (3 if kw.get("limit") else 10)


def test_ordering_skips_documents_that_lack_the_field():
    fs = make()
    fill(fs)
    fs.put("posts", "no-date", {"id": "no-date", "status": "live"})
    assert "no-date" not in ids(fs.query_ex("posts", order_by="createdAt", desc=True, limit=100))      # Firestore semantics: ORDER BY needs the field
    assert "no-date" in ids(fs.query("posts"))


def test_ordered_limited_query_reads_only_what_it_needs():
    fs = make({("posts", "createdAt", ("status",))})
    fill(fs)
    fs.client.reads = 0
    assert len(fs.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=5)) == 5
    assert fs.client.reads == 5                                     # composite index present: exactly the 5 documents returned
    fs.client.reads = 0
    assert len(fs.query_ex("posts", order_by="createdAt", desc=True, limit=5)) == 5
    assert fs.client.reads == 5                                     # no filters: single-field index, still bounded


def test_missing_composite_index_falls_back_and_remembers():
    fs = make()                                                     # no composite index
    fill(fs)
    fs.client.reads = 0
    got = fs.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=5)
    mem = MemoryDatabase()
    fill(mem)
    assert ids(got) == ids(mem.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=5))      # same answer as with the index
    assert fs.client.reads == 20                                    # over-fetch: 4 × limit, filtered in Python
    assert ("posts", "createdAt", ("status",)) in fs._no_index
    fs.client.reads = 0
    fs.query_ex("posts", {"status": "live"}, order_by="createdAt", desc=True, limit=5)
    assert fs.client.reads == 20                                    # remembered: no failed attempt is repeated


def test_other_errors_are_not_swallowed():
    fs = make({("posts", "createdAt", ("status",))})

    class Boom(Exception):
        pass
    orig = FakeQuery.stream

    def bad(self):
        raise Boom("quota exceeded")
    FakeQuery.stream = bad
    try:
        with pytest.raises(Boom):
            fs.query_ex("posts", {"status": "live"}, order_by="createdAt", limit=3)
    finally:
        FakeQuery.stream = orig


def test_count_uses_aggregation_and_falls_back():
    fs = make()
    fill(fs)
    fs.client.reads = 0
    assert fs.count("posts") == 30 and fs.count("posts", status="pending") == 10
    assert fs.client.agg_calls == 2 and fs.client.reads == 0        # server-side count: no documents billed
    fs.client.count_broken = True
    assert fs.count("posts", status="pending") == 10                # old client / transient error: count by streaming
