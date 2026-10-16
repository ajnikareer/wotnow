#!/usr/bin/env bash
# End-to-end checks on the deployed service: web, API, ADK agents, Gemini judge, content engine, jobs auth.
source "$(dirname "$0")/_common.sh"
set +e
URL="$(service_url)"; [[ -n "$URL" ]] || { c_err "Service not deployed. Run ./03_deploy.sh"; exit 1; }
TOKEN="$(jobs_token)"
U="smoke-$(date +%s)"
H=(-H "X-Demo-User: $U" -H "Content-Type: application/json")
pass=0; fail=0
chk () { if [[ "$2" == *"$3"* ]]; then c_ok "$1"; ((pass++)); else c_err "$1 → ${2:0:300}"; ((fail++)); fi; }
py  () { python3 -c "import sys,json
try:
  d=json.load(sys.stdin); print($1)
except Exception as e: print('?')"; }

step "$URL"
INFO="$(curl -s "$URL/api/info")"; echo "  $INFO"
chk "API health"                "$(curl -s "$URL/api/health")" '"ok":true'
chk "Gemini connected"          "$INFO" '"geminiReady":true'
chk "ADK agent runtime"         "$INFO" '"agentRuntime":"adk"'
chk "Web app served at /"       "$(curl -s "$URL/")" '<div id="root">'
chk "Agent catalogue"           "$(curl -s "$URL/api/ai/agents")" '"safety_reviewer"'
chk "Firestore + feed"          "$(curl -s "${H[@]}" "$URL/api/feed")" '"local_alert"'

step "Judge agent scores a student answer"
EV="$(curl -s "${H[@]}" -X POST "$URL/api/posts/oil-fire/answer" -d '{"text":"I would tell my brother not to throw water, switch off the gas and slide a metal lid over the pan. If it spreads we leave and call 101."}')"
chk "answer scored" "$EV" '"score"'
echo "  ℹ judgedBy=$(echo "$EV" | py "d.get('judgedBy')")  score=$(echo "$EV" | py "d.get('score')")   (want judgedBy=gemini)"
echo "  ℹ feedback: $(echo "$EV" | py "d.get('feedback')")"

step "Content studio: expert writer → safety reviewer (preview, not published)"
PV="$(curl -s -X POST -H "X-Jobs-Token: $TOKEN" "$URL/jobs/preview?agent=ember&kind=scenario")"
chk "preview generated" "$PV" '"ok":true'
echo "  ℹ source=$(echo "$PV" | py "d['post']['source']")  dedupe=$(echo "$PV" | py "d['post']['quality']['dedupe']")   (want gemini / embedding)"
echo "  ℹ title: $(echo "$PV" | py "d['post']['title']")"

step "Agent traces (last runs)"
TR="$(curl -s -H "X-Jobs-Token: $TOKEN" "$URL/api/ai/traces?limit=6")"
chk "traces recorded" "$TR" '"skill"'
echo "$TR" | python3 -c "import sys,json
for t in json.load(sys.stdin).get('traces',[]):
  print('  ·', t.get('skill'), '|', t.get('agent'), '|', str(t.get('ms'))+' ms', '| ok' if t.get('ok') else '| BLOCKED: '+str(t.get('blocked') or t.get('error')))" 2>/dev/null

step "Security"
chk "jobs reject missing token" "$(curl -s -o /dev/null -w '%{http_code}' -X POST "$URL/jobs/generate")" "403"
chk "traces reject missing token" "$(curl -s -o /dev/null -w '%{http_code}' "$URL/api/ai/traces")" "403"
curl -s "${H[@]}" -X DELETE "$URL/api/me" >/dev/null

echo; echo "Result: $pass passed, $fail failed"
[[ $fail -eq 0 ]] && echo "🎉 Open $URL" || echo "See DEPLOYMENT.md → Troubleshooting, and ./07_logs.sh adk"
