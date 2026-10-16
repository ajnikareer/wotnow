#!/usr/bin/env bash
# Apply sign-in settings (GOOGLE_CLIENT_ID, ADMIN_EMAILS, AUTH_MODE, ALLOW_DEMO) from config.env to the RUNNING service.
# No rebuild: it only creates a new revision with different environment variables (~30 s).
source "$(dirname "$0")/_common.sh"
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed yet. Run ./03_deploy.sh"; exit 1; }
GC="$(clean "$GOOGLE_CLIENT_ID")"; AE="$(clean "$ADMIN_EMAILS")"

if [[ -z "$GC" ]]; then
  c_err "GOOGLE_CLIENT_ID is not set in config.env."
  echo "  1. Create the OAuth client (CLOUD_RUN_DEPLOY.md, Part 6). Register these two origins:"
  echo "       $URL"
  echo "       $(predicted_url)"
  echo "  2. Put the client ID in config.env, then run this script again."
  exit 1
fi
[[ "$GC" == *.apps.googleusercontent.com ]] || c_warn "That doesn't look like a client ID (it should end in .apps.googleusercontent.com)"

E=("AUTH_MODE=${AUTH_MODE}" "ALLOW_DEMO=${ALLOW_DEMO}" "GOOGLE_CLIENT_ID=${GC}")
[[ -n "$AE" ]] && E+=("ADMIN_EMAILS=${AE}")
step "Updating $SERVICE: AUTH_MODE=$AUTH_MODE  ALLOW_DEMO=$ALLOW_DEMO  admin=${AE:-(token only)}"
gcloud run services update "$SERVICE" --region "$REGION" --update-env-vars "^;^$(IFS=';'; echo "${E[*]}")" --quiet >/dev/null
c_ok "new revision serving"

sleep 3
CFG="$(curl -s "$URL/api/auth/config")"; echo "  $CFG"
[[ "$CFG" == *'"googleEnabled":true'* ]] && c_ok "Google sign-in is ON" || c_err "still off: check AUTH_MODE=google and the client ID"
echo
echo "Test it: open $URL in a private window → 'Sign in' → your Google account → add a child profile."
echo "If Google says 'origin_mismatch', the URL in the address bar isn't registered as an Authorised JavaScript origin (changes can take a few minutes)."
