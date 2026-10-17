#!/usr/bin/env bash
# Build (Cloud Build: npm install + vite build + pip install) and deploy ONE Cloud Run service that serves the web app
# at / and the API at /api/*. Re-run any time to redeploy. First build takes ~5–8 minutes.
source "$(dirname "$0")/_common.sh"

GC="$(clean "$GOOGLE_CLIENT_ID")"; AE="$(clean "$ADMIN_EMAILS")"

# Environment variables. gcloud's "^;^" prefix switches the separator to ';' so values may contain commas (ADMIN_EMAILS).
# ALLOW_GUESTS=false: with Google sign-in nobody can invent guest profiles through the X-Demo-User header (only the shared demo student).
# DEV_LOGIN is never set here: the test sign-in must not exist on Cloud Run (the app also refuses it when K_SERVICE is set).
E=("LLM_PROVIDER=gemini" "GEMINI_MODEL=${GEMINI_MODEL}" "EMBED_MODEL=${EMBED_MODEL}" "AGENT_RUNTIME=${AGENT_RUNTIME}"
   "DATA_MODE=${DATA_MODE}" "DB_BACKEND=${DB_BACKEND}" "AUTO_SEED=${AUTO_SEED}" "TIMEZONE=${TIMEZONE}" "DEMO_CROWD=${DEMO_CROWD}"
   "AUTH_MODE=${AUTH_MODE}" "ALLOW_DEMO=${ALLOW_DEMO}" "ALLOW_GUESTS=${ALLOW_GUESTS:-false}" "ENV=cloudrun" "TRUST_PROXY=true"
   "PIPELINE_ENABLED=${PIPELINE_ENABLED}" "PIPELINE_TICK_SECONDS=${PIPELINE_TICK_SECONDS}"
   "FEED_CACHE_TTL_S=${FEED_CACHE_TTL_S}" "OVERRIDES_TTL_S=${OVERRIDES_TTL_S}" "LLM_CONCURRENCY=${LLM_CONCURRENCY}")
[[ -n "$GC" ]] && E+=("GOOGLE_CLIENT_ID=${GC}")
[[ -n "$AE" ]] && E+=("ADMIN_EMAILS=${AE}")
SECRETS="JOBS_TOKEN=${JOBS_SECRET}:latest,SESSION_SECRET=${SESSION_SECRET_NAME}:latest"

if [[ "$GEMINI_AUTH" == "vertex" ]]; then
  # GOOGLE_CLOUD_PROJECT set => Gemini on Agent Platform (Vertex AI) with the service account (no key).
  E+=("GOOGLE_CLOUD_PROJECT=${PROJECT_ID}" "GOOGLE_CLOUD_LOCATION=${VERTEX_LOCATION}" "GOOGLE_GENAI_USE_VERTEXAI=TRUE")
else
  E+=("GOOGLE_GENAI_USE_VERTEXAI=FALSE")
  SECRETS+=",GEMINI_API_KEY=${GEMINI_KEY_SECRET}:latest"
fi
is_set MAPS_KEY_SECRET && SECRETS+=",GOOGLE_MAPS_API_KEY=${MAPS_KEY_SECRET}:latest"
ENV_VARS="$(IFS=';'; echo "${E[*]}")"

[[ "$ALLOW_PUBLIC" == "true" ]] && ACCESS="--allow-unauthenticated" || ACCESS="--no-allow-unauthenticated"
if [[ "$RUN_MODE" == "always_on" ]]; then SCALE=(--min-instances 1 --max-instances 1 --no-cpu-throttling)
else SCALE=(--min-instances 0 --max-instances 1 --cpu-throttling); fi

step "Deploying $SERVICE to Cloud Run ($REGION · mode: $RUN_MODE · agents: $AGENT_RUNTIME · db: $DB_BACKEND · auth: $AUTH_MODE)"
echo "  source: $ROOT_DIR   (the Dockerfile builds the web app and the API together)"
[[ -z "$GC" ]] && c_warn "GOOGLE_CLIENT_ID is not set: only the shared demo student works until you create the OAuth client (CLOUD_RUN_DEPLOY.md Part 6) and run ./09_auth.sh"
cd "$ROOT_DIR"
gcloud run deploy "$SERVICE" \
  --source . \
  --region "$REGION" \
  --service-account "$RUNTIME_SA" \
  $ACCESS \
  --set-env-vars "^;^${ENV_VARS}" \
  --set-secrets "$SECRETS" \
  --cpu "$CPU" --memory "$MEMORY" \
  "${SCALE[@]}" \
  --concurrency "$CONCURRENCY" --timeout 600 \
  --cpu-boost \
  --labels app=wotnow \
  --quiet

URL="$(service_url)"
echo "$URL" > "$DEPLOY_DIR/.service_url"
echo
echo "✅ Deployed: $URL"
echo "   Web app   : $URL"
echo "   Admin     : $URL/#/admin     (token: gcloud secrets versions access latest --secret=$JOBS_SECRET)"
echo "   API docs  : $URL/docs"
echo "   Status    : $URL/api/info        (want \"geminiReady\": true, \"db\": \"firestore\")"
echo "   Agents    : $URL/api/ai/agents"
echo
echo "   Google sign-in origins to register (Part 6):"
echo "     $URL"
echo "     $(predicted_url)"
echo "   Next: ./04_scheduler.sh  then  ./05_smoke_test.sh"
