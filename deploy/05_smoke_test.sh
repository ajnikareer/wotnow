#!/usr/bin/env bash
# End-to-end checks on the deployed service: web, API, Firestore, Gemini, ADK agents, pipeline, admin, sign-in settings and security.
source "$(dirname "$0")/_common.sh"
set +e
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed. Run ./03_deploy.sh"; exit 1; }
TOKEN="$(jobs_token)"
# The shared demo student: with Google sign-in on, guest ids are refused, and the demo student can't be changed or deleted.
H=(-H "X-Demo-User: demo-student" -H "Content-Type: application/json")
A=(-H "X-Admin-Token: $TOKEN")
pass=0; fail=0
chk () { if [[ "$2" == *"$3"* ]]; then c_ok "$1"; ((pass++)); else c_err "$1 → ${2:0:300}"; ((fail++)); fi; }
code () { curl -s -o /dev/null -w '%{http_code}' "$@"; }
py  () { python3 -c "import sys,json
try:
  d=json.load(sys.stdin); print($1)
except Exception as e: print('?')"; }

step "$URL"
INFO="$(curl -s "$URL/api/info")"; echo "  $INFO"
chk "API health"            "$(curl -s "$URL/api/health")" '"ok":true'
chk "Gemini connected"      "$INFO" '"geminiReady":true'
chk "ADK agent runtime"     "$INFO" '"agentRuntime":"adk"'
chk "Firestore database"    "$INFO" '"db":"firestore"'
chk "Web app served at /"   "$(curl -s "$URL/")" '<div id="root">'
chk "Agent catalogue"       "$(curl -s "$URL/api/ai/agents")" '"safety_reviewer"'

step "Sign-in settings"
CFG="$(curl -s "$URL/api/auth/config")"; echo "  ℹ auth: $CFG"
chk "demo login allowed"    "$CFG" '"allowDemo":true'
chk "test sign-in is OFF on Cloud Run" "$(code -X POST -H 'Content-Type: application/json' -d '{"email":"smoke@example.com"}' "$URL/api/auth/dev-login")" "404"
if [[ "$CFG" == *'"googleEnabled":true'* ]]; then
  c_ok "Google sign-in is switched on"
  chk "invented guest profiles are refused" "$(code -H 'X-Demo-User: guest-smoke' "$URL/api/feed")" "403"
else
  c_warn "Google sign-in is not on yet (Part 6 + ./09_auth.sh)"
fi
chk "demo student can't be renamed" "$(code -X POST "${H[@]}" -d '{"nickname":"Hacker"}' "$URL/api/me")" "403"
chk "demo student can't be deleted" "$(code -X DELETE "${H[@]}" "$URL/api/me")" "403"
chk "sign-out-everywhere needs a session" "$(code -X POST -d '' "$URL/api/auth/logout-all")" "401"

step "The student feed"
FEED="$(curl -s "${H[@]}" "$URL/api/feed")"
chk "feed has today's city alert" "$FEED" '"local_alert"'
echo "  ℹ $(echo "$FEED" | py "str(len(d))+' posts · newest: '+' | '.join(p['title'] for p in d[:3])")"
LAT="$(curl -s "${H[@]}" "$URL/api/feed/latest")"
chk "feed/latest works"     "$LAT" '"newCount"'

step "Judge agent scores a student answer"
EV="$(curl -s "${H[@]}" -X POST "$URL/api/posts/oil-fire/answer" -d '{"text":"I would tell my brother not to throw water, switch off the gas and slide a metal lid over the pan. If it spreads we leave and call 101."}')"
chk "answer scored" "$EV" '"score"'
echo "  ℹ judgedBy=$(echo "$EV" | py "d.get('judgedBy')")  score=$(echo "$EV" | py "d.get('score')")   (want judgedBy=gemini)"

step "Admin console API + content pipeline"
OV="$(curl -s "${A[@]}" "$URL/api/admin/overview")"
chk "admin overview (token)" "$OV" '"pipeline"'
echo "  ℹ $(echo "$OV" | py "'posts: '+str(d['posts']['byStatus'])+' · pipeline: '+('paused' if d['pipeline']['paused'] else 'running' if d['pipeline']['enabled'] else 'disabled')+' · last tick: '+str(d['pipeline']['lastTickAt'])")"
TK="$(curl -s -X POST -H "X-Jobs-Token: $TOKEN" -d '' "$URL/jobs/tick")"
chk "scheduler tick runs" "$TK" '"id"'
PV="$(curl -s -X POST -H "X-Jobs-Token: $TOKEN" -d '' "$URL/jobs/preview?agent=ember&kind=scenario")"
chk "content studio preview" "$PV" '"ok":true'
echo "  ℹ source=$(echo "$PV" | py "d['post']['source']")  dedupe=$(echo "$PV" | py "d['post']['quality']['dedupe']")   (want gemini / embedding)"
echo "  ℹ title: $(echo "$PV" | py "d['post']['title']")"
TR="$(curl -s "${A[@]}" "$URL/api/admin/traces?limit=5")"
chk "agent traces recorded" "$TR" '"skill"'

step "Firestore feed index"
gcloud firestore indexes composite list --format="table(name.basename(),state)" 2>/dev/null | head -5

step "Security"
chk "jobs reject missing token"   "$(code -X POST -d '' "$URL/jobs/tick")" "403"
chk "admin rejects missing token" "$(code "$URL/api/admin/overview")" "403"
HDR="$(curl -sI "$URL/api/health" | tr -d '\r' | tr 'A-Z' 'a-z')"
chk "nosniff header"              "$HDR" "x-content-type-options: nosniff"
chk "HSTS over https"             "$HDR" "strict-transport-security"

echo; echo "Result: $pass passed, $fail failed"
[[ $fail -eq 0 ]] && echo "🎉 Open $URL" || echo "See CLOUD_RUN_DEPLOY.md → Troubleshooting, and ./07_logs.sh error"
