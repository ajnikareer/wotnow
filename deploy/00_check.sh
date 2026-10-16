#!/usr/bin/env bash
# Pre-flight checks: login, project, billing, your permissions, source files. Changes nothing.
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
  *)         c_err "Billing is NOT enabled. Link a billing account: Console → Billing → Link a billing account"; fail=1 ;;
esac

step "Your roles on the project"
ROLES="$(gcloud projects get-iam-policy "$PROJECT_ID" --flatten='bindings[].members' \
        --filter="bindings.members:user:$ACCT" --format='value(bindings.role)' 2>/dev/null | tr '\n' ' ')"
if [[ "$ROLES" == *"roles/owner"* ]]; then c_ok "Owner (all permissions)"
else
  c_warn "Not Owner. You need: run.admin, iam.serviceAccountAdmin, iam.serviceAccountUser, resourcemanager.projectIamAdmin,"
  c_warn "serviceusage.serviceUsageAdmin, cloudbuild.builds.editor, artifactregistry.admin, secretmanager.admin,"
  c_warn "datastore.owner, cloudscheduler.admin, storage.admin. You have: ${ROLES:-none visible}"
fi

step "Organisation policy (public access)"
POL="$(gcloud resource-manager org-policies describe iam.allowedPolicyMemberDomains --project "$PROJECT_ID" --effective --format='value(listPolicy.allowedValues)' 2>/dev/null || true)"
if [[ -n "$POL" ]]; then c_warn "Domain-restricted sharing is ON. 'allUsers' (public site) may be blocked. Use a personal project or set ALLOW_PUBLIC=false"
else c_ok "No domain restriction found (public Cloud Run allowed)"; fi

step "Source files"
for f in Dockerfile .gcloudignore backend/app/main.py backend/requirements.txt web/package.json web/src/main.tsx; do
  [[ -f "$ROOT_DIR/$f" ]] && c_ok "$f" || { c_err "missing $f (extract all bundles into the same wotnow/ folder)"; fail=1; }
done
[[ -d "$ROOT_DIR/web/node_modules" ]] && c_warn "web/node_modules exists locally. It's ignored by .gcloudignore, fine."

step "Config"
echo "  REGION=$REGION  FIRESTORE=$FIRESTORE_LOCATION  VERTEX=$VERTEX_LOCATION  GEMINI_AUTH=$GEMINI_AUTH  MODEL=$GEMINI_MODEL"
echo
[[ $fail -eq 0 ]] && echo "✅ Pre-flight OK. Next: ./01_setup_gcp.sh" || { echo "❌ Fix the items above first."; exit 1; }
