"""
Current local conditions for Terra's alerts.
DATA_MODE=mock -> city presets (content/cities.json).  DATA_MODE=live -> Open-Meteo forecast + air quality
(free, no key) with Google Air Quality API when GOOGLE_MAPS_API_KEY is set. Any failure falls back to the preset.
"""
from __future__ import annotations

import json
import logging
import re
from functools import lru_cache

import httpx

from ..config import get_settings

log = logging.getLogger("wotnow.conditions")

PM25 = [(0.0, 9.0, 0, 50), (9.1, 35.4, 51, 100), (35.5, 55.4, 101, 150), (55.5, 125.4, 151, 200), (125.5, 225.4, 201, 300), (225.5, 500.4, 301, 500)]


def us_aqi_pm25(c: float | None) -> int | None:
    if c is None:
        return None
    for lo, hi, alo, ahi in PM25:
        if c <= hi:
            return round((ahi - alo) / (hi - lo) * (max(c, lo) - lo) + alo)
    return 500


def aqi_band(aqi: int | None) -> str:
    if aqi is None:
        return "Unknown"
    for lim, name in ((50, "Good"), (100, "Moderate"), (150, "Unhealthy for sensitive groups"), (200, "Unhealthy"), (300, "Very unhealthy")):
        if aqi <= lim:
            return name
    return "Hazardous"


@lru_cache
def presets() -> dict:
    d = json.loads((get_settings().CONTENT_DIR / "cities.json").read_text(encoding="utf-8"))
    d.pop("_note", None)
    return d


def slug(city: str) -> str:
    s = re.sub(r"[^a-z]", "", (city or "").lower())
    return {"newdelhi": "delhi", "bangalore": "bengaluru", "bombay": "mumbai", "calcutta": "kolkata", "madras": "chennai"}.get(s, s)


async def _get(url: str, params: dict) -> dict:
    async with httpx.AsyncClient(timeout=get_settings().HTTP_TIMEOUT) as c:
        r = await c.get(url, params=params)
        r.raise_for_status()
        return r.json()


async def locate(city: str) -> dict:
    p = presets().get(slug(city))
    if p:
        return {"name": p["name"], "lat": p["lat"], "lon": p["lon"], "slug": slug(city)}
    if get_settings().DATA_MODE == "live":
        try:
            d = await _get("https://geocoding-api.open-meteo.com/v1/search", {"name": city, "count": 1, "country": "IN"})
            r = (d.get("results") or [None])[0]
            if r:
                return {"name": r["name"], "lat": r["latitude"], "lon": r["longitude"], "slug": slug(r["name"])}
        except Exception as exc:
            log.warning("geocode failed for %s: %s", city, exc)
    p = presets()["pune"]
    return {"name": city or p["name"], "lat": p["lat"], "lon": p["lon"], "slug": slug(city) or "pune", "approx": True}


_GEO: dict[str, dict] = {}


async def locate_cached(city: str) -> dict:
    k = slug(city)
    if k not in _GEO:
        _GEO[k] = await locate(city)
    return _GEO[k]


async def conditions(city: str, loc: dict | None = None) -> dict:
    loc = loc or await locate_cached(city)
    preset = presets().get(loc["slug"], presets()["pune"])["demo"]
    out = {"city": loc["name"], "slug": loc["slug"], **preset, "source": "demo-preset"}
    if get_settings().DATA_MODE != "live":
        out["aqi_band"] = aqi_band(out["aqi"])
        return out
    try:
        w = await _get("https://api.open-meteo.com/v1/forecast", {
            "latitude": loc["lat"], "longitude": loc["lon"], "timezone": "auto", "forecast_days": 1, "past_days": 7,
            "current": "temperature_2m,apparent_temperature,relative_humidity_2m",
            "daily": "temperature_2m_max,precipitation_sum"})
        cur, dl = w["current"], w["daily"]
        out.update(temp_c=round(cur["temperature_2m"]), feels_like_c=round(cur["apparent_temperature"]),
                   humidity=round(cur["relative_humidity_2m"]), max_c=round(dl["temperature_2m_max"][-1]),
                   rain_7d_mm=round(sum(x or 0 for x in dl["precipitation_sum"][:-1])), source="open-meteo")
    except Exception as exc:
        log.warning("weather failed (%s): %s", city, exc)
    try:
        aqi = None
        key = get_settings().GOOGLE_MAPS_API_KEY
        if key:
            async with httpx.AsyncClient(timeout=get_settings().HTTP_TIMEOUT) as c:
                r = await c.post("https://airquality.googleapis.com/v1/currentConditions:lookup", params={"key": key},
                                 json={"location": {"latitude": loc["lat"], "longitude": loc["lon"]}, "extraComputations": ["POLLUTANT_CONCENTRATION"]})
                r.raise_for_status()
                pm = {p["code"]: p.get("concentration", {}).get("value") for p in r.json().get("pollutants", [])}
                aqi = us_aqi_pm25(pm.get("pm25"))
        if aqi is None:
            a = await _get("https://air-quality-api.open-meteo.com/v1/air-quality", {"latitude": loc["lat"], "longitude": loc["lon"], "current": "us_aqi,pm2_5"})
            aqi = a["current"].get("us_aqi") or us_aqi_pm25(a["current"].get("pm2_5"))
        if aqi is not None:
            out["aqi"] = round(aqi)
    except Exception as exc:
        log.warning("air quality failed (%s): %s", city, exc)
    out["aqi_band"] = aqi_band(out["aqi"])
    return out
