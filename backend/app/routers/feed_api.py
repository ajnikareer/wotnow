"""
Feed endpoints:  GET /api/feed (the student's feed, with neon-border states and the Today tab)
                 GET /api/feed/latest ('anything new?' poll + today's count)
                 POST /api/admin/posts/{id}/pin

GET /api/feed lives here, and this router is included BEFORE the older routers/api.py in main.py, so this version answers.
The older one only knew the tabs foryou / following / near.
"""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException

from ..auth import get_uid, require_admin
from ..core import audit
from ..engine.generator import POSTS
from ..services import feed, posts, users
from ..store.base import get_db

router = APIRouter(prefix="/api", tags=["feed"])


def _tab(tab: str) -> str:
    if tab not in feed.TABS:
        raise HTTPException(400, "tab must be today|foryou|near|following")
    return tab


@router.get("/feed")
async def feed_list(tab: str = "foryou", agent: Optional[str] = None, uid: str = Depends(get_uid)):
    """The student's feed. Each post carries `state`: done | retry | new | none (the neon border colour)."""
    return await posts.feed(users.get_user(uid), _tab(tab), agent)


@router.get("/feed/latest")
async def feed_latest(tab: str = "foryou", since: Optional[str] = None, uid: str = Depends(get_uid)):
    """{latest, newCount, todayCount}. No AI, tiny reads. `todayCount` is the number on the Today tab."""
    _tab(tab)
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
