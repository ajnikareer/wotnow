#!/usr/bin/env bash
# Day-to-day controls.   Usage: ./06_demo_ready.sh [on | pause | resume | stop]
#   on      (default) make sure the service is warm and posting, and create a fresh round of posts now
#   pause   stop ALL automatic posting (students keep using the app)
#   resume  start posting again
#   stop    pause posting AND scale to zero (end of the evaluation window: stops the always-on cost)
source "$(dirname "$0")/_common.sh"
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed."; exit 1; }
TOKEN="$(jobs_token)"
A=(-H "X-Admin-Token: $TOKEN" -H "Content-Type: application/json")
post () { curl -s -o /dev/null -w "  %{http_code}  $1\n" -X POST "${A[@]}" "$URL$1" -d "${2:-{\}}"; }

case "${1:-on}" in
  on)
    if [[ "$RUN_MODE" == "always_on" ]]; then
      gcloud run services update "$SERVICE" --region "$REGION" --min-instances 1 --max-instances 1 --no-cpu-throttling --quiet >/dev/null && c_ok "1 warm instance, CPU always on"
    else
      gcloud run services update "$SERVICE" --region "$REGION" --min-instances 1 --quiet >/dev/null && c_ok "1 warm instance for the demo (run '$0 stop' afterwards)"
    fi
    post /api/admin/pipeline/pause '{"paused": false}'
    post /api/admin/pipeline/run-now '{}'
    curl -s -o /dev/null -w "  %{http_code}  warm feed\n" -H "X-Demo-User: demo-student" "$URL/api/feed"
    echo; echo "✅ Ready → $URL   (posts from every expert appear over the next few minutes; Admin → Schedule shows progress)" ;;
  pause)  post /api/admin/pipeline/pause '{"paused": true}';  c_ok "automatic posting paused" ;;
  resume) post /api/admin/pipeline/pause '{"paused": false}'; c_ok "automatic posting resumed" ;;
  stop)
    post /api/admin/pipeline/pause '{"paused": true}'
    gcloud run services update "$SERVICE" --region "$REGION" --min-instances 0 --cpu-throttling --quiet >/dev/null && c_ok "scaled to zero (no idle cost). To go live again: ./06_demo_ready.sh on, then ./03_deploy.sh if you changed RUN_MODE" ;;
  *) echo "usage: $0 [on|pause|resume|stop]"; exit 1 ;;
esac
