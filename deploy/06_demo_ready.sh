#!/usr/bin/env bash
# Before judging: 1 warm instance + fresh alert, quiz and posts.   After judging: ./06_demo_ready.sh off
source "$(dirname "$0")/_common.sh"
if [[ "${1:-on}" == "off" ]]; then
  gcloud run services update "$SERVICE" --region "$REGION" --min-instances 0 --quiet >/dev/null && c_ok "min-instances=0 (scale to zero, no idle cost)"
  exit 0
fi
gcloud run services update "$SERVICE" --region "$REGION" --min-instances 1 --quiet >/dev/null && c_ok "min-instances=1 (no cold starts)"
URL="$(service_url)"; TOKEN="$(jobs_token)"
for p in "/jobs/local-alerts" "/jobs/live-quiz?agent=signal" "/jobs/generate"; do
  curl -s -o /dev/null -w "  %{http_code}  ${p}  (%{time_total}s)\n" -X POST -H "X-Jobs-Token: $TOKEN" "$URL$p"
done
curl -s -o /dev/null -w "  %{http_code}  warm feed\n" -H "X-Demo-User: demo-student" "$URL/api/feed"
echo; echo "✅ Demo ready → $URL    (remember: ./06_demo_ready.sh off afterwards)"
