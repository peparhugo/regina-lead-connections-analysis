#!/usr/bin/env python3
from __future__ import annotations
import csv
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "memory" / "mission-state.json"
PROG = ROOT / "memory" / "mission-progress.json"
LOG = ROOT / "reports" / "mission-log.md"
KG = ROOT / "reports" / "knowledge-gaps.md"

DA_OUT = ROOT / "data" / "derived" / "statscan_da_equity_vars_2016_regina.csv"
CT_OUT = ROOT / "data" / "derived" / "statscan_ct_equity_vars_2016_regina.csv"
SUMMARY = ROOT / "reports" / "phd_equity_summary_2026-03-06.html"
APPENDIX = ROOT / "reports" / "reproducibility_appendix_equity_2026-03-06.md"
FINAL_SYNTH = ROOT / "reports" / "final_synthesis_2026-03-06.md"
SIG_RESULTS = ROOT / "data" / "derived" / "equity_significance_results_official_ct_2026-03-06_regina.csv"
CT_PANEL = ROOT / "data" / "derived" / "ct_equity_panel_official_2026-03-06_regina.csv"
TERMINAL_LOCK = ROOT / "memory" / "terminal-lock.json"
TERMINAL_UNLOCK_ENV = "REGINA_TERMINAL_UNLOCK"
TERMINAL_UNLOCK_VALUE = "I_UNDERSTAND"

STEP_TIMEOUT_SEC = int(os.environ.get("REGINA_STEP_TIMEOUT_SEC", "1200"))


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_terminal_lock() -> dict | None:
    if not TERMINAL_LOCK.exists():
        return None
    try:
        data = json.loads(TERMINAL_LOCK.read_text(encoding="utf-8"))
    except Exception:
        return None
    if data.get("locked") is not True:
        return None
    return data


def write_terminal_lock(locked_by: str = "regina_mission_orch_v2.py"):
    TERMINAL_LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock = {
        "locked": True,
        "finalSynthPath": str(FINAL_SYNTH.relative_to(ROOT)),
        "finalSynthSha256": sha256_file(FINAL_SYNTH),
        "lockedAt": now(),
        "lockedBy": locked_by,
    }
    write_json(TERMINAL_LOCK, lock)


def log(msg: str):
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"\n- {now()} | {msg}")


def append_gap(gate: str, gap: str, action: str):
    with KG.open("a", encoding="utf-8") as f:
        f.write(f"\n| {now()} | {gate} | {gap} | {action} |")


def run(cmd: str):
    try:
        p = subprocess.run(
            cmd,
            shell=True,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=STEP_TIMEOUT_SEC,
        )
        return p.returncode, p.stdout[-1200:], p.stderr[-1200:], False
    except subprocess.TimeoutExpired as e:
        return 124, (e.stdout or "")[-1200:], (e.stderr or "")[-1200:], True


def count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", newline="") as f:
        return max(0, sum(1 for _ in f) - 1)


def g1_pass(progress: dict) -> bool:
    # file-based deterministic rule
    ct_ok = CT_OUT.exists() and count_rows(CT_OUT) >= 50
    da_ok = DA_OUT.exists() and count_rows(DA_OUT) >= progress["da"]["targetRows"]
    return ct_ok and da_ok


def g2_pass() -> bool:
    return (ROOT / "data" / "derived" / "equity_significance_results_2026-03-06.csv").exists() or \
           (ROOT / "data" / "derived" / "equity_significance_results_official_ct_2026-03-06.csv").exists()


def g3_pass() -> bool:
    return SUMMARY.exists() and APPENDIX.exists()


def next_data_cmd(progress: dict) -> str:
    da = progress["da"]
    rows_now = count_rows(DA_OUT)
    offset = int(da.get("offset", 0))
    # auto-heal cursor from on-disk progress
    if offset == 0 and rows_now > 0:
        offset = rows_now
        da["offset"] = rows_now
    batch = int(da.get("batchSize", 10))
    append = 1 if rows_now > 0 else 0
    return (
        f"STATSCAN_MODE=da_only STATSCAN_DA_START={offset} "
        f"STATSCAN_DA_LIMIT={batch} STATSCAN_DA_APPEND={append} "
        f"python3 scripts/fetch_statscan_equity_vars.py"
    )


