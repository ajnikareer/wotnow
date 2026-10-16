#!/usr/bin/env bash
# Recent app logs (newest first). Usage: ./07_logs.sh [filter] [minutes]
#   ./07_logs.sh gemini      ./07_logs.sh error 120      ./07_logs.sh "" 10
source "$(dirname "$0")/_common.sh"
F="${1:-}"; MIN="${2:-60}"
gcloud logging read "resource.type=\"cloud_run_revision\" AND resource.labels.service_name=\"$SERVICE\"" \
  --freshness="${MIN}m" --limit 300 --format='value(timestamp,severity,textPayload)' \
  | { if [[ -n "$F" ]]; then grep -i -- "$F" || echo "(no lines matching '$F')"; else cat; fi; }
