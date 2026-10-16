from __future__ import annotations

from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

from ..config import get_settings


def tz() -> ZoneInfo:
    return ZoneInfo(get_settings().TIMEZONE)


def now_local() -> datetime:
    return datetime.now(tz())


def today() -> date:
    return now_local().date()


def week_id(d: date | None = None) -> str:
    y, w, _ = (d or today()).isocalendar()
    return f"{y}-W{w:02d}"


def utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def local_date_of(iso: str) -> date:
    return datetime.fromisoformat(iso).astimezone(tz()).date()
