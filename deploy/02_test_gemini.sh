#!/usr/bin/env bash
# Proves the project can call Gemini + embeddings BEFORE deploying (uses your Cloud Shell login).
# Cloud Run will use the runtime service account instead, with the same APIs and model names.
source "$(dirname "$0")/_common.sh"
BODY='{"contents":[{"role":"user","parts":[{"text":"Reply with exactly: wotnow ready"}]}]}'

if [[ "$GEMINI_AUTH" == "vertex" ]]; then
  TOKEN="$(gcloud auth print-access-token)"
  BASE="https://${VERTEX_LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${VERTEX_LOCATION}/publishers/google/models"

  step "Gemini on Vertex AI: $GEMINI_MODEL @ $VERTEX_LOCATION"
  R="$(curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" "$BASE/${GEMINI_MODEL}:generateContent" -d "$BODY")"
  if echo "$R" | grep -q '"text"'; then c_ok "Gemini replied: $(echo "$R" | python3 -c 'import sys,json;print(json.load(sys.stdin)["candidates"][0]["content"]["parts"][0]["text"].strip())')"
  else c_err "Gemini call failed:"; echo "$R" | head -c 800; echo; GEM_FAIL=1; fi

  step "Embeddings on Vertex AI: $EMBED_MODEL"
  E="$(curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" "$BASE/${EMBED_MODEL}:predict" -d '{"instances":[{"content":"oil fire in a pan"}]}')"
  if echo "$E" | grep -q '"values"'; then c_ok "Embeddings OK ($(echo "$E" | python3 -c 'import sys,json;print(len(json.load(sys.stdin)["predictions"][0]["embeddings"]["values"]))') dims)"
  else c_warn "Embeddings failed. The app falls back to text similarity automatically:"; echo "$E" | head -c 400; echo; fi

  step "Runtime service account has Vertex AI access?"
  if gcloud projects get-iam-policy "$PROJECT_ID" --flatten='bindings[].members' --filter="bindings.members:serviceAccount:$RUNTIME_SA AND bindings.role:roles/aiplatform.user" --format='value(bindings.role)' | grep -q aiplatform; then
    c_ok "$RUNTIME_SA has roles/aiplatform.user"
  else c_err "Missing roles/aiplatform.user on $RUNTIME_SA. Re-run ./01_setup_gcp.sh"; GEM_FAIL=1; fi
else
  KEY="$(gcloud secrets versions access latest --secret="$GEMINI_KEY_SECRET")"
  step "Gemini via API key: $GEMINI_MODEL"
  R="$(curl -s -X POST -H "Content-Type: application/json" "https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${KEY}" -d "$BODY")"
  echo "$R" | grep -q '"text"' && c_ok "Gemini replied" || { c_err "Gemini call failed:"; echo "$R" | head -c 800; echo; GEM_FAIL=1; }
fi

echo
if [[ "${GEM_FAIL:-0}" == 1 ]]; then
  echo "❌ Fix Gemini access first (see DEPLOYMENT.md → Troubleshooting). Common causes:"
  echo "   - API just enabled: wait 2 minutes and retry"
  echo "   - model not available in $VERTEX_LOCATION: keep VERTEX_LOCATION=us-central1, or try GEMINI_MODEL=gemini-2.0-flash"
  exit 1
fi
echo "✅ Gemini access works. Next: ./03_deploy.sh"
