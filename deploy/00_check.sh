#!/usr/bin/env bash
# Pre-flight checks: login, project, billing, your permissions, source files, config. Changes nothing.
source "$(dirname "$0")/_common.sh"
fail=0

step "Account & project"
ACCT="$(gcloud config get-value account 2>/dev/null)"
[[ -n "$ACCT" ]] && c_ok "Logged in as $ACCT" || { c_err "Not logged in: gcloud auth login"; fail=1; }
[[ -n "$PROJECT_NUMBER" ]] && c_ok "Project $PROJECT_ID (#$PROJECT_NUMBER)" || { c_err "Project $PROJECT_ID not found or no access"; fail=1; }

step "Billing"
BILL="$(gcloud billing projects describe "$PROJECT_ID" --format='value(billingEnabled)' 2>/dev/null || echo unknown)"
case "$BILL" in
  True|true) c_ok "Billing enabled" ;;
  unknown)   c_warn "Couldn't read billing (needs billing viewer). Make sure billing is linked: Console → Billing" ;;
  *)         c_err "Billing is NOT enabled. Console → Billing → Link a billing account"; fail=1 ;;
esac

step "Your roles on the project"
ROLES="$(gcloud projects get-iam-policy "$PROJECT_ID" --flatten='bindings[].members' \
        --filter="bindings.members:user:$ACCT" --format='value(bindings.role)' 2>/dev/null | tr '\n' ' ')"
if [[ "$ROLES" == *"roles/owner"* ]]; then c_ok "Owner (all permissions)"
else c_warn "Not Owner. You have: ${ROLES:-none visible}. The scripts need Owner (or Editor + IAM admin + Cloud Run admin) on this project."; fi

step "Organisation policy (public access)"
POL="$(gcloud resource-manager org-policies describe iam.allowedPolicyMemberDomains --project "$PROJECT_ID" --effective --format='value(listPolicy.allowedValues)' 2>/dev/null || true)"
if [[ -n "$POL" ]]; then c_warn "Domain-restricted sharing is ON: a public site may be blocked. Use a personal project (no organisation)."
else c_ok "No domain restriction found (public Cloud Run allowed)"; fi

step "Source files"
for f in Dockerfile .gcloudignore backend/app/main.py backend/app/services/feed.py backend/app/pipeline/scheduler.py \
         backend/app/agents/registry.json backend/requirements.txt web/package.json web/src/main.tsx web/src/pages/admin/AdminPage.tsx; do
  [[ -f "$ROOT_DIR/$f" ]] && c_ok "$f" || { c_err "missing $f (apply every bundle in order: backend, web, deploy, ADK, v3, this one)"; fail=1; }
done
grep -q "google-adk" "$ROOT_DIR/backend/requirements.txt" 2>/dev/null && c_ok "ADK in requirements" || { c_err "google-adk missing from requirements.txt"; fail=1; }

step "Config"
echo "  REGION=$REGION  FIRESTORE=$FIRESTORE_LOCATION  VERTEX=$VERTEX_LOCATION  GEMINI_AUTH=$GEMINI_AUTH  MODEL=$GEMINI_MODEL  RUN_MODE=$RUN_MODE"
is_set GOOGLE_CLIENT_ID && c_ok "GOOGLE_CLIENT_ID set" || c_warn "GOOGLE_CLIENT_ID not set yet. Fine for now: deploy first, then Part 6 + ./09_auth.sh"
is_set ADMIN_EMAILS && c_ok "ADMIN_EMAILS = $ADMIN_EMAILS" || c_warn "ADMIN_EMAILS not set: you can still open the admin console with the admin token"
[[ "$RUN_MODE" == "always_on" || "$RUN_MODE" == "economy" ]] && c_ok "RUN_MODE=$RUN_MODE" || { c_err "RUN_MODE must be always_on or economy"; fail=1; }
[[ "$DB_BACKEND" == "firestore" ]] || c_warn "DB_BACKEND=$DB_BACKEND: Cloud Run's disk is wiped on every restart; only firestore keeps data"
echo
[[ $fail -eq 0 ]] && echo "✅ Pre-flight OK. Next: ./01_setup_gcp.sh" || { echo "❌ Fix the items above first."; exit 1; }
