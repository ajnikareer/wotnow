#!/usr/bin/env bash
# Budget alerts at 50%, 90% and 100% of BUDGET_USD (emails go to the billing account's administrators). Best effort.
source "$(dirname "$0")/_common.sh"
if ! is_set BILLING_ACCOUNT_ID; then
  c_warn "Set BILLING_ACCOUNT_ID in config.env (Console → Billing → your account → Account ID), or create the budget by hand:"
  echo "  Console → Billing → Budgets & alerts → Create budget → project $PROJECT_ID → amount \$${BUDGET_USD} → alerts at 50/90/100%."
  exit 0
fi
gcloud services enable billingbudgets.googleapis.com
if gcloud billing budgets create --billing-account="$BILLING_ACCOUNT_ID" --display-name="wotnow-${PROJECT_ID}" \
     --budget-amount="${BUDGET_USD}USD" --filter-projects="projects/${PROJECT_ID}" \
     --threshold-rule=percent=0.5 --threshold-rule=percent=0.9 --threshold-rule=percent=1.0; then
  c_ok "budget created: alerts at 50%, 90% and 100% of \$${BUDGET_USD}"
else
  c_warn "couldn't create the budget (needs Billing Account Administrator). Create it in the console instead."
fi
echo "A budget only SENDS alerts. It does not stop spending."
