#!/usr/bin/env bash
# Cloud Scheduler jobs → /jobs/* (authenticated with the X-Jobs-Token secret). Re-runnable (create or update).
source "$(dirname "$0")/_common.sh"
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed yet. Run ./03_deploy.sh"; exit 1; }
TOKEN="$(jobs_token)"

upsert () {  # name cron path
  local name=$1 cron=$2 path=$3
  local args=(--location "$REGION" --schedule "$cron" --time-zone "$TIMEZONE" --uri "${URL}${path}"
              --http-method POST --attempt-deadline 600s --max-retry-attempts 1)
  if gcloud scheduler jobs describe "$name" --location "$REGION" >/dev/null 2>&1; then
    gcloud scheduler jobs update http "$name" "${args[@]}" --update-headers "X-Jobs-Token=${TOKEN}" >/dev/null
  else
    gcloud scheduler jobs create http "$name" "${args[@]}" --headers "X-Jobs-Token=${TOKEN}" >/dev/null
  fi
  c_ok "$name  [$cron $TIMEZONE] → $path"
}

step "Scheduler jobs for $URL"
upsert wotnow-generate     "$CRON_GENERATE" "/jobs/generate"
upsert wotnow-local-alerts "$CRON_ALERTS"   "/jobs/local-alerts"
upsert wotnow-quiz-1       "$CRON_QUIZ_1"   "/jobs/live-quiz"
upsert wotnow-quiz-2       "$CRON_QUIZ_2"   "/jobs/live-quiz"

step "Kick off the first Gemini posts now"
gcloud scheduler jobs run wotnow-generate --location "$REGION" && c_ok "wotnow-generate triggered (takes ~1–2 min)"
echo
echo "✅ Scheduler ready. Next: ./05_smoke_test.sh"
