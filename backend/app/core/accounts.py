"""Accounts (a parent, signed in with Google or the test sign-in) and their child profiles (the students).
Children are normal 'users' documents; an account only lists their ids."""
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
CHILD_FIELDS = ("nickname", "avatar", "grade", "city", "country", "follows")


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())


def get_account(account_id: str) -> Optional[dict]:
    return get_db().get(ACC, account_id)


def save(acc: dict) -> dict:
    get_db().put(ACC, acc["id"], acc)
    return acc


def upsert_google(info: dict) -> dict:
    aid = account_id_for(info["sub"])
    acc = get_account(aid) or {"id": aid, "children": [], "epoch": 0, "createdAt": _now()}
    acc.update(email=info["email"], name=info.get("name", ""), picture=info.get("picture", ""), provider="google",
               emailVerified=bool(info.get("email_verified")), lastLogin=_now())
    acc.pop("dev", None)
    return save(acc)


def upsert_dev(email: str, name: str = "") -> dict:
    """The test sign-in (DEV_LOGIN): an account for any email, no password. Never an admin, never on Cloud Run."""
    aid = account_id_for("dev:" + email.lower())
    acc = get_account(aid) or {"id": aid, "children": [], "epoch": 0, "createdAt": _now()}
    acc.update(email=email.lower(), name=name or email.split("@")[0], picture="", provider="dev", dev=True, emailVerified=True, lastLogin=_now())
    return save(acc)


def is_admin(acc: dict) -> bool:
    return (not acc.get("dev")) and bool(acc.get("emailVerified")) and acc.get("email", "").lower() in get_platform().admin_emails


def bump_epoch(acc: dict) -> dict:
    """Invalidates every session token issued so far for this account ("sign out of all devices")."""
    acc["epoch"] = int(acc.get("epoch", 0)) + 1
    return save(acc)


def resolve_child(acc: dict, requested: Optional[str]) -> Optional[str]:
    """The child to act as: the requested one if it belongs to this account, else the first. Children whose profile was
    deleted (for example through DELETE /api/me) are ignored so they are never silently re-created."""
    db = get_db()
    kids = [k for k in acc.get("children", []) if db.get(users.USERS, k)]
    if requested and requested in kids:
        return requested
    return kids[0] if kids else None


def _clean(patch: dict) -> dict:
    return {k: patch[k] for k in CHILD_FIELDS if patch.get(k) not in (None, "")}


def create_child(acc: dict, patch: dict) -> dict:
    if len(acc.get("children", [])) >= get_platform().max_children:
        raise HTTPException(409, f"At most {get_platform().max_children} child profiles per account")
    uid = "c_" + uuid.uuid4().hex[:12]
    u = users.update_profile(users.new_user(uid), _clean(patch))
    acc.setdefault("children", []).append(uid)
    save(acc)
    return users.public(u)


def update_child(acc: dict, child_id: str, patch: dict) -> dict:
    if child_id not in acc.get("children", []):
        raise HTTPException(404, "child not found")
    u = get_db().get(users.USERS, child_id)
    if not u:
        raise HTTPException(404, "child not found")
    return users.public(users.update_profile(u, _clean(patch)))


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
            "provider": acc.get("provider", "google"), "isAdmin": is_admin(acc), "createdAt": acc.get("createdAt", ""),
            "children": kids, "maxChildren": get_platform().max_children}
