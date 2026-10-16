#!/usr/bin/env bash
# Re-seed the demo content and demo student (CleverFox) without redeploying.
source "$(dirname "$0")/_common.sh"
URL="$(service_url)"
curl -s -X POST -H "X-Jobs-Token: $(jobs_token)" "$URL/jobs/seed"; echo
