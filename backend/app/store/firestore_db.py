"""Cloud Firestore backend (Application Default Credentials on Cloud Run)."""
from __future__ import annotations

from .base import Database


class FirestoreDatabase(Database):
    name = "firestore"

    def __init__(self) -> None:
        from google.cloud import firestore  # type: ignore
        self.client = firestore.Client()

    def get(self, collection, doc_id):
        snap = self.client.collection(collection).document(doc_id).get()
        return snap.to_dict() if snap.exists else None

    def put(self, collection, doc_id, data):
        self.client.collection(collection).document(doc_id).set(data)
        return data

    def query(self, collection, **filters):
        q = self.client.collection(collection)
        for k, v in filters.items():
            q = q.where(k, "==", v)
        return [d.to_dict() for d in q.stream()]

    def delete(self, collection, doc_id):
        self.client.collection(collection).document(doc_id).delete()
