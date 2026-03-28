#!/usr/bin/env bash
set -euo pipefail

ROOT="/root/.openclaw/workspace"
PROJ="$ROOT/projects/regina-lead-github-pages"
INGEST="$ROOT/corpus_docs/scripts/research_ingest.sh"
CHECKPOINT_FILE="$PROJ/memory/regina_sync_checkpoint.json"
PENDING_REVIEWS_FILE="$PROJ/memory/regina_sync_pending_reviews.jsonl"

# Tunables (override via env)
REGINA_SYNC_STEP_TIMEOUT_SEC="${REGINA_SYNC_STEP_TIMEOUT_SEC:-900}"
REGINA_SYNC_AUTO_REVIEW_MAX_BYTES="${REGINA_SYNC_AUTO_REVIEW_MAX_BYTES:-350000}"
REGINA_SYNC_FORCE="${REGINA_SYNC_FORCE:-0}"

mkdir -p "$PROJ/memory"

init_checkpoint() {
  if [[ ! -f "$CHECKPOINT_FILE" ]]; then
    cat > "$CHECKPOINT_FILE" <<'JSON'
{
  "version": 1,
  "updated_at": "",
  "completed": {}
}
JSON
  fi
}

file_signature() {
  local file="$1"
  local size mtime
  size=$(stat -c %s "$file")
  mtime=$(stat -c %Y "$file")
  printf "%s:%s" "$size" "$mtime"
}

is_completed() {
  local file="$1" sig="$2"
  python3 - "$CHECKPOINT_FILE" "$file" "$sig" <<'PY'
import json,sys
cp,file,sig=sys.argv[1:4]
try:
    data=json.load(open(cp))
except Exception:
    print("0")
    raise SystemExit(0)
completed=(data.get("completed") or {}).get(file)
print("1" if completed and completed.get("signature")==sig else "0")
PY
}

mark_completed() {
  local file="$1" sig="$2" doc_id="$3" auto_review="$4"
  python3 - "$CHECKPOINT_FILE" "$file" "$sig" "$doc_id" "$auto_review" <<'PY'
import json,sys,datetime
cp,file,sig,doc_id,auto_review=sys.argv[1:6]
now = datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
try:
    data=json.load(open(cp))
except Exception:
    data={"version":1,"updated_at":"","completed":{}}
if "completed" not in data:
    data["completed"]={}
data["completed"][file]={
    "signature": sig,
    "doc_id": doc_id,
    "auto_review": auto_review,
    "completed_at": now,
}
data["updated_at"]=now
json.dump(data, open(cp,"w"), indent=2)
PY
}

queue_pending_review() {
  local file="$1" doc_id="$2" reason="$3"
  python3 - "$file" "$doc_id" "$reason" "$PENDING_REVIEWS_FILE" <<'PY'
import json,sys,datetime
path,doc_id,reason,out=sys.argv[1:5]
rec={
  "queued_at": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
  "file": path,
  "doc_id": doc_id,
  "reason": reason,
}
with open(out,"a",encoding="utf-8") as f:
    f.write(json.dumps(rec)+"\n")
PY
}

extract_doc_id() {
  local ingest_json="$1"
  printf "%s" "$ingest_json" | python3 - <<'PY'
import json,sys
raw=sys.stdin.read().strip()
if not raw:
    print("")
    raise SystemExit(0)
try:
    data=json.loads(raw)
except Exception:
    print("")
    raise SystemExit(0)
if isinstance(data, dict):
    if data.get("doc_id"):
        print(data["doc_id"])
        raise SystemExit(0)
    ing=data.get("ingested") or []
    if ing and isinstance(ing[0], dict) and ing[0].get("doc_id"):
        print(ing[0]["doc_id"])
        raise SystemExit(0)
print("")
PY
}

# Key Regina artifacts to promote into shared corpus + beliefs.
# Format: file|title|doc_type|url
entries=(
  "$PROJ/reports/final_synthesis_2026-03-06.md|Regina Lead Equity Mission Final Synthesis|report|"
  "$PROJ/reports/phd_equity_summary_2026-03-06.html|Regina Lead PhD Equity Summary 2026-03-06|report|"
  "$PROJ/reports/reproducibility_appendix_equity_2026-03-06.md|Regina Lead Reproducibility Appendix 2026-03-06|report|"
  "$PROJ/reports/statscan_census_polygon_expansion_plan_2026-03-06.md|Regina StatsCan Census Polygon Expansion Plan|plan|"
  "$PROJ/reports/evidence_tier_ab_search_2026-03-06.csv|Regina Tier A/B Evidence Search 2026-03-06|dataset|"
  "$PROJ/reports/data_provenance_ledger_2026-03-06.csv|Regina Data Provenance Ledger 2026-03-06|dataset|"
  "$PROJ/reports/qa_validation_report_2026-03-06.json|Regina QA Validation Report 2026-03-06|report|"
  "$PROJ/memory/PROJECT_MEMORY.md|Regina Project Memory|memory|"
  "$PROJ/index.html|Regina Lead Connections Public Analysis Map Page|webpage|https://peparhugo.github.io/regina-lead-connections-analysis/"
)

init_checkpoint

for entry in "${entries[@]}"; do
  IFS='|' read -r file title doc_type url <<< "$entry"
  [[ -f "$file" ]] || continue

  sig=$(file_signature "$file")
  if [[ "$REGINA_SYNC_FORCE" != "1" ]]; then
    completed=$(is_completed "$file" "$sig")
    if [[ "$completed" == "1" ]]; then
      echo "[regina-sync] skip (checkpoint): $file"
      continue
    fi
  fi

  size=$(stat -c %s "$file")
  auto_review="1"
  if [[ "$size" -gt "$REGINA_SYNC_AUTO_REVIEW_MAX_BYTES" ]]; then
    auto_review="0"
  fi

  cmd=("$INGEST" file --source regina_mission --title "$title" --file "$file" --doc-type "$doc_type" --tags "regina,opengis,lead,phd,mission")
  if [[ -n "$url" ]]; then
    cmd+=(--url "$url")
  fi
  if [[ "$auto_review" == "1" ]]; then
    cmd+=(--auto-review)
  fi

  set +e
  ingest_json=$(timeout "$REGINA_SYNC_STEP_TIMEOUT_SEC" "${cmd[@]}" 2>&1)
  rc=$?
  set -e

  if [[ "$rc" -ne 0 ]]; then
    echo "[regina-sync] failed rc=$rc file=$file"
    echo "$ingest_json" | tail -n 5
    exit "$rc"
  fi

  doc_id=$(extract_doc_id "$ingest_json" || true)
  mark_completed "$file" "$sig" "$doc_id" "$auto_review"

  if [[ "$auto_review" == "1" ]]; then
    echo "[regina-sync] ingested+jtb: $file"
  else
    [[ -n "$doc_id" ]] && queue_pending_review "$file" "$doc_id" "size_exceeds_auto_review_threshold"
    echo "[regina-sync] ingested(no-auto-review): $file"
  fi
done
