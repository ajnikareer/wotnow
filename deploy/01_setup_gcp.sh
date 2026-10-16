#!/usr/bin/env bash
# One-time GCP setup. Safe to re-run (skips what already exists).
#  - enables APIs
#  - creates the runtime service account + roles (this is how Cloud Run talks to Gemini/Firestore, no keys)
#  - creates Firestore (Native) database
#  - creates secrets (jobs token; Gemini key only in apikey mode)
#  - creates the Artifact Registry repo + build permissions for source deploys
source "$(dirname "$0")/_common.sh"

step "1/6 Enabling APIs (1–3 min)"
APIS=(run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com firestore.googleapis.com
      secretmanager.googleapis.com cloudscheduler.googleapis.com iam.googleapis.com logging.googleapis.com
      aiplatform.googleapis.com)
[[ "$GEMINI_AUTH" == "apikey" ]] && APIS+=(generativelanguage.googleapis.com)
[[ -n "$MAPS_KEY_SECRET" ]] && APIS+=(airquality.googleapis.com)
gcloud services enable "${APIS[@]}"
c_ok "${#APIS[@]} APIs enabled"

step "2/6 Runtime service account: $RUNTIME_SA"
if ! gcloud iam service-accounts describe "$RUNTIME_SA" >/dev/null 2>&1; then
  gcloud iam service-accounts create "$RUNTIME_SA_NAME" --display-name="wotnow Cloud Run runtime"
  sleep 8
fi
ROLES=(roles/datastore.user roles/secretmanager.secretAccessor roles/logging.logWriter)
[[ "$GEMINI_AUTH" == "vertex" ]] && ROLES+=(roles/aiplatform.user)
for r in "${ROLES[@]}"; do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:$RUNTIME_SA" --role="$r" --condition=None >/dev/null
  c_ok "$r"
done

step "3/6 Firestore (Native mode) in $FIRESTORE_LOCATION"
if gcloud firestore databases describe --database="(default)" >/dev/null 2>&1; then
  TYPE="$(gcloud firestore databases describe --database='(default)' --format='value(type)')"
  [[ "$TYPE" == "FIRESTORE_NATIVE" ]] && c_ok "exists (Native)" || c_warn "exists but type=$TYPE. Needs FIRESTORE_NATIVE (use a new project)."
else
  gcloud firestore databases create --database="(default)" --location="$FIRESTORE_LOCATION" --type=firestore-native
  c_ok "created"
fi

step "4/6 Secrets"
if ! gcloud secrets describe "$JOBS_SECRET" >/dev/null 2>&1; then
  head -c 48 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c 40 | \
    gcloud secrets create "$JOBS_SECRET" --replication-policy=automatic --data-file=- >/dev/null
  c_ok "$JOBS_SECRET created (random)"
else c_ok "$JOBS_SECRET exists"; fi
if [[ "$GEMINI_AUTH" == "apikey" ]]; then
  if ! gcloud secrets describe "$GEMINI_KEY_SECRET" >/dev/null 2>&1; then
    read -r -s -p "  Paste your Gemini API key (aistudio.google.com → Get API key): " KEY; echo
    printf "%s" "$KEY" | gcloud secrets create "$GEMINI_KEY_SECRET" --replication-policy=automatic --data-file=- >/dev/null
    c_ok "$GEMINI_KEY_SECRET created"
  else c_ok "$GEMINI_KEY_SECRET exists"; fi
fi
if [[ -n "$MAPS_KEY_SECRET" ]] && ! gcloud secrets describe "$MAPS_KEY_SECRET" >/dev/null 2>&1; then
  c_warn "MAPS_KEY_SECRET=$MAPS_KEY_SECRET doesn't exist. Create it or clear it in config.env (Open-Meteo works without it)."
fi

step "5/6 Artifact Registry (for source builds)"
if ! gcloud artifacts repositories describe cloud-run-source-deploy --location "$REGION" >/dev/null 2>&1; then
  gcloud artifacts repositories create cloud-run-source-deploy --repository-format=docker --location "$REGION" \
    --description="wotnow source deploys" >/dev/null
  c_ok "cloud-run-source-deploy created"
else c_ok "cloud-run-source-deploy exists"; fi

step "6/6 Build permissions (Cloud Build runs as the default compute service account)"
BUILD_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
for r in roles/run.builder roles/artifactregistry.writer roles/logging.logWriter roles/storage.objectViewer; do
  if gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:$BUILD_SA" --role="$r" --condition=None >/dev/null 2>&1; then
    c_ok "$r → $BUILD_SA"
  else c_warn "couldn't grant $r (fine if your project uses a different build SA)"; fi
done

echo
echo "✅ GCP setup done. IAM changes can take 1–2 minutes to apply."
echo "   Next: ./02_test_gemini.sh   (proves Gemini access before deploying)"
