"""
Request auth.

  Student/parent API  (get_uid)
     Bearer <session token>   → a Google account's active child profile (header X-Child picks which one)
     X-Demo-User: <id>        → demo / guest identity (only when ALLOW_DEMO, or AUTH_MODE=dev). 'a_' and 'c_' ids are reserved
                                for real accounts and can never be claimed through this header.
  Admin API           (require_admin)  Google session whose verified email is in ADMIN_EMAILS, or X-Admin-Token (= JOBS_TOKEN)
  Scheduler / jobs    (require_jobs_token)  header X-Jobs-Token
"""
from __future__ import annotations

import hmac
import re
from typing import Optional

from fastapi import Header, HTTPException

from .config import get_settings
from .core import accounts, security
from .core.settings import get_platform

SAFE_ID = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
RESERVED_PREFIXES = ("a_", "c_")


def _bearer(authorization: Optional[str]) -> Optional[str]:
    if authorization and authorization.lower().startswith("bearer "):
        return authorization.split(" ", 1)[1].strip()
    return None


def session_account(authorization: Optional[str]) -> Optional[dict]:
    tok = _bearer(authorization)
    if not tok:
        return None
    sess = security.verify_session(tok)
    if not sess:
        raise HTTPException(401, "Session expired. Please sign in again.")
    acc = accounts.get_account(sess["sub"])
    if not acc:
        raise HTTPException(401, "Account not found. Please sign in again.")
    return acc


async def get_uid(authorization: Optional[str] = Header(default=None), x_demo_user: Optional[str] = Header(default=None),
                  x_child: Optional[str] = Header(default=None)) -> str:
    acc = session_account(authorization)
    if acc is not None:
        child = accounts.resolve_child(acc, x_child)
        if not child:
            raise HTTPException(409, "Create a child profile first")
        return child
    ps = get_platform()
    if ps.auth_mode == "dev" or ps.allow_demo:
        uid = (x_demo_user or ("demo-student" if ps.auth_mode == "dev" else "")).strip()
        if not uid:
            raise HTTPException(401, "Sign in required")
        if not SAFE_ID.match(uid) or uid.startswith(RESERVED_PREFIXES):
            raise HTTPException(400, "bad X-Demo-User")
        return uid
    raise HTTPException(401, "Sign in required")


async def get_account_required(authorization: Optional[str] = Header(default=None)) -> dict:
    acc = session_account(authorization)
    if acc is None:
        raise HTTPException(401, "Sign in required")
    return acc


async def require_admin(authorization: Optional[str] = Header(default=None), x_admin_token: Optional[str] = Header(default=None)) -> str:
    """Returns the admin's identity (email or 'admin-token') for the audit log."""
    acc = session_account(authorization)
    if acc is not None and accounts.is_admin(acc):
        return acc["email"]
    ps = get_platform()
    if x_admin_token and ps.admin_token_login and hmac.compare_digest(x_admin_token, get_settings().JOBS_TOKEN):
        return "admin-token"
    raise HTTPException(403, "Admin access required")


async def require_jobs_token(x_jobs_token: Optional[str] = Header(default=None)) -> None:
    if not x_jobs_token or not hmac.compare_digest(x_jobs_token, get_settings().JOBS_TOKEN):
        raise HTTPException(403, "bad jobs token")
