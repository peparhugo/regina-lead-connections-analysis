#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCEN = ROOT / "reports" / "model_scenario_endpoint_uncertainty_2026-03-06.csv"
OUT_CSV = ROOT / "data" / "derived" / "npv_policy_summary_2026-03-06.csv"
OUT_MD = ROOT / "reports" / "npv_policy_summary_2026-03-06.md"

YEARS = 30
DISCOUNT = {"best": 0.05, "base": 0.03, "worst": 0.015}


def annuity_factor(rate: float, years: int) -> float:
    if rate == 0:
        return float(years)
    return (1 - (1 + rate) ** (-years)) / rate


def fnum(v: str, d: float = 0.0) -> float:
    try:
        return float(v)
    except Exception:
        return d


def endpoint_band_values(rows: list[dict], endpoint: str, param: str):
    r = next(x for x in rows if x["endpoint"] == endpoint and x["parameter"] == param)
    p10, p50, p90 = fnum(r["sim_p10"]), fnum(r["sim_p50"]), fnum(r["sim_p90"])
    return p10, p50, p90


def main():
    rows = list(csv.DictReader(SCEN.open("r", encoding="utf-8", newline="")))

    # Convert each endpoint to a positive burden metric
    iq_p10, iq_p50, iq_p90 = endpoint_band_values(rows, "IQ", "iq_delta_points_per_bll_shift")
    adhd_p10, adhd_p50, adhd_p90 = endpoint_band_values(rows, "ADHD", "adhd_or_childhood_lead")
    cvd_p10, cvd_p50, cvd_p90 = endpoint_band_values(rows, "CVD", "sbp_mmHg_per_bll_doubling")
    ckd_p10, ckd_p50, ckd_p90 = endpoint_band_values(rows, "CKD", "ckd_incident_hr_q4_vs_q1q3")

    endpoint_raw = {
        "IQ": {
            "best": min(abs(iq_p10), abs(iq_p50), abs(iq_p90)),
            "base": abs(iq_p50),
            "worst": max(abs(iq_p10), abs(iq_p50), abs(iq_p90)),
            "unit": "|IQ-point decrement|",
        },
        "ADHD": {
            "best": min(adhd_p10, adhd_p50, adhd_p90) - 1.0,
            "base": adhd_p50 - 1.0,
            "worst": max(adhd_p10, adhd_p50, adhd_p90) - 1.0,
            "unit": "OR-1",
        },
        "CVD": {
            "best": min(cvd_p10, cvd_p50, cvd_p90),
            "base": cvd_p50,
            "worst": max(cvd_p10, cvd_p50, cvd_p90),
            "unit": "mmHg/doubling",
        },
        "CKD": {
            "best": min(ckd_p10, ckd_p50, ckd_p90) - 1.0,
            "base": ckd_p50 - 1.0,
            "worst": max(ckd_p10, ckd_p50, ckd_p90) - 1.0,
            "unit": "HR-1",
        },
    }

    out_rows: list[dict] = []
    combined = {"best": 0.0, "base": 0.0, "worst": 0.0}

    for ep, vals in endpoint_raw.items():
        base = vals["base"] if vals["base"] != 0 else 1e-9
        for band in ["best", "base", "worst"]:
            rel = vals[band] / base
            af = annuity_factor(DISCOUNT[band], YEARS)
            npv_index = rel * af
            combined[band] += npv_index
            out_rows.append(
                {
                    "endpoint": ep,
                    "band": band,
                    "discount_rate": DISCOUNT[band],
                    "years": YEARS,
                    "burden_metric_value": f"{vals[band]:.6f}",
                    "burden_unit": vals["unit"],
                    "relative_to_base": f"{rel:.6f}",
                    "npv_index": f"{npv_index:.6f}",
                    "annual_cost_anchor": "1.0",
                    "notes": "Index-only pending CAD calibration",
                }
            )

    # combined caution band rows
    for band in ["best", "base", "worst"]:
        out_rows.append(
            {
                "endpoint": "COMBINED",
                "band": band,
                "discount_rate": DISCOUNT[band],
                "years": YEARS,
                "burden_metric_value": "",
                "burden_unit": "aggregate index",
                "relative_to_base": "",
                "npv_index": f"{combined[band]:.6f}",
                "annual_cost_anchor": "1.0",
                "notes": "Equal-weight sum of endpoint indices (caution band)",
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    md = [
        "# NPV Policy Summary (Index Mode)",
        "",
        "This is a first-pass policy summary using endpoint-separated uncertainty bands.",
        "Values are **index units** (annual_cost_anchor=1) until CAD calibration inputs are finalized.",
        "",
        "## Combined caution band (equal-weight endpoint aggregate)",
        f"- Best: `{combined['best']:.3f}`",
        f"- Base: `{combined['base']:.3f}`",
        f"- Worst: `{combined['worst']:.3f}`",
        "",
        "Interpretation: higher value = larger long-horizon burden under chosen band/discount assumptions.",
        "",
        "## Endpoint-level bands",
        "| Endpoint | Best NPV index | Base NPV index | Worst NPV index |",
        "|---|---:|---:|---:|",
    ]

    for ep in ["IQ", "ADHD", "CVD", "CKD"]:
        get = lambda b: next(float(r["npv_index"]) for r in out_rows if r["endpoint"] == ep and r["band"] == b)
        md.append(f"| {ep} | {get('best'):.3f} | {get('base'):.3f} | {get('worst'):.3f} |")

    md += [
        "",
        "## Guardrails",
        "- Not a monetary estimate yet; this is scenario indexing only.",
        "- Convert to CAD by attaching endpoint-specific annual cost anchors (CIHI/provincial + productivity assumptions).",
        "- Preserve endpoint-specific uncertainty; avoid single-point collapse.",
    ]

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print({"ok": True, "csv": str(OUT_CSV.relative_to(ROOT)), "md": str(OUT_MD.relative_to(ROOT))})


if __name__ == "__main__":
    main()
