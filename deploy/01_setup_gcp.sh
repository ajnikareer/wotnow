#!/usr/bin/env bash
# One-time GCP setup. Safe to re-run (skips what already exists).
#  APIs · runtime service account + roles (keyless Gemini/Firestore access) · Firestore (Native) + the feed index
#  secrets (jobs token, session secret) · Artifact Registry + build permissions · optional daily Firestore backups
source "$(dirname "$0")/_common.sh"

step "1/7 Enabling APIs (1–3 min)"
APIS=(run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com firestore.googleapis.com
      secretmanager.googleapis.com cloudscheduler.googleapis.com iam.googleapis.com logging.googleapis.com
      aiplatform.googleapis.com)
[[ "$GEMINI_AUTH" == "apikey" ]] && APIS+=(generativelanguage.googleapis.com)
is_set MAPS_KEY_SECRET && APIS+=(airquality.googleapis.com)
gcloud services enable "${APIS[@]}"
c_ok "${#APIS[@]} APIs enabled"

step "2/7 Runtime service account: $RUNTIME_SA"
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

step "3/7 Firestore (Native mode) in $FIRESTORE_LOCATION"
if gcloud firestore databases describe --database="(default)" >/dev/null 2>&1; then
  TYPE="$(gcloud firestore databases describe --database='(default)' --format='value(type)')"
  [[ "$TYPE" == "FIRESTORE_NATIVE" ]] && c_ok "exists (Native)" || c_warn "exists but type=$TYPE. Needs FIRESTORE_NATIVE (use a new project)."
else
  gcloud firestore databases create --database="(default)" --location="$FIRESTORE_LOCATION" --type=firestore-native
  c_ok "created"
fi

step "4/7 Firestore index for the feed (posts: status + newest first)"
if OUT="$(gcloud firestore indexes composite create --collection-group=posts --query-scope=collection \
      --field-config=field-path=status,order=ascending --field-config=field-path=createdAt,order=descending --quiet 2>&1)"; then
  c_ok "index requested (builds in a few minutes; the app works without it, just reads a bit more)"
elif grep -qi "already exists" <<<"$OUT"; then c_ok "index already exists"
else c_warn "couldn't create the index automatically (the app falls back to a slower query). Details: $(echo "$OUT" | tail -1)"; fi

step "5/7 Secrets"
make_secret () {  # name
  if ! gcloud secrets describe "$1" >/dev/null 2>&1; then
    local value; value="$(openssl rand -hex 24)"                      # 48 random characters
    printf "%s" "$value" | gcloud secrets create "$1" --replication-policy=automatic --data-file=- >/dev/null
    c_ok "$1 created (random)"
  else c_ok "$1 exists"; fi
}
make_secret "$JOBS_SECRET"
make_secret "$SESSION_SECRET_NAME"
if [[ "$GEMINI_AUTH" == "apikey" ]]; then
  if ! gcloud secrets describe "$GEMINI_KEY_SECRET" >/dev/null 2>&1; then
    read -r -s -p "  Paste your Gemini API key (aistudio.google.com → Get API key): " KEY; echo
    printf "%s" "$KEY" | gcloud secrets create "$GEMINI_KEY_SECRET" --replication-policy=automatic --data-file=- >/dev/null
    c_ok "$GEMINI_KEY_SECRET created"
  else c_ok "$GEMINI_KEY_SECRET exists"; fi
fi
if is_set MAPS_KEY_SECRET && ! gcloud secrets describe "$MAPS_KEY_SECRET" >/dev/null 2>&1; then
  c_warn "MAPS_KEY_SECRET=$MAPS_KEY_SECRET doesn't exist. Create it or clear it in config.env (Open-Meteo works without it)."
fi

step "6/7 Artifact Registry (for source builds)"
if ! gcloud artifacts repositories describe cloud-run-source-deploy --location "$REGION" >/dev/null 2>&1; then
  gcloud artifacts repositories create cloud-run-source-deploy --repository-format=docker --location "$REGION" \
    --description="wotnow source deploys" >/dev/null
  c_ok "cloud-run-source-deploy created"
else c_ok "cloud-run-source-deploy exists"; fi
BUILD_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
for r in roles/run.builder roles/artifactregistry.writer roles/logging.logWriter roles/storage.objectViewer; do
  if gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:$BUILD_SA" --role="$r" --condition=None >/dev/null 2>&1; then
    c_ok "$r → build account"
  else c_warn "couldn't grant $r (fine if your project uses a different build account)"; fi
done

step "7/7 Daily Firestore backup (optional)"
if [[ "$ENABLE_BACKUPS" == "true" ]]; then
  if gcloud firestore backups schedules list --database='(default)' --format='value(name)' 2>/dev/null | grep -q .; then c_ok "a backup schedule already exists"
  elif gcloud firestore backups schedules create --database='(default)' --recurrence=daily --retention=7d >/dev/null 2>&1; then c_ok "daily backup, kept 7 days"
  else c_warn "couldn't create the backup schedule (older gcloud?). Skip it, or see Part 8 of CLOUD_RUN_DEPLOY.md for a manual export."; fi
else c_ok "skipped (ENABLE_BACKUPS=false)"; fi

echo
echo "✅ GCP setup done. IAM changes can take 1–2 minutes to apply."
echo "   Next: ./02_test_gemini.sh   (proves Gemini access before deploying)"
