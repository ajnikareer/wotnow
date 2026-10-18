#!/usr/bin/env bash
# Shared helpers. Sourced by every script.
set -euo pipefail
DEPLOY_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[[ -d "$DEPLOY_DIR/.bin" ]] && export PATH="$DEPLOY_DIR/.bin:$PATH"
ROOT_DIR="$(cd "$DEPLOY_DIR/.." && pwd)"
# shellcheck disable=SC1091
source "$DEPLOY_DIR/config.env"

c_ok()   { printf "  \033[32m✔\033[0m %s\n" "$*"; }
c_warn() { printf "  \033[33m⚠\033[0m %s\n" "$*"; }
c_err()  { printf "  \033[31m✘\033[0m %s\n" "$*" >&2; }
step()   { printf "\n\033[1;35m▶ %s\033[0m\n" "$*"; }

# "set" = non-empty and not a <PLACEHOLDER>
is_set() { local v="${!1:-}"; [[ -n "$v" && "$v" != "<"* ]]; }
clean()  { local v="${1:-}"; [[ "$v" == "<"* ]] && echo "" || echo "$v"; }

if ! is_set PROJECT_ID; then
  c_err "Set PROJECT_ID in deploy/config.env first."; exit 1
fi
command -v gcloud >/dev/null || { c_err "gcloud not found. Use Cloud Shell (shell.cloud.google.com)."; exit 1; }
gcloud config set project "$PROJECT_ID" >/dev/null 2>&1
RUNTIME_SA="${RUNTIME_SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)' 2>/dev/null || true)"

service_url() { gcloud run services describe "$SERVICE" --region "$REGION" --format='value(status.url)' 2>/dev/null || true; }
# Cloud Run also serves every service on a predictable address; the OAuth client can list both.
predicted_url() { echo "https://${SERVICE}-${PROJECT_NUMBER}.${REGION}.run.app"; }
jobs_token()  { gcloud secrets versions access latest --secret="$JOBS_SECRET"; }
