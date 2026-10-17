"""
Profile and parent-setting endpoints with ONE extra rule: the shared demo student can't be changed.

The demo student ('demo-student', used by "Try the student demo") is shared by every visitor. Without this rule one visitor could
rename it, move it to another class (changing everybody's feed), set a 5-minute time limit (blocking everybody's answers) or delete it.
Only `follows` (Follow / Unfollow on an expert) stays open, because the demo shows that button.

This router is included BEFORE routers/api.py in main.py, so these POST /api/me, DELETE /api/me and POST /api/parent/settings
answer instead of the older versions (which behave the same for everyone else). GET /api/me is unchanged and stays in api.py.
"""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel

from ..auth import get_uid
from ..core.security import DEMO_ID
from ..services import parent as parent_svc
from ..services import users

router = APIRouter(prefix="/api", tags=["me"])
DEMO_MSG = "The shared demo student can't be changed. Sign in to make your own profile."


class MePatch(BaseModel):
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    grade: Optional[int] = None
    city: Optional[str] = None
    school: Optional[str] = None
    className: Optional[str] = None
    follows: Optional[list[str]] = None


@router.post("/me")
async def update_me(body: MePatch, uid: str = Depends(get_uid)):
    patch = body.model_dump(exclude_none=True)
    if uid == DEMO_ID and set(patch) - {"follows"}:
        raise HTTPException(403, DEMO_MSG)
    return users.public(users.update_profile(users.get_user(uid), patch))


@router.delete("/me")
async def delete_me(uid: str = Depends(get_uid)):
    if uid == DEMO_ID:
        raise HTTPException(403, DEMO_MSG)
    users.delete_user(uid)
    return {"deleted": True}


@router.post("/parent/settings")
async def parent_settings(body: dict = Body(...), uid: str = Depends(get_uid)):
    if uid == DEMO_ID:
        raise HTTPException(403, DEMO_MSG)
    return await parent_svc.update_settings(users.get_user(uid), body)
