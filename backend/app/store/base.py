"""Tiny document-store PORT. Collections may be paths, e.g. 'users/u1/activity'."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

_INSTANCE = None


class Database(ABC):
    name = "base"

    @abstractmethod
    def get(self, collection: str, doc_id: str) -> Optional[dict]: ...
    @abstractmethod
    def put(self, collection: str, doc_id: str, data: dict) -> dict: ...
    @abstractmethod
    def query(self, collection: str, **filters: Any) -> list[dict]: ...
    @abstractmethod
    def delete(self, collection: str, doc_id: str) -> None: ...

    def update(self, collection: str, doc_id: str, patch: dict) -> dict:
        cur = self.get(collection, doc_id) or {}
        cur.update(patch)
        return self.put(collection, doc_id, cur)


def get_db() -> Database:
    global _INSTANCE
    if _INSTANCE is None:
        from ..config import get_settings
        if get_settings().DB_BACKEND == "firestore":
            from .firestore_db import FirestoreDatabase
            _INSTANCE = FirestoreDatabase()
        else:
            from .memory_db import MemoryDatabase
            _INSTANCE = MemoryDatabase()
    return _INSTANCE


def reset_db() -> None:
    """Tests only."""
    global _INSTANCE
    _INSTANCE = None
    from .memory_db import _STORE
    _STORE.clear()
