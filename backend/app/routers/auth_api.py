"""Sign-in (Google, plus a test-only email sign-in), sessions, the parent's account and the child profiles."""
from __future__ import annotations

import re
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, Field

from ..auth import get_account_required
from ..core import accounts, security
from ..core.settings import get_platform
from ..services import users

router = APIRouter(prefix="/api", tags=["auth"])
EMAIL = re.compile(r"^[^@\s]{1,64}@[^@\s]{1,120}\.[^@\s]{2,24}$")


class GoogleIn(BaseModel):
    credential: str = Field(min_length=20, max_length=4096)


class DevLoginIn(BaseModel):
    email: str = Field(min_length=5, max_length=190)
    name: str = Field(default="", max_length=60)


class ChildIn(BaseModel):
    nickname: str = Field(min_length=3, max_length=16)
    avatar: str = Field(default="🦊", max_length=8)
    grade: int = Field(default=8, ge=3, le=12)
    city: str = Field(default="Pune", max_length=40)
    country: Optional[str] = Field(default="India", max_length=50)
    follows: Optional[list[str]] = None


class ChildPatch(BaseModel):
    nickname: Optional[str] = Field(default=None, min_length=3, max_length=16)
    avatar: Optional[str] = Field(default=None, max_length=8)
    grade: Optional[int] = Field(default=None, ge=3, le=12)
    city: Optional[str] = Field(default=None, max_length=40)
    country: Optional[str] = Field(default=None, max_length=50)
    follows: Optional[list[str]] = None


def _session(acc: dict) -> dict:
    return {"token": security.issue_session(acc), "account": accounts.public_account(acc)}


@router.get("/auth/config")
async def auth_config():
    ps = get_platform()
    return {"authMode": ps.auth_mode, "googleEnabled": ps.google_enabled, "googleClientId": ps.google_client_id if ps.google_enabled else "",
            "allowDemo": ps.allow_demo or ps.auth_mode == "dev", "devLogin": ps.dev_login_enabled, "adminTokenLogin": ps.admin_token_login,
            "maxChildren": ps.max_children}


@router.get("/auth/check-nickname")
async def check_nickname(nickname: str, exclude: Optional[str] = None):
    clean = re.sub(r"[^A-Za-z0-9]", "", str(nickname)).strip()
    if len(clean) < 3:
        return {"available": False, "message": "At least 3 characters required"}
    taken = users.is_nickname_taken(clean, exclude_uid=exclude)
    return {"available": not taken, "message": f"'{clean}' is already taken" if taken else "Available"}


@router.post("/auth/google")
async def auth_google(body: GoogleIn):
    if not get_platform().google_enabled:
        raise HTTPException(503, "Google sign-in is not enabled on this server")
    try:
        info = await run_in_threadpool(security.verify_google_credential, body.credential)
    except Exception as exc:
        raise HTTPException(401, f"Google sign-in failed: {str(exc)[:120]}")
    if not info.get("email_verified"):
        raise HTTPException(401, "Your Google email is not verified")
    return _session(accounts.upsert_google(info))


@router.post("/auth/dev-login")
async def auth_dev_login(body: DevLoginIn):
    """TEST ONLY: sign in as any email with no password, so accounts, children and sessions can be tried on a server that
    Google can't reach (the build-host). Off unless DEV_LOGIN=true, and always off on Cloud Run. Never grants admin."""
    if not get_platform().dev_login_enabled:
        raise HTTPException(404, "Not found")
    email = body.email.strip().lower()
    if not EMAIL.match(email):
        raise HTTPException(422, "Enter a valid email address")
    return _session(accounts.upsert_dev(email, body.name.strip()))


@router.post("/auth/refresh")
async def auth_refresh(acc: dict = Depends(get_account_required)):
    """A fresh 14-day token for a still-valid session (the app calls this when its token is a few days old)."""
    return {"token": security.issue_session(acc)}


@router.post("/auth/logout-all")
async def auth_logout_all(acc: dict = Depends(get_account_required)):
    """Sign out of every device: all tokens issued so far stop working."""
    accounts.bump_epoch(acc)
    return {"ok": True}


@router.get("/account")
async def get_account(acc: dict = Depends(get_account_required)):
    return accounts.public_account(acc)


@router.post("/account/children")
async def add_child(body: ChildIn, acc: dict = Depends(get_account_required)):
    child = accounts.create_child(acc, body.model_dump())
    return {"child": child, "account": accounts.public_account(accounts.get_account(acc["id"]))}


@router.put("/account/children/{child_id}")
async def edit_child(child_id: str, body: ChildPatch, acc: dict = Depends(get_account_required)):
    accounts.update_child(acc, child_id, body.model_dump(exclude_none=True))
    return accounts.public_account(accounts.get_account(acc["id"]))


@router.delete("/account/children/{child_id}")
async def remove_child(child_id: str, acc: dict = Depends(get_account_required)):
    accounts.delete_child(acc, child_id)
    return accounts.public_account(accounts.get_account(acc["id"]))


@router.delete("/account")
async def remove_account(acc: dict = Depends(get_account_required)):
    accounts.delete_account(acc)
    return {"deleted": True}
