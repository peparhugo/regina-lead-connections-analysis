#!/usr/bin/env python3
"""Advance-loop for StatsCan table/variable pinning.

What it does per tick:
1) Run pin_statscan_variable_ids.py to refresh pinned HIER IDs.
2) Read reports/statscan_table_inventory_regina_equity_2026-03-06.csv.
3) Promote pending rows to pinned_hier_id when a mapped indicator exists.
4) Write reports/statscan_table_inventory_regina_equity_2026-03-06.advanced.csv.
5) Append a run summary to reports/table_advance_loop_log.md.

Usage:
  python3 scripts/regina_table_advance_loop.py --once
  python3 scripts/regina_table_advance_loop.py --iterations 6 --sleep 120
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "reports" / "statscan_table_inventory_regina_equity_2026-03-06.csv"
PINNED = ROOT / "reports" / "statscan_variable_ids_pinned_2026-03-06.csv"
OUT = ROOT / "reports" / "statscan_table_inventory_regina_equity_2026-03-06.advanced.csv"
LOG = ROOT / "reports" / "table_advance_loop_log.md"

TOPIC_TO_INDICATORS = {
    "tenure": ["tenure_owner", "tenure_renter", "tenure_total"],
    "income": ["median_after_tax_income_households", "lim_at_prevalence_pct"],
    "indigenous": ["indigenous_identity_total", "indigenous_identity_count"],
    "demographics": ["age_0_14_total"],
    "housing": ["private_dwellings_total"],
}


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def run_pin_worker() -> tuple[int, str, str]:
    p = subprocess.run(
        ["python3", "scripts/pin_statscan_variable_ids.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=180,
    )
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def load_pinned() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not PINNED.exists():
        return mapping
    with PINNED.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            mapping[row.get("indicator", "").strip()] = row.get("hier_id", "").strip()
    return mapping


def advance_inventory(pinned: dict[str, str]) -> tuple[int, int]:
    with INVENTORY.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        headers = list(rows[0].keys()) if rows else []

    if "advance_note" not in headers:
        headers.append("advance_note")

    promoted = 0
    pending = 0
    for row in rows:
        status = (row.get("status") or "").strip()
        topic = (row.get("topic") or "").strip().lower()

        if status == "pending_table_pin":
            pending += 1
            candidates = TOPIC_TO_INDICATORS.get(topic, [])
            hit = None
            for key in candidates:
                if pinned.get(key):
                    hit = f"{key}:{pinned[key]}"
                    break

            if hit:
                row["status"] = "pinned_hier_id"
                row["advance_note"] = f"{now()} matched {hit}"
                promoted += 1
            else:
                row["advance_note"] = f"{now()} no match yet"

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        w.writerows(rows)

    return pending, promoted


def append_log(line: str):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Table Advance Loop Log\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"\n- {line}")


def tick() -> dict:
    rc, out, err = run_pin_worker()
    pinned = load_pinned()
    pending, promoted = advance_inventory(pinned)
    summary = {
        "at": now(),
        "pin_rc": rc,
        "pinned_count": len([k for k, v in pinned.items() if v]),
        "pending_seen": pending,
        "promoted": promoted,
        "advanced_csv": str(OUT.relative_to(ROOT)),
    }
    append_log(
        f"{summary['at']} | rc={rc} pinned={summary['pinned_count']} pending={pending} promoted={promoted}"
    )
    if out:
        append_log(f"pin_stdout: {out[:400]}")
    if err:
        append_log(f"pin_stderr: {err[:400]}")
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--iterations", type=int, default=1)
    ap.add_argument("--sleep", type=int, default=60)
    args = ap.parse_args()

    n = 1 if args.once else max(1, args.iterations)
    for i in range(n):
        summary = tick()
        print(summary)
        if i < n - 1:
            time.sleep(max(1, args.sleep))


if __name__ == "__main__":
    main()
