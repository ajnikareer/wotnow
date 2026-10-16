#!/usr/bin/env bash
# Remove the Cloud Run service and scheduler jobs (keeps Firestore data, secrets and service account).
source "$(dirname "$0")/_common.sh"
read -r -p "Delete service '$SERVICE' and its scheduler jobs in $PROJECT_ID? [y/N] " a; [[ "$a" == "y" ]] || exit 0
for j in wotnow-generate wotnow-local-alerts wotnow-quiz-1 wotnow-quiz-2; do
  gcloud scheduler jobs delete "$j" --location "$REGION" --quiet 2>/dev/null && c_ok "deleted $j" || true
done
gcloud run services delete "$SERVICE" --region "$REGION" --quiet && c_ok "deleted $SERVICE"
echo "Firestore data, secrets and the service account were kept. Delete the project to remove everything."
