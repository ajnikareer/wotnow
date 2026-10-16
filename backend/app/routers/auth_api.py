"""Google sign-in, the parent's account, and child profiles."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, Field

from ..auth import get_account_required
from ..core import accounts, security
from ..core.settings import get_platform

router = APIRouter(prefix="/api", tags=["auth"])


class GoogleIn(BaseModel):
    credential: str = Field(min_length=20, max_length=4096)


class ChildIn(BaseModel):
    nickname: str = Field(min_length=3, max_length=16)
    avatar: str = Field(default="🦊", max_length=8)
    grade: int = Field(default=8, ge=3, le=12)
    city: str = Field(default="Pune", max_length=40)


@router.get("/auth/config")
async def auth_config():
    ps = get_platform()
    return {"authMode": ps.auth_mode, "googleEnabled": ps.google_enabled, "googleClientId": ps.google_client_id if ps.google_enabled else "",
            "allowDemo": ps.allow_demo or ps.auth_mode == "dev", "adminTokenLogin": ps.admin_token_login, "maxChildren": ps.max_children}


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
    acc = accounts.upsert_google(info)
    return {"token": security.issue_session(acc), "account": accounts.public_account(acc)}


@router.get("/account")
async def get_account(acc: dict = Depends(get_account_required)):
    return accounts.public_account(acc)


@router.post("/account/children")
async def add_child(body: ChildIn, acc: dict = Depends(get_account_required)):
    child = accounts.create_child(acc, body.model_dump())
    return {"child": child, "account": accounts.public_account(accounts.get_account(acc["id"]))}


@router.delete("/account/children/{child_id}")
async def remove_child(child_id: str, acc: dict = Depends(get_account_required)):
    accounts.delete_child(acc, child_id)
    return accounts.public_account(accounts.get_account(acc["id"]))


@router.delete("/account")
async def remove_account(acc: dict = Depends(get_account_required)):
    accounts.delete_account(acc)
    return {"deleted": True}
