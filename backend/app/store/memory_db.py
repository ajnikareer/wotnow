"""In-memory backend for local dev and tests."""
from __future__ import annotations

import copy
from .base import Database

_STORE: dict[str, dict[str, dict]] = {}


class MemoryDatabase(Database):
    name = "memory"

    def get(self, collection, doc_id):
        d = _STORE.get(collection, {}).get(doc_id)
        return copy.deepcopy(d) if d is not None else None

    def put(self, collection, doc_id, data):
        _STORE.setdefault(collection, {})[doc_id] = copy.deepcopy(data)
        return data

    def query(self, collection, **filters):
        out = [copy.deepcopy(d) for d in _STORE.get(collection, {}).values()]
        for k, v in filters.items():
            out = [d for d in out if d.get(k) == v]
        return out

    def delete(self, collection, doc_id):
        _STORE.get(collection, {}).pop(doc_id, None)
