# ---------------------------------------------------------------------------
# wotnow: ONE container = web app (React, built here) + API (FastAPI).
# Cloud Build runs `npm install` + `vite build` in the cloud, so no local npm is needed.
# ---------------------------------------------------------------------------

# ---------- 1) build the web app ----------
FROM node:20-slim AS web
WORKDIR /web
COPY web/package*.json ./
RUN npm install --no-audit --no-fund --loglevel=error
COPY web/ ./
# The browser calls the API on the same domain (/api/*)
ENV VITE_API_MODE=live
RUN npm run build

# ---------- 2) API + static site ----------
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PORT=8080 STATIC_DIR=/srv/static
WORKDIR /srv
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/app ./app
COPY --from=web /web/dist ./static
EXPOSE 8080
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips='*'"]
