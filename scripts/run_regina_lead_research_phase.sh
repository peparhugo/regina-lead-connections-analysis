#!/usr/bin/env bash
# Regina research phase runner (concrete executable steps)
# Usage: ./run_regina_lead_research_phase.sh [phase]
# phases: all, setup, evidence, exposure, linkage, model, report, qa, tick, status
set -euo pipefail

PHASE=${1:-all}
ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
SCRIPT_DIR="$ROOT_DIR/scripts"
DATA_DIR="$ROOT_DIR/data"
REPORT_DIR="$ROOT_DIR/reports"

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

terminal_lock_guard(){
  local lock_file="$ROOT_DIR/memory/terminal-lock.json"
  [[ -f "$lock_file" ]] || return 0

  python3 - "$ROOT_DIR" "$lock_file" <<'PY'
import hashlib, json, os, sys
from pathlib import Path

root = Path(sys.argv[1])
lock_path = Path(sys.argv[2])
lock = json.loads(lock_path.read_text(encoding="utf-8"))
if lock.get("locked") is not True:
    raise SystemExit(0)
if os.environ.get("REGINA_TERMINAL_UNLOCK") == "I_UNDERSTAND":
    print("terminal lock bypass accepted via REGINA_TERMINAL_UNLOCK")
    raise SystemExit(0)

final_rel = lock.get("finalSynthPath", "reports/final_synthesis_2026-03-06.md")
final_path = root / final_rel
if not final_path.exists():
    print("TERMINAL_LOCK_BREACH: final synthesis missing", file=sys.stderr)
    raise SystemExit(41)

h = hashlib.sha256(final_path.read_bytes()).hexdigest()
if h != lock.get("finalSynthSha256", ""):
    print("TERMINAL_LOCK_BREACH: final synthesis hash mismatch", file=sys.stderr)
    raise SystemExit(42)

print("TERMINAL_LOCK_ACTIVE: hash verified; write/sync paths blocked (set REGINA_TERMINAL_UNLOCK=I_UNDERSTAND to bypass)")
raise SystemExit(43)
PY
  rc=$?
  if [[ $rc -eq 43 ]]; then
    return 1
  fi
  if [[ $rc -ne 0 ]]; then
    exit $rc
  fi
  return 0
}

run_setup(){
  echo "[$(ts)] setup: preparing folders"
  mkdir -p "$DATA_DIR/raw" "$DATA_DIR/derived" "$REPORT_DIR"
}

run_evidence(){
  echo "[$(ts)] evidence: running Tier A/B search seed via SearXNG"
  python3 "$SCRIPT_DIR/evidence_search_tier_ab.py"
}

run_exposure(){
  echo "[$(ts)] exposure: refreshing Regina CT/DA StatsCan variables"
  STATSCAN_MODE=ct_first python3 "$SCRIPT_DIR/fetch_statscan_equity_vars.py"
}

run_linkage(){
  echo "[$(ts)] linkage: building official CT equity panel"
  python3 "$SCRIPT_DIR/build_official_ct_equity_panel.py"

  echo "[$(ts)] linkage: building proxy CT/DA panel + robustness tests"
  python3 "$SCRIPT_DIR/build_equity_panel_and_tests.py"
}

run_model(){
  echo "[$(ts)] model: generating/refreshing summary pack"
  python3 "$SCRIPT_DIR/publish_equity_summary_pack.py"

  echo "[$(ts)] model: running endpoint-separated uncertainty scenarios"
  python3 "$SCRIPT_DIR/run_endpoint_uncertainty_scenarios.py"
}

run_report(){
  echo "[$(ts)] report: generating provenance ledger + readiness report"
  python3 "$SCRIPT_DIR/generate_data_provenance_ledger.py"

  echo "[$(ts)] report: generating first NPV policy summary (index mode)"
  python3 "$SCRIPT_DIR/generate_npv_policy_summary.py"

  echo "[$(ts)] report: generating CAD-calibrated NPV policy summary"
  python3 "$SCRIPT_DIR/generate_npv_policy_summary_cad.py"
}

run_qa(){
  echo "[$(ts)] qa: running dataset sanity checks"
  python3 "$SCRIPT_DIR/validate_regina_datasets.py"
}

if [[ "$PHASE" != "status" ]]; then
  if ! terminal_lock_guard; then
    echo "[$(ts)] blocked: terminal lock active"
    exit 1
  fi
fi

case "$PHASE" in
  all)
    run_setup
    run_evidence
    run_exposure
    run_linkage
    run_model
    run_report
    run_qa
    ;;
  setup) run_setup ;;
  evidence) run_evidence ;;
  exposure) run_exposure ;;
  linkage) run_linkage ;;
  model) run_model ;;
  report) run_report ;;
  qa) run_qa ;;
  tick)
    echo "[$(ts)] tick: legacy swarm loop archived; use mission orchestrator instead"
    python3 "$SCRIPT_DIR/regina_mission_orch_v2.py"
    ;;
  status)
    echo "[$(ts)] status: legacy swarm digest archived; read mission state"
    python3 - <<PY
import json
from pathlib import Path
p = Path("$ROOT_DIR") / "memory" / "mission-state.json"
if not p.exists():
    print("mission-state.json missing")
else:
    s = json.loads(p.read_text())
    print("REGINA_MISSION_STATUS")
    print(f"status={s.get('status')} gate={s.get('currentGate')} lastAction={s.get('lastAction')}")
PY
    ;;
  *) echo "Unknown phase: $PHASE"; exit 1 ;;
esac

echo "[$(ts)] done phase=$PHASE"