def write_final_synthesis(state: dict, progress: dict):
    lines = [
        "# Regina Lead Equity Mission — Final Synthesis",
        "",
        f"Generated: {now()}",
        "",
        "## Mission status",
        "- Status: COMPLETE",
        "- Current gate: G4_MISSION_CLOSEOUT",
        "- Regina scope enforced (CT DGUID prefix 2016S0507705; DA GEO_ID prefix 4706)",
        "",
        "## Completed artifacts",
        f"- CT vars: `{CT_OUT.relative_to(ROOT)}` (rows: {count_rows(CT_OUT)})",
        f"- DA vars: `{DA_OUT.relative_to(ROOT)}` (rows: {count_rows(DA_OUT)})",
        f"- Official CT panel: `{CT_PANEL.relative_to(ROOT)}` (rows: {count_rows(CT_PANEL)})",
        f"- Significance output: `{SIG_RESULTS.relative_to(ROOT)}`",
        f"- Public summary: `{SUMMARY.relative_to(ROOT)}`",
        f"- Repro appendix: `{APPENDIX.relative_to(ROOT)}`",
        "",
        "## Interpretation guardrails",
        "- Association-level findings only (non-causal).",
        "- Replacement fields in CT panel are inferred proxies and explicitly labeled.",
        "- Use this output for decision support and prioritization, not causal attribution.",
        "",
        "## Remaining gaps / next work",
        "- Add household-level or address-linked validation when accessible.",
        "- Add temporal robustness checks across additional windows.",
        "- Keep official vs inferred metrics visually separated in public outputs.",
        "",
        "## Automation note",
        "- Mission orchestrator now closes out automatically when G1-G3 pass and writes this synthesis artifact.",
    ]
    FINAL_SYNTH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"G4 -> PASS | wrote {FINAL_SYNTH.relative_to(ROOT)}")


def sync_regina_knowledge_to_corpus():
    sync_timeout_sec = int(os.environ.get("REGINA_SYNC_TIMEOUT_SEC", "3600"))
    env = os.environ.copy()
    env.setdefault("REGINA_SYNC_STEP_TIMEOUT_SEC", "900")
    env.setdefault("REGINA_SYNC_AUTO_REVIEW_MAX_BYTES", "350000")

    try:
        p = subprocess.run(
            "bash scripts/regina_sync_to_corpus_jtb.sh",
            shell=True,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=sync_timeout_sec,
            env=env,
        )
        rc, timed_out = p.returncode, False
    except subprocess.TimeoutExpired as e:
        rc, timed_out = 124, True

    if rc == 0:
        log("G4 -> corpus/JTB sync complete")
    else:
        log(f"G4 -> corpus/JTB sync failed rc={rc} timeout={timed_out}")


def enforce_terminal_lock_or_exit(state: dict | None = None):
    lock = read_terminal_lock()
    if not lock:
        return

    unlock = os.environ.get(TERMINAL_UNLOCK_ENV, "")
    if unlock == TERMINAL_UNLOCK_VALUE:
        log(f"G4 -> UNLOCK_BYPASS | {TERMINAL_UNLOCK_ENV} accepted; terminal lock bypassed")
        return

    final_path = ROOT / lock.get("finalSynthPath", str(FINAL_SYNTH.relative_to(ROOT)))
    expected = lock.get("finalSynthSha256", "")

    if not final_path.exists():
        log("G4 -> BLOCKED | terminal lock enforced; final synthesis missing")
        if state is not None:
            state["currentGate"] = "G4_MISSION_CLOSEOUT"
            state["lastAction"] = "TERMINAL_LOCK_BLOCKED_MISSING_FINAL_SYNTH"
            state["lastUpdated"] = now()
            write_json(STATE, state)
        print("TERMINAL_LOCK_BREACH: final synthesis missing", file=sys.stderr)
        raise SystemExit(41)

    current = sha256_file(final_path)
    if current != expected:
        log("G4 -> BLOCKED | terminal lock enforced; integrity breach (final synthesis hash mismatch)")
        if state is not None:
            state["currentGate"] = "G4_MISSION_CLOSEOUT"
            state["lastAction"] = "TERMINAL_LOCK_INTEGRITY_BREACH"
            state["lastUpdated"] = now()
            write_json(STATE, state)
        print("TERMINAL_LOCK_BREACH: final synthesis hash mismatch", file=sys.stderr)
        raise SystemExit(42)

    log("G4 -> NOOP | terminal lock enforced; hash verified; skipping all gate logic")
    if state is not None:
        state["currentGate"] = "G4_MISSION_CLOSEOUT"
        state["lastAction"] = "TERMINAL_LOCK_NOOP"
        state["lastUpdated"] = now()
        write_json(STATE, state)
    print({"terminalLock": True, "action": "NOOP", "gate": "G4_MISSION_CLOSEOUT", "status": "COMPLETE"})
    raise SystemExit(0)


