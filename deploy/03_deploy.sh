#!/usr/bin/env bash
# Build (Cloud Build: npm install + vite build + pip install) and deploy ONE Cloud Run service
# that serves the web app at /  and the API at /api/*.   Re-run any time to redeploy.
source "$(dirname "$0")/_common.sh"
AGENT_RUNTIME="${AGENT_RUNTIME:-adk}"

ENV="LLM_PROVIDER=gemini,GEMINI_MODEL=${GEMINI_MODEL},EMBED_MODEL=${EMBED_MODEL},AGENT_RUNTIME=${AGENT_RUNTIME}"
ENV+=",DATA_MODE=${DATA_MODE},DB_BACKEND=firestore,AUTH_MODE=${AUTH_MODE},AUTO_SEED=${AUTO_SEED}"
ENV+=",TIMEZONE=${TIMEZONE},DEMO_CROWD=${DEMO_CROWD},ENV=cloudrun"
SECRETS="JOBS_TOKEN=${JOBS_SECRET}:latest"

if [[ "$GEMINI_AUTH" == "vertex" ]]; then
  # GOOGLE_CLOUD_PROJECT set => Gemini on Agent Platform (Vertex AI) with the service account (no key).
  # GOOGLE_GENAI_USE_VERTEXAI tells ADK's model client to do the same.
  ENV+=",GOOGLE_CLOUD_PROJECT=${PROJECT_ID},GOOGLE_CLOUD_LOCATION=${VERTEX_LOCATION},GOOGLE_GENAI_USE_VERTEXAI=TRUE"
else
  # no GOOGLE_CLOUD_PROJECT => the app uses GEMINI_API_KEY (AI Studio)
  ENV+=",GOOGLE_GENAI_USE_VERTEXAI=FALSE"
  SECRETS+=",GEMINI_API_KEY=${GEMINI_KEY_SECRET}:latest"
fi
[[ -n "$MAPS_KEY_SECRET" ]] && SECRETS+=",GOOGLE_MAPS_API_KEY=${MAPS_KEY_SECRET}:latest"
[[ "$ALLOW_PUBLIC" == "true" ]] && ACCESS="--allow-unauthenticated" || ACCESS="--no-allow-unauthenticated"

step "Deploying $SERVICE to Cloud Run ($REGION, agent runtime: $AGENT_RUNTIME). The first build takes ~5–8 min"
echo "  source: $ROOT_DIR   (Dockerfile builds web + API together)"
cd "$ROOT_DIR"
gcloud run deploy "$SERVICE" \
  --source . \
  --region "$REGION" \
  --service-account "$RUNTIME_SA" \
  $ACCESS \
  --set-env-vars "$ENV" \
  --set-secrets "$SECRETS" \
  --cpu "$CPU" --memory "$MEMORY" \
  --min-instances "$MIN_INSTANCES" --max-instances "$MAX_INSTANCES" \
  --concurrency "$CONCURRENCY" --timeout 300 \
  --cpu-boost \
  --labels app=wotnow \
  --quiet

URL="$(service_url)"
echo "$URL" > "$DEPLOY_DIR/.service_url"
echo
echo "✅ Deployed: $URL"
echo "   Web app : $URL"
echo "   API docs: $URL/docs"
echo "   Status  : $URL/api/info        (want \"geminiReady\": true, \"agentRuntime\": \"adk\")"
echo "   Agents  : $URL/api/ai/agents   (ADK skills, experts and guardrails)"
echo "   Next    : ./04_scheduler.sh  then  ./05_smoke_test.sh"
