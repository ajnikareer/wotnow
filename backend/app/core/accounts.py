"""Google accounts (a parent) and their child profiles (the students). Children are normal 'users' documents."""
from __future__ import annotations

import time
import uuid
from typing import Optional

from fastapi import HTTPException

from ..services import users
from ..store.base import get_db
from .security import account_id_for
from .settings import get_platform

ACC = "accounts"


def get_account(account_id: str) -> Optional[dict]:
    return get_db().get(ACC, account_id)


def save(acc: dict) -> dict:
    get_db().put(ACC, acc["id"], acc)
    return acc


def upsert_google(info: dict) -> dict:
    aid = account_id_for(info["sub"])
    acc = get_account(aid) or {"id": aid, "children": [], "createdAt": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())}
    acc.update(email=info["email"], name=info.get("name", ""), picture=info.get("picture", ""),
               emailVerified=bool(info.get("email_verified")), lastLogin=time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()))
    return save(acc)


def is_admin(acc: dict) -> bool:
    return bool(acc.get("emailVerified")) and acc.get("email", "").lower() in get_platform().admin_emails


def resolve_child(acc: dict, requested: Optional[str]) -> Optional[str]:
    """The child to act as: the requested one if it belongs to this account, else the first. Children whose profile was
    deleted (for example through DELETE /api/me) are ignored so they are never silently re-created."""
    db = get_db()
    kids = [k for k in acc.get("children", []) if db.get(users.USERS, k)]
    if requested and requested in kids:
        return requested
    return kids[0] if kids else None


def create_child(acc: dict, patch: dict) -> dict:
    if len(acc.get("children", [])) >= get_platform().max_children:
        raise HTTPException(409, f"At most {get_platform().max_children} child profiles per account")
    uid = "c_" + uuid.uuid4().hex[:12]
    u = users.new_user(uid)
    clean = {k: patch[k] for k in ("nickname", "avatar", "grade", "city") if patch.get(k) not in (None, "")}
    u = users.update_profile(u, clean)
    acc.setdefault("children", []).append(uid)
    save(acc)
    return users.public(u)


def delete_child(acc: dict, child_id: str) -> None:
    if child_id not in acc.get("children", []):
        raise HTTPException(404, "child not found")
    users.delete_user(child_id)
    acc["children"] = [c for c in acc["children"] if c != child_id]
    save(acc)


def delete_account(acc: dict) -> None:
    for c in list(acc.get("children", [])):
        users.delete_user(c)
    get_db().delete(ACC, acc["id"])


def public_account(acc: dict) -> dict:
    kids = []
    for c in acc.get("children", []):
        u = get_db().get(users.USERS, c)
        if u:
            kids.append(users.public(u))
    return {"id": acc["id"], "email": acc.get("email", ""), "name": acc.get("name", ""), "picture": acc.get("picture", ""),
            "isAdmin": is_admin(acc), "children": kids, "maxChildren": get_platform().max_children}
