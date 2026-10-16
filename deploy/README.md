# deploy/

Run in **Cloud Shell**, in this order. Full guide: [`../DEPLOYMENT.md`](../DEPLOYMENT.md)

| Script | What it does |
|---|---|
| `config.env` | **Edit first.** Set `PROJECT_ID` (everything else has defaults) |
| `00_check.sh` | Pre-flight: login, billing, roles, org policy, files (no changes) |
| `01_setup_gcp.sh` | APIs, service account + roles, Firestore, secrets, Artifact Registry, build permissions |
| `02_test_gemini.sh` | Calls Gemini + embeddings on Vertex AI to prove access |
| `03_deploy.sh` | Cloud Build → one Cloud Run service (web at `/`, API at `/api`) |
| `04_scheduler.sh` | Cloud Scheduler jobs for fresh AI content |
| `05_smoke_test.sh` | End-to-end checks (web, Firestore, Gemini judge, content engine, auth) |
| `06_demo_ready.sh [off]` | Warm instance + fresh content before judging / scale back to zero |
| `07_logs.sh [filter] [min]` | Recent logs, e.g. `./07_logs.sh gemini` |
| `08_reset_demo.sh` | Re-seed demo content |
| `99_teardown.sh` | Delete service + scheduler jobs |
