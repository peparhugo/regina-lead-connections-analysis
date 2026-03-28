#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
import random
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
PRIORS = ROOT / "reports" / "model_parameter_priors_2026-03-06.csv"
OUT_CSV = ROOT / "reports" / "model_scenario_endpoint_uncertainty_2026-03-06.csv"
OUT_MD = ROOT / "reports" / "model_scenario_endpoint_uncertainty_2026-03-06.md"


def parse_float(v, default=None):
    try:
        return float(v)
    except Exception:
        return default


def draw_value(row: dict, rnd: random.Random):
    dist = (row.get("distribution") or "").lower()
    b = parse_float(row.get("base_case"))
    lo = parse_float(row.get("low"), b)
    hi = parse_float(row.get("high"), b)

    if dist == "normal" and b is not None and lo is not None and hi is not None:
        sd = abs(hi - lo) / 3.92 if hi != lo else max(abs(b) * 0.05, 1e-6)
        return rnd.gauss(b, sd)

    if dist == "lognormal" and b and lo and hi and b > 0 and lo > 0 and hi > 0:
        sigma = (math.log(hi) - math.log(lo)) / 3.92 if hi != lo else 0.1
        mu = math.log(b)
        return math.exp(rnd.gauss(mu, sigma))

    if dist == "categorical":
        # deterministic map to scores for scenario comparability
        m = {"uncertain": 0.0, "mixed_positive": 0.5, "positive": 1.0}
        return m.get((row.get("base_case") or "").strip(), 0.5)

    return b if b is not None else 0.0


def summarize(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return (None, None, None)
    p10 = s[max(0, int(0.10 * (n - 1)))]
    p50 = median(s)
    p90 = s[min(n - 1, int(0.90 * (n - 1)))]
    return p10, p50, p90


def main():
    if not PRIORS.exists():
        raise SystemExit(f"Missing priors file: {PRIORS}")

    rows = list(csv.DictReader(PRIORS.open("r", encoding="utf-8", newline="")))
    rnd = random.Random(42)
    draws = 5000

    out = []
    by_endpoint = {}

    for r in rows:
        vals = [draw_value(r, rnd) for _ in range(draws)]
        p10, p50, p90 = summarize(vals)
        rec = {
            "endpoint": r.get("endpoint", ""),
            "parameter": r.get("parameter", ""),
            "distribution": r.get("distribution", ""),
            "unit": r.get("unit", ""),
            "input_base_case": r.get("base_case", ""),
            "input_low": r.get("low", ""),
            "input_high": r.get("high", ""),
            "sim_p10": f"{p10:.6f}" if isinstance(p10, (int, float)) else "",
            "sim_p50": f"{p50:.6f}" if isinstance(p50, (int, float)) else "",
            "sim_p90": f"{p90:.6f}" if isinstance(p90, (int, float)) else "",
            "confidence": r.get("confidence", ""),
            "source_study": r.get("source_study", ""),
        }
        out.append(rec)
        by_endpoint.setdefault(r.get("endpoint", ""), []).append(rec)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    lines = [
        "# Endpoint-Separated Uncertainty Scenario Summary",
        "",
        "Generated from priors in `model_parameter_priors_2026-03-06.csv`.",
        f"Monte Carlo draws per parameter: {draws}",
        "",
    ]
    for ep, recs in by_endpoint.items():
        lines.append(f"## {ep}")
        for r in recs:
            lines.append(
                f"- `{r['parameter']}` ({r['distribution']}): P10={r['sim_p10']}, P50={r['sim_p50']}, P90={r['sim_p90']} [{r['unit']}]"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print({"ok": True, "rows": len(out), "csv": str(OUT_CSV.relative_to(ROOT)), "md": str(OUT_MD.relative_to(ROOT))})


if __name__ == "__main__":
    main()
