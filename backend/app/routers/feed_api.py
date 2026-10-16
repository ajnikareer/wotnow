"""Lightweight feed endpoints: 'is there anything new?' (polled by the web app) and the admin pin switch."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException

from ..auth import get_uid, require_admin
from ..core import audit
from ..engine.generator import POSTS
from ..services import feed, users
from ..store.base import get_db

router = APIRouter(prefix="/api", tags=["feed"])


@router.get("/feed/latest")
async def feed_latest(tab: str = "foryou", since: Optional[str] = None, uid: str = Depends(get_uid)):
    """{latest: ISO time of the newest post this student can see, newCount: posts newer than `since`}. No AI, tiny reads."""
    if tab not in ("foryou", "following", "near"):
        raise HTTPException(400, "tab must be foryou|following|near")
    if since:
        since = since.replace(" ", "+")      # a raw "+00:00" in a query string arrives as " 00:00"; clients should encode it, but be forgiving
    return feed.latest(users.get_user(uid), tab, since)


@router.post("/admin/posts/{post_id}/pin")
async def pin_post(post_id: str, body: dict = Body(...), actor: str = Depends(require_admin)):
    """Keep a post in every eligible student's feed even after newer posts push it past the cut-off."""
    db = get_db()
    p = db.get(POSTS, post_id)
    if not p:
        raise HTTPException(404, "post not found")
    pinned = bool(body.get("pinned", True))
    p["pinned"] = pinned
    db.put(POSTS, post_id, p)
    feed.invalidate()
    audit.log(actor, "post.pin" if pinned else "post.unpin", post_id)
    return {"id": post_id, "pinned": pinned}
