#!/usr/bin/env bash
# One Cloud Scheduler job that calls POST /jobs/tick. Always-on mode: a watchdog (the in-app loop does the work).
# Economy mode: this is what wakes the service and runs the pipeline. Re-runnable. Also removes the pre-v3 jobs.
source "$(dirname "$0")/_common.sh"
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed yet. Run ./03_deploy.sh"; exit 1; }
TOKEN="$(jobs_token)"

step "Removing old scheduler jobs (pre-v3), if any"
for j in wotnow-generate wotnow-local-alerts wotnow-quiz-1 wotnow-quiz-2; do
  gcloud scheduler jobs delete "$j" --location "$REGION" --quiet 2>/dev/null && c_ok "deleted $j" || true
done

step "Scheduler job → ${URL}/jobs/tick   [$CRON_TICK $TIMEZONE]"
ARGS=(--location "$REGION" --schedule "$CRON_TICK" --time-zone "$TIMEZONE" --uri "${URL}/jobs/tick"
      --http-method POST --attempt-deadline 300s --max-retry-attempts 1)
if gcloud scheduler jobs describe wotnow-tick --location "$REGION" >/dev/null 2>&1; then
  gcloud scheduler jobs update http wotnow-tick "${ARGS[@]}" --update-headers "X-Jobs-Token=${TOKEN}" >/dev/null
else
  gcloud scheduler jobs create http wotnow-tick "${ARGS[@]}" --headers "X-Jobs-Token=${TOKEN}" >/dev/null
fi
c_ok "wotnow-tick ready"

step "First pass now"
gcloud scheduler jobs run wotnow-tick --location "$REGION" && c_ok "triggered (new posts appear over the day, per the schedule in the admin console)"
echo
echo "✅ Next: ./05_smoke_test.sh"
