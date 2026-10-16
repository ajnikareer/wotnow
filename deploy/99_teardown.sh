#!/usr/bin/env bash
# Remove the Cloud Run service and the scheduler job (keeps Firestore data, secrets and the service account).
source "$(dirname "$0")/_common.sh"
read -r -p "Delete service '$SERVICE' and the 'wotnow-tick' scheduler job in $PROJECT_ID? [y/N] " a; [[ "$a" == "y" ]] || exit 0
gcloud scheduler jobs delete wotnow-tick --location "$REGION" --quiet 2>/dev/null && c_ok "deleted wotnow-tick" || true
gcloud run services delete "$SERVICE" --region "$REGION" --quiet && c_ok "deleted $SERVICE"
echo "Firestore data, secrets and the service account were kept. Delete the project to remove everything."
