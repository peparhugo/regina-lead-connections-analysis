#!/usr/bin/env python3
"""Build Regina-only CT equity panel with explicit official vs inferred fields.

Official inputs:
- data/derived/statscan_ct_equity_vars_2016_regina.csv (StatsCan CPR vars)

Inferred inputs:
- data/derived/area_priority_signals.csv (citywide lead/replacement baseline)

Outputs:
- data/derived/ct_equity_panel_official_2026-03-06_regina.csv
- data/derived/equity_significance_results_official_ct_2026-03-06_regina.csv
"""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"

IN_CT = DERIVED / "statscan_ct_equity_vars_2016_regina.csv"
AREA_SIGNALS = DERIVED / "area_priority_signals.csv"
STRICT_MONTHLY = DERIVED / "strict_replacements_by_area_month.csv"

OUT_PANEL = DERIVED / "ct_equity_panel_official_2026-03-06_regina.csv"
OUT_TESTS = DERIVED / "equity_significance_results_official_ct_2026-03-06_regina.csv"


def as_float(v, default=0.0):
    try:
        if v in (None, ""):
            return default
        return float(v)
    except Exception:
        return default


def read_csv(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: List[dict], fieldnames: List[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def rankdata(values: List[float]) -> List[float]:
    idx = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[idx[j + 1]] == values[idx[i]]:
            j += 1
        avg = (i + j + 2) / 2.0
        for k in range(i, j + 1):
            ranks[idx[k]] = avg
        i = j + 1
    return ranks


def pearson(x: List[float], y: List[float]) -> float:
    n = len(x)
    if n == 0:
        return float("nan")
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denx = math.sqrt(sum((a - mx) ** 2 for a in x))
    deny = math.sqrt(sum((b - my) ** 2 for b in y))
    return num / (denx * deny) if denx and deny else float("nan")


def spearman(x: List[float], y: List[float]) -> float:
    return pearson(rankdata(x), rankdata(y))


def permutation_p_corr(x, y, reps=5000, seed=42):
    rnd = random.Random(seed)
    obs = abs(spearman(x, y))
    yy = list(y)
    cnt = 0
    for _ in range(reps):
        rnd.shuffle(yy)
        if abs(spearman(x, yy)) >= obs:
            cnt += 1
    return (cnt + 1) / (reps + 1)


def simple_ols(y: List[float], x: List[float]):
    n = len(y)
    if n < 3:
        return float("nan"), float("nan"), float("nan")
    mx = sum(x) / n
    my = sum(y) / n
    sxx = sum((xi - mx) ** 2 for xi in x)
    if sxx == 0:
        return float("nan"), float("nan"), float("nan")
    sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    b1 = sxy / sxx
    b0 = my - b1 * mx
    resid = [yi - (b0 + b1 * xi) for xi, yi in zip(x, y)]
    sigma2 = sum(r * r for r in resid) / (n - 2)
    se = math.sqrt(sigma2 / sxx) if sxx > 0 else float("nan")
    t = b1 / se if se and se == se else float("nan")
    return b1, se, t


def main():
    import os

    ct_rows = read_csv(IN_CT)
    sig_rows = read_csv(AREA_SIGNALS)
    strict_monthly_rows = read_csv(STRICT_MONTHLY) if STRICT_MONTHLY.exists() else []

    # User requested problem-era analysis from 2019 forward.
    start_year = int(os.getenv("REGINA_START_YEAR", "2019") or "2019")

    city_lead_total = sum(as_float(r.get("lead_total")) for r in sig_rows)
    city_wc_total = sum(as_float(r.get("wc_total")) for r in sig_rows)

    # strict replacements constrained to post-start_year if monthly source is available.
    if strict_monthly_rows:
        city_strict = sum(
            as_float(r.get("count"))
            for r in strict_monthly_rows
            if str(r.get("month", ""))[:4].isdigit() and int(str(r.get("month", ""))[:4]) >= start_year
        )
    else:
        city_strict = sum(as_float(r.get("strict_replaced")) for r in sig_rows)

    city_lead_per = (100.0 * city_lead_total / city_wc_total) if city_wc_total else 0.0
    city_strict_rate = (city_strict / city_lead_total) if city_lead_total else 0.0

    # Pass 1: raw CT vulnerability allocations, later normalized to known city totals.
    raw_panel = []
    for r in ct_rows:
        dguid = r.get("geo_uid", "")
        if not dguid.startswith("2016S0507705"):
            continue

        dwell = as_float(r.get("private_dwellings_total"), 0.0)
        renter = as_float(r.get("tenure_renter_pct"), 0.0)
        lim = as_float(r.get("lim_at_prevalence_pct"), 0.0)
        ind = as_float(r.get("indigenous_identity_pct"), 0.0)

        vulnerability = 1.0 + 0.004 * renter + 0.010 * lim + 0.006 * ind
        active_proxy = dwell * (city_lead_per / 100.0) * vulnerability
        strict_proxy = active_proxy * city_strict_rate
        strict_rate = (strict_proxy / active_proxy) if active_proxy else 0.0

        pop_total = as_float(r.get("population_total"))
        age_0_14 = as_float(r.get("age_0_14_total"))
        persons_per_dwelling = (pop_total / dwell) if dwell else 0.0
        impacted_people_est = active_proxy * persons_per_dwelling if persons_per_dwelling else 0.0
        children_share = (age_0_14 / pop_total) if pop_total else 0.0
        impacted_children_0_14_est = impacted_people_est * children_share if children_share else 0.0

        raw_panel.append(
            {
                "as_of_date": "2026-03-06",
                "geography_level": "CT_official_regina",
                "ct_dguid": dguid,
                "ct_uid_code": r.get("geo_id_code", ""),
                "ct_name": f"CT {r.get('geo_name','').strip()}" if r.get('geo_name') else "",
                "strict_replaced": f"{strict_proxy:.3f}",
                "active_lead_count": f"{active_proxy:.3f}",
                "strict_repl_rate_vs_active_lead": f"{strict_rate:.6f}",
                "population_total": r.get("population_total", ""),
                "age_0_14_total": r.get("age_0_14_total", ""),
                "age_0_4_total": r.get("age_0_4_total", ""),
                "age_5_9_total": r.get("age_5_9_total", ""),
                "age_10_14_total": r.get("age_10_14_total", ""),
                "children_0_14_pct": r.get("children_0_14_pct", ""),
                "private_dwellings_total": r.get("private_dwellings_total", ""),
                "tenure_total": r.get("tenure_total", ""),
                "tenure_owner": r.get("tenure_owner", ""),
                "tenure_renter": r.get("tenure_renter", ""),
                "tenure_owner_pct": r.get("tenure_owner_pct", ""),
                "tenure_renter_pct": r.get("tenure_renter_pct", ""),
                "median_after_tax_income_households": r.get("median_after_tax_income_households", ""),
                "lim_at_prevalence_pct": r.get("lim_at_prevalence_pct", ""),
                "lim_at_children_0_17_count": r.get("lim_at_children_0_17_count", ""),
                "lim_at_children_0_17_pct": r.get("lim_at_children_0_17_pct", ""),
                "immigrant_count": r.get("immigrant_count", ""),
                "visible_minority_count": r.get("visible_minority_count", ""),
                "lone_parent_family_count": r.get("lone_parent_family_count", ""),
                "couples_with_children_count": r.get("couples_with_children_count", ""),
                "unemployment_rate_pct": r.get("unemployment_rate_pct", ""),
                "education_no_certificate_25_64": r.get("education_no_certificate_25_64", ""),
                "education_bachelor_or_higher_25_64": r.get("education_bachelor_or_higher_25_64", ""),
                "indigenous_identity_total": r.get("indigenous_identity_total", ""),
                "indigenous_identity_count": r.get("indigenous_identity_count", ""),
                "indigenous_identity_pct": r.get("indigenous_identity_pct", ""),
                "impacted_people_est": f"{impacted_people_est:.3f}",
                "impacted_children_0_14_est": f"{impacted_children_0_14_est:.3f}",
                "notes": "Official StatsCan CT covariates (Regina-only). Replacement fields are inferred proxies using city baseline from area_priority_signals.csv.",
            }
        )

    # Normalize CT allocations to known city totals so aggregate active/replaced are not overstated.
    raw_active_sum = sum(as_float(r.get("active_lead_count")) for r in raw_panel)
    raw_strict_sum = sum(as_float(r.get("strict_replaced")) for r in raw_panel)
    scale_active = (city_lead_total / raw_active_sum) if raw_active_sum else 1.0
    scale_strict = (city_strict / raw_strict_sum) if raw_strict_sum else 1.0

    panel = []
    for r in raw_panel:
        active = as_float(r.get("active_lead_count")) * scale_active
        strict = as_float(r.get("strict_replaced")) * scale_strict
        ppl = as_float(r.get("impacted_people_est")) * scale_active
        kids = as_float(r.get("impacted_children_0_14_est")) * scale_active
        rr = (strict / active) if active else 0.0

        rr2 = dict(r)
        rr2["active_lead_count"] = f"{active:.3f}"
        rr2["strict_replaced"] = f"{strict:.3f}"
        rr2["strict_repl_rate_vs_active_lead"] = f"{rr:.6f}"
        rr2["impacted_people_est"] = f"{ppl:.3f}"
        rr2["impacted_children_0_14_est"] = f"{kids:.3f}"
        rr2["notes"] = (
            "Official StatsCan CT covariates (Regina-only). Lead/replacement fields are inferred CT allocations normalized to city totals; "
            f"strict replacements constrained to >= {start_year} from monthly series when available."
        )
        panel.append(rr2)

    fields = list(panel[0].keys()) if panel else []
    write_csv(OUT_PANEL, panel, fields)

    y = [as_float(r["strict_replaced"]) for r in panel]
    x_inc = [as_float(r["median_after_tax_income_households"]) for r in panel]
    x_rent = [as_float(r["tenure_renter_pct"]) for r in panel]
    x_ind = [as_float(r["indigenous_identity_pct"]) for r in panel]

    tests = []
    for name, x in [("income", x_inc), ("renter_pct", x_rent), ("indigenous_identity_pct", x_ind)]:
        rho = spearman(x, y)
        p = permutation_p_corr(x, y)
        b1, se, t = simple_ols(y, x)
        tests.append(
            {
                "test_id": f"spearman_perm::{name}",
                "test_family": "nonparametric",
                "n": len(panel),
                "estimate": f"{rho:.6f}",
                "p_value": f"{p:.6f}",
                "interpretation": f"Association between {name} and inferred strict replacements.",
                "caveat": "Outcome is inferred proxy; directional only.",
            }
        )
        tests.append(
            {
                "test_id": f"ols_slope::{name}",
                "test_family": "regression",
                "n": len(panel),
                "estimate": f"{b1:.6f}" if b1 == b1 else "",
                "p_value": "",
                "interpretation": f"Univariate OLS slope, t_stat={t:.4f}, se={se:.6f}",
                "caveat": "No robust p-value here; screening only.",
            }
        )

    write_csv(
        OUT_TESTS,
        tests,
        ["test_id", "test_family", "n", "estimate", "p_value", "interpretation", "caveat"],
    )

    print(
        {
            "ct_count": len(panel),
            "panel": str(OUT_PANEL.relative_to(ROOT)),
            "tests": str(OUT_TESTS.relative_to(ROOT)),
            "regina_filter": "CT_DGUID_PREFIX_2016S0507705",
            "replacement_mode": "INFERRED_PROXY",
        }
    )


if __name__ == "__main__":
    main()
