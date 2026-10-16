"""
Auth.
AUTH_MODE=firebase : verify 'Authorization: Bearer <Firebase ID token>' (parent's Google account; one family = one uid).
AUTH_MODE=dev      : trust 'X-Demo-User' header (default 'demo-student'). Local/demo only.
"""
from __future__ import annotations

from fastapi import Header, HTTPException

from .config import get_settings

_APP = None


def _firebase():
    global _APP
    if _APP is None:
        import firebase_admin  # type: ignore
        _APP = firebase_admin.get_app() if firebase_admin._apps else firebase_admin.initialize_app()
    return _APP


async def get_uid(authorization: str | None = Header(default=None), x_demo_user: str | None = Header(default=None)) -> str:
    if get_settings().AUTH_MODE != "firebase":
        uid = (x_demo_user or "demo-student").strip()[:64]
        if not uid.replace("-", "").replace("_", "").isalnum():
            raise HTTPException(400, "bad X-Demo-User")
        return uid
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "missing bearer token")
    try:
        from firebase_admin import auth as fb_auth  # type: ignore
        return fb_auth.verify_id_token(authorization.split(" ", 1)[1], app=_firebase())["uid"]
    except Exception as exc:
        raise HTTPException(401, f"invalid token: {exc}")


async def require_jobs_token(x_jobs_token: str | None = Header(default=None)) -> None:
    if x_jobs_token != get_settings().JOBS_TOKEN:
        raise HTTPException(403, "bad jobs token")
