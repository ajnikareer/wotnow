"""Sessions, Google ID-token verification, rate limiting, request helpers."""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from collections import defaultdict, deque
from typing import Optional

from .settings import get_platform

DEMO_ID = "demo-student"


# ---------------- signed session tokens (no external JWT dependency) ----------------
def _b64e(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def _b64d(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def _sign(msg: str) -> str:
    return _b64e(hmac.new(get_platform().session_secret.encode(), msg.encode(), hashlib.sha256).digest())


def issue_session(account: dict, ttl_days: Optional[int] = None) -> str:
    """`ep` is the account's session epoch: "sign out of all devices" bumps it, which invalidates every token issued before."""
    now = int(time.time())
    payload = {"sub": account["id"], "email": account.get("email", ""), "ep": int(account.get("epoch", 0)), "iat": now,
               "exp": now + 86400 * (ttl_days or get_platform().session_ttl_days)}
    body = _b64e(json.dumps(payload, separators=(",", ":")).encode())
    return f"v1.{body}.{_sign('v1.' + body)}"


def verify_session(token: str) -> Optional[dict]:
    try:
        v, body, sig = token.split(".")
        if v != "v1" or not hmac.compare_digest(sig, _sign(f"v1.{body}")):
            return None
        payload = json.loads(_b64d(body))
        return payload if payload.get("exp", 0) > time.time() else None
    except Exception:
        return None


# ---------------- Google sign-in ----------------
def verify_google_credential(credential: str) -> dict:
    """Verifies a Google Identity Services ID token. Returns {sub, email, email_verified, name, picture}. Raises ValueError."""
    cid = get_platform().google_client_id
    if not cid:
        raise ValueError("Google sign-in is not configured (GOOGLE_CLIENT_ID)")
    from google.auth.transport import requests as g_requests  # type: ignore
    from google.oauth2 import id_token  # type: ignore
    info = id_token.verify_oauth2_token(credential, g_requests.Request(), cid)
    if info.get("iss") not in ("accounts.google.com", "https://accounts.google.com"):
        raise ValueError("bad issuer")
    return {"sub": info["sub"], "email": (info.get("email") or "").lower(), "email_verified": bool(info.get("email_verified")),
            "name": info.get("name") or "", "picture": info.get("picture") or ""}


def account_id_for(sub: str) -> str:
    return "a_" + hashlib.sha256(sub.encode()).hexdigest()[:20]


# ---------------- rate limiting (in-process sliding window) ----------------
class RateLimiter:
    def __init__(self) -> None:
        self.hits: dict[str, deque] = defaultdict(deque)
        self._ops = 0

    def allow(self, key: str, limit: int, window_s: float) -> tuple[bool, int]:
        now = time.time()
        q = self.hits[key]
        while q and q[0] <= now - window_s:
            q.popleft()
        if len(q) >= limit:
            return False, max(1, int(q[0] + window_s - now))
        q.append(now)
        self._ops += 1
        if self._ops % 2000 == 0:   # drop idle keys
            for k in [k for k, v in self.hits.items() if not v or v[-1] < now - 86400]:
                self.hits.pop(k, None)
        return True, 0


limiter = RateLimiter()


def client_ip(request) -> str:
    if get_platform().trust_proxy:
        xff = request.headers.get("x-forwarded-for")
        if xff:
            return xff.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def identity_key(request) -> str:
    """Who is making the request (for per-user limits). The shared demo student is limited PER VISITOR (by IP), otherwise
    one busy visitor would use up the demo's limits for everybody."""
    auth = request.headers.get("authorization")
    if auth:
        return "t:" + hashlib.sha1(auth.encode()).hexdigest()[:16]
    demo = request.headers.get("x-demo-user")
    if demo == DEMO_ID:
        return f"d:{DEMO_ID}:{client_ip(request)}"
    if demo:
        return "d:" + demo[:64]
    return "ip:" + client_ip(request)