def main():
    s = read_json(STATE)
    p = read_json(PROG)

    enforce_terminal_lock_or_exit(state=s)

    # refresh gate status by file checks
    s["gates"]["G1_DATA_COMPLETENESS"]["passed"] = g1_pass(p)
    s["gates"]["G2_STATISTICAL_VALIDITY"]["passed"] = g2_pass()
    s["gates"]["G3_PUBLICATION_QUALITY"]["passed"] = g3_pass()
    s["gates"]["G4_MISSION_CLOSEOUT"]["passed"] = all(
        s["gates"][g]["passed"] for g in ["G1_DATA_COMPLETENESS", "G2_STATISTICAL_VALIDITY", "G3_PUBLICATION_QUALITY"]
    )

    # Backfill lock for already-closed missions.
    if (
        s.get("status") == "COMPLETE"
        and s["gates"]["G4_MISSION_CLOSEOUT"]["passed"]
        and FINAL_SYNTH.exists()
        and not read_terminal_lock()
    ):
        write_terminal_lock(locked_by="regina_mission_orch_v2.py(backfill)")
        log(f"G4 -> LOCKED | backfilled {TERMINAL_LOCK.relative_to(ROOT)}")
        enforce_terminal_lock_or_exit(state=s)

    # G1
    if not s["gates"]["G1_DATA_COMPLETENESS"]["passed"]:
        s["currentGate"] = "G1_DATA_COMPLETENESS"
        cmd = next_data_cmd(p)
        rc, out, err, timed_out = run(cmd)
        s["lastAction"] = "WORKER_DATA"

        rows_now = count_rows(DA_OUT)
        p["da"]["rowsWritten"] = rows_now
        p["da"]["offset"] = int(p["da"]["offset"]) + int(p["da"]["batchSize"])
        p["da"]["lastCheckpointAt"] = now()

        if rows_now - int(p.get("lastHeartbeatRows", 0)) >= 50:
            p["lastHeartbeatRows"] = rows_now
            log(f"heartbeat: DA rows={rows_now}")

        if rc != 0:
            p["retries"]["G1_DATA_COMPLETENESS"] += 1
            log(f"G1 WORKER_DATA rc={rc} timeout={timed_out}")
            if p["retries"]["G1_DATA_COMPLETENESS"] >= 2:
                s["knowledgeGap"]["active"] = True
                s["knowledgeGap"]["topic"] = "Repeated G1 extraction failures; trigger JTB pinning"
                append_gap("G1_DATA_COMPLETENESS", "repeated extraction failure", "run WORKER_RESEARCH_JTB")
                run("python3 scripts/pin_statscan_variable_ids.py")
        else:
            p["retries"]["G1_DATA_COMPLETENESS"] = 0
            log(f"G1 WORKER_DATA rc=0 rows={rows_now} next_offset={p['da']['offset']}")

    # G2
    elif not s["gates"]["G2_STATISTICAL_VALIDITY"]["passed"]:
        s["currentGate"] = "G2_STATISTICAL_VALIDITY"
        rc, out, err, timed_out = run("python3 scripts/build_equity_panel_and_tests.py")
        s["lastAction"] = "WORKER_STATS"
        if rc != 0:
            p["retries"]["G2_STATISTICAL_VALIDITY"] += 1
            log(f"G2 WORKER_STATS rc={rc} timeout={timed_out}")
        else:
            p["retries"]["G2_STATISTICAL_VALIDITY"] = 0
            log("G2 WORKER_STATS rc=0")

    # G3
    elif not s["gates"]["G3_PUBLICATION_QUALITY"]["passed"]:
        s["currentGate"] = "G3_PUBLICATION_QUALITY"
        rc, out, err, timed_out = run("python3 scripts/publish_equity_summary_pack.py")
        s["lastAction"] = "WORKER_PUBLISH"
        if rc != 0:
            p["retries"]["G3_PUBLICATION_QUALITY"] += 1
            log(f"G3 WORKER_PUBLISH rc={rc} timeout={timed_out}")
        else:
            p["retries"]["G3_PUBLICATION_QUALITY"] = 0
            log("G3 WORKER_PUBLISH rc=0")

    else:
        s["currentGate"] = "G4_MISSION_CLOSEOUT"
        write_final_synthesis(s, p)
        sync_regina_knowledge_to_corpus()
        s["status"] = "COMPLETE"
        s["lastAction"] = "MISSION_SYNTHESIS_WRITTEN"
        write_terminal_lock()
        log(f"G4 -> LOCKED | wrote {TERMINAL_LOCK.relative_to(ROOT)}")

    s["lastUpdated"] = now()
    write_json(STATE, s)
    write_json(PROG, p)
    print({
        "gate": s["currentGate"],
        "status": s["status"],
        "rowsWritten": p["da"]["rowsWritten"],
        "nextOffset": p["da"]["offset"],
        "lastAction": s.get("lastAction", ""),
    })


if __name__ == "__main__":
    main()
