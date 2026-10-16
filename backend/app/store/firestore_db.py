"""
Cloud Firestore backend (Application Default Credentials on Cloud Run).

Cost-aware: Firestore bills per document read, so every query that can be bounded is bounded.
  query_ex(order_by=…, limit=N)  uses a Firestore ORDER BY + LIMIT (N reads, not the whole collection).
  With equality filters AND an order_by Firestore needs a composite index. If it exists (deploy/01_setup_gcp.sh creates the
  one the feed uses) it is used; if not, we fall back to ORDER BY + LIMIT on the single-field index and filter in Python.
  count() uses Firestore's server-side aggregation (one read per 1000 matches) instead of streaming documents.
"""
from __future__ import annotations

import logging

from .base import Database

log = logging.getLogger("wotnow.firestore")


class FirestoreDatabase(Database):
    name = "firestore"

    def __init__(self) -> None:
        from google.cloud import firestore  # type: ignore
        self.client = firestore.Client()
        self._no_index: set = set()          # (collection, order_by, filter names) known to lack a composite index

    # ---------- basic ops ----------
    def get(self, collection, doc_id):
        snap = self.client.collection(collection).document(doc_id).get()
        return snap.to_dict() if snap.exists else None

    def put(self, collection, doc_id, data):
        self.client.collection(collection).document(doc_id).set(data)
        return data

    def delete(self, collection, doc_id):
        self.client.collection(collection).document(doc_id).delete()

    def query(self, collection, **filters):
        return self.query_ex(collection, filters)

    # ---------- bounded queries ----------
    def query_ex(self, collection, filters=None, order_by=None, desc=False, limit=None):
        filters = filters or {}
        base = self.client.collection(collection)
        if not order_by:
            q = base
            for k, v in filters.items():
                q = q.where(k, "==", v)
            if limit:
                q = q.limit(int(limit))
            return [d.to_dict() for d in q.stream()]

        direction = "DESCENDING" if desc else "ASCENDING"
        key = (collection, order_by, tuple(sorted(filters)))
        if filters and key not in self._no_index:
            try:
                q = base
                for k, v in filters.items():
                    q = q.where(k, "==", v)
                q = q.order_by(order_by, direction=direction)
                if limit:
                    q = q.limit(int(limit))
                return [d.to_dict() for d in q.stream()]
            except Exception as exc:
                if type(exc).__name__ != "FailedPrecondition":      # anything but "index missing" is a real error
                    raise
                self._no_index.add(key)
                log.warning("Firestore composite index missing for %s (%s + %s); using the slower path. "
                            "Create it with deploy/01_setup_gcp.sh", collection, ",".join(filters), order_by)

        # No filters (uses the automatic single-field index), or no composite index: over-fetch, then filter in Python.
        q = base.order_by(order_by, direction=direction)
        if limit:
            q = q.limit(int(limit) * (4 if filters else 1))
        rows = [d.to_dict() for d in q.stream()]
        if filters:
            rows = [r for r in rows if all(r.get(k) == v for k, v in filters.items())]
        return rows[:limit] if limit else rows

    def count(self, collection, **filters):
        q = self.client.collection(collection)
        for k, v in filters.items():
            q = q.where(k, "==", v)
        try:
            return int(q.count().get()[0][0].value)
        except Exception:                      # old client library or transient error: count by streaming
            return len(list(q.stream()))
