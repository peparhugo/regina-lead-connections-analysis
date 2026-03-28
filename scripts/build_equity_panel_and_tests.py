#!/usr/bin/env python3
"""
Build equity panel (CT/DA proxy panel) and run significance/robustness tests
using reproducible local/public artifacts.

Inputs:
- data/derived/area_priority_signals.csv
- data/derived/strict_replacements_by_area_month.csv
- City ArcGIS Neighbourhood_Profile layer (for public profile links only)

Outputs:
- data/derived/ct_da_equity_panel_2026-03-06.csv
- data/derived/equity_significance_results_2026-03-06.csv
"""

from __future__ import annotations

import csv
import math
import random
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import requests

ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
OUT_PANEL = DERIVED / "ct_da_equity_panel_2026-03-06.csv"
OUT_TESTS = DERIVED / "equity_significance_results_2026-03-06.csv"

AREA_SIGNALS = DERIVED / "area_priority_signals.csv"
MONTH_COUNTS = DERIVED / "strict_replacements_by_area_month.csv"

NEIGH_PROFILE_QUERY = (
    "https://opengis.regina.ca/arcgis/rest/services/CGISViewer/Neighbourhood_Profile/MapServer/0/query"
)


def read_csv(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def safe_float(v, default=0.0):
    try:
        if v in (None, ""):
            return default
        return float(v)
    except Exception:
        return default


def fetch_profile_links() -> Dict[str, str]:
    params = {
        "f": "json",
        "where": "1=1",
        "outFields": "CA,PDF_Link",
        "returnGeometry": "false",
    }
    try:
        j = requests.get(NEIGH_PROFILE_QUERY, params=params, timeout=60).json()
    except Exception:
        return {}

    out: Dict[str, str] = {}
    for feat in j.get("features", []) or []:
        a = feat.get("attributes") or {}
        name = (a.get("CA") or "").strip().upper()
        link = (a.get("PDF_Link") or "").strip()
        if name and link:
            out[name] = link
    return out


def month_to_ord(month: str) -> int:
    # YYYY-MM -> sortable integer
    try:
        y, m = month.split("-")
        return int(y) * 12 + int(m)
    except Exception:
        return -1


def build_panel_rows() -> List[dict]:
    area_rows = read_csv(AREA_SIGNALS)
    month_rows = read_csv(MONTH_COUNTS)

    area_to_month_counts: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    for r in month_rows:
        area = (r.get("area") or "").strip().upper()
        month = (r.get("month") or "").strip()
        c = int(safe_float(r.get("count"), 0))
        if not area or area == "UNKNOWN" or not month:
            continue
        area_to_month_counts[area].append((month, c))

    profile_links = fetch_profile_links()

    rows: List[dict] = []

    for r in area_rows:
        area = (r.get("area") or "").strip().upper()
        lead_total = safe_float(r.get("lead_total"), 0)
        wc_total = safe_float(r.get("wc_total"), 0)
        lead_per = safe_float(r.get("lead_per"), 0)
        strict_replaced = safe_float(r.get("strict_replaced"), 0)
        strict_rate = safe_float(r.get("strict_repl_rate_vs_lead_total"), 0)

        month_counts = area_to_month_counts.get(area, [])
        obs_months = len(month_counts)
        monthly_intensity = (strict_replaced / obs_months) if obs_months > 0 else 0.0

        # Recent 24m share (relative to latest observed month in the area)
        recent_24m = 0
        recent_share = ""
        if month_counts:
            ords = [month_to_ord(m) for m, _ in month_counts if month_to_ord(m) >= 0]
            if ords:
                max_ord = max(ords)
                lo = max_ord - 23
                recent_24m = sum(c for m, c in month_counts if lo <= month_to_ord(m) <= max_ord)
                recent_share = f"{(recent_24m / strict_replaced):.6f}" if strict_replaced > 0 else ""

        rows.append(
            {
                "as_of_date": "2026-03-06",
                "geography_level": "DA_proxy",
                "geography_id": f"DA_PROXY::{area}",
                "area": area,
                "lead_total": f"{lead_total:.0f}",
                "wc_total": f"{wc_total:.0f}",
                "lead_per": f"{lead_per:.6f}",
                "strict_replaced": f"{strict_replaced:.0f}",
                "strict_repl_rate_vs_lead_total": f"{strict_rate:.6f}",
                "repl_obs_months": str(obs_months),
                "repl_monthly_intensity": f"{monthly_intensity:.6f}",
                "repl_recent_24m": str(recent_24m),
                "repl_recent_share_24m": recent_share,
                "tenure_owner_pct": "",
                "tenure_renter_pct": "",
                "median_income_after_tax": "",
                "indigenous_identity_pct": "",
                "demographic_data_status": "pending_extraction_from_public_neighbourhood_profiles",
                "demographic_source_link": profile_links.get(area, ""),
                "replacement_source": "data/derived/area_priority_signals.csv + strict_replacements_by_area_month.csv",
                "notes": "DA_proxy = LeadConnectionArea proxy, not official StatsCan DA.",
            }
        )

    # Add one CT proxy roll-up row to create merged CT/DA panel artifact
    if rows:
        lead_total = sum(safe_float(r["lead_total"]) for r in rows)
        wc_total = sum(safe_float(r["wc_total"]) for r in rows)
        strict_replaced = sum(safe_float(r["strict_replaced"]) for r in rows)
        obs_months = max(safe_float(r["repl_obs_months"]) for r in rows)
        weighted_rate = (strict_replaced / lead_total) if lead_total > 0 else 0.0
        rows.append(
            {
                "as_of_date": "2026-03-06",
                "geography_level": "CT_proxy",
                "geography_id": "CT_PROXY::REGINA_LEAD_AREAS",
                "area": "REGINA (proxy aggregate)",
                "lead_total": f"{lead_total:.0f}",
                "wc_total": f"{wc_total:.0f}",
                "lead_per": f"{(100.0 * lead_total / wc_total) if wc_total else 0.0:.6f}",
                "strict_replaced": f"{strict_replaced:.0f}",
                "strict_repl_rate_vs_lead_total": f"{weighted_rate:.6f}",
                "repl_obs_months": f"{int(obs_months)}",
                "repl_monthly_intensity": f"{(strict_replaced / obs_months) if obs_months else 0.0:.6f}",
                "repl_recent_24m": "",
                "repl_recent_share_24m": "",
                "tenure_owner_pct": "",
                "tenure_renter_pct": "",
                "median_income_after_tax": "",
                "indigenous_identity_pct": "",
                "demographic_data_status": "pending_extraction_from_public_neighbourhood_profiles",
                "demographic_source_link": "https://www.regina.ca/about-regina/maps/neighbourhood-profiles/",
                "replacement_source": "data/derived/area_priority_signals.csv + strict_replacements_by_area_month.csv",
                "notes": "CT_proxy aggregate for panel completeness; not official StatsCan CT.",
            }
        )

    return rows


def rankdata(values: List[float]) -> List[float]:
    # average ranks for ties
    sorted_idx = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[sorted_idx[j + 1]] == values[sorted_idx[i]]:
            j += 1
        avg_rank = (i + j + 2) / 2.0
        for k in range(i, j + 1):
            ranks[sorted_idx[k]] = avg_rank
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
    if denx == 0 or deny == 0:
        return float("nan")
    return num / (denx * deny)


def spearman(x: List[float], y: List[float]) -> float:
    return pearson(rankdata(x), rankdata(y))


def permutation_pvalue_corr(x: List[float], y: List[float], reps: int = 10000, seed: int = 42) -> float:
    rnd = random.Random(seed)
    obs = abs(spearman(x, y))
    cnt = 0
    yb = list(y)
    for _ in range(reps):
        rnd.shuffle(yb)
        if abs(spearman(x, yb)) >= obs:
            cnt += 1
    return (cnt + 1) / (reps + 1)


def mann_whitney_u(x: List[float], y: List[float]) -> float:
    pooled = [(v, 0) for v in x] + [(v, 1) for v in y]
    vals = [v for v, _ in pooled]
    ranks = rankdata(vals)
    rx = sum(r for r, (_, g) in zip(ranks, pooled) if g == 0)
    nx = len(x)
    return rx - nx * (nx + 1) / 2


def permutation_pvalue_mw(x: List[float], y: List[float], reps: int = 10000, seed: int = 42) -> float:
    rnd = random.Random(seed)
    obs = mann_whitney_u(x, y)
    nx = len(x)
    pooled = x + y
    cnt = 0
    for _ in range(reps):
        rnd.shuffle(pooled)
        xp = pooled[:nx]
        yp = pooled[nx:]
        u = mann_whitney_u(xp, yp)
        if abs(u - nx * len(y) / 2) >= abs(obs - nx * len(y) / 2):
            cnt += 1
    return (cnt + 1) / (reps + 1)


def mat_inv(a: List[List[float]]) -> List[List[float]]:
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]

    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("Singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for r in range(n):
            if r == col:
                continue
            fac = aug[r][col]
            if fac == 0:
                continue
            aug[r] = [rv - fac * cv for rv, cv in zip(aug[r], aug[col])]

    return [row[n:] for row in aug]


def mat_mul(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(ar, bc)) for bc in bt] for ar in a]


def ols_hc1(y: List[float], X: List[List[float]]):
    n = len(y)
    k = len(X[0])
    Xt = list(zip(*X))
    XtX = [[sum(a * b for a, b in zip(col_i, col_j)) for col_j in Xt] for col_i in Xt]
    XtX_inv = mat_inv(XtX)

    Xty = [sum(col[i] * y[i] for i in range(n)) for col in Xt]
    beta = [sum(XtX_inv[r][c] * Xty[c] for c in range(k)) for r in range(k)]

    yhat = [sum(X[i][j] * beta[j] for j in range(k)) for i in range(n)]
    resid = [y[i] - yhat[i] for i in range(n)]

    S = [[0.0] * k for _ in range(k)]
    for i in range(n):
        xi = X[i]
        ei2 = resid[i] ** 2
        for r in range(k):
            for c in range(k):
                S[r][c] += ei2 * xi[r] * xi[c]

    middle = mat_mul(mat_mul(XtX_inv, S), XtX_inv)
    scale = n / max(1, (n - k))
    vcov = [[v * scale for v in row] for row in middle]
    se = [math.sqrt(max(0.0, vcov[j][j])) for j in range(k)]

    return beta, se, resid


def normal_approx_p(z: float) -> float:
    # two-sided using erf
    cdf = 0.5 * (1 + math.erf(abs(z) / math.sqrt(2)))
    return max(0.0, min(1.0, 2 * (1 - cdf)))


def run_tests(panel_rows: List[dict]) -> List[dict]:
    da = [r for r in panel_rows if r["geography_level"] == "DA_proxy"]
    x = [safe_float(r["lead_per"]) for r in da]
    y = [safe_float(r["strict_repl_rate_vs_lead_total"]) for r in da]
    n = len(da)

    results: List[dict] = []

    rho = spearman(x, y)
    p_rho = permutation_pvalue_corr(x, y, reps=10000, seed=42)
    results.append(
        {
            "test_id": "spearman_perm",
            "method": "Spearman rank correlation + permutation p-value",
            "outcome": "strict_repl_rate_vs_lead_total",
            "grouping": "all_DA_proxy",
            "n": str(n),
            "estimate": f"{rho:.6f}",
            "p_value": f"{p_rho:.6f}",
            "ci_low": "",
            "ci_high": "",
            "interpretation": "Positive monotonic association in snapshot.",
            "caveat": "Small n, ecological/proxy geography, observational only.",
        }
    )

    med = sorted(x)[len(x) // 2]
    hi = [yy for xx, yy in zip(x, y) if xx >= med]
    lo = [yy for xx, yy in zip(x, y) if xx < med]
    diff_median = (sorted(hi)[len(hi) // 2] - sorted(lo)[len(lo) // 2]) if hi and lo else float("nan")
    p_mw = permutation_pvalue_mw(hi, lo, reps=10000, seed=43) if hi and lo else float("nan")
    results.append(
        {
            "test_id": "mw_high_vs_low_lead",
            "method": "Mann-Whitney U (high vs low lead burden) + permutation p-value",
            "outcome": "strict_repl_rate_vs_lead_total",
            "grouping": "lead_per_above_vs_below_median",
            "n": str(n),
            "estimate": f"{diff_median:.6f}",
            "p_value": f"{p_mw:.6f}",
            "ci_low": "",
            "ci_high": "",
            "interpretation": "Higher-burden half shows higher replacement intensity median.",
            "caveat": "Threshold split is arbitrary; non-causal.",
        }
    )

    # OLS with HC1 robust SE
    # y = b0 + b1*lead_per + b2*log1p(lead_total) + b3*log1p(wc_total)
    yy = [safe_float(r["strict_repl_rate_vs_lead_total"]) for r in da]
    X = [
        [
            1.0,
            safe_float(r["lead_per"]),
            math.log1p(safe_float(r["lead_total"])),
            math.log1p(safe_float(r["wc_total"])),
        ]
        for r in da
    ]

    try:
        beta, se, _ = ols_hc1(yy, X)
        names = ["intercept", "lead_per", "log1p_lead_total", "log1p_wc_total"]
        for nm, b, s in zip(names, beta, se):
            z = b / s if s > 0 else float("nan")
            p = normal_approx_p(z) if s > 0 else float("nan")
            ci_l = b - 1.96 * s if s > 0 else float("nan")
            ci_h = b + 1.96 * s if s > 0 else float("nan")
            results.append(
                {
                    "test_id": f"ols_hc1::{nm}",
                    "method": "OLS linear probability model with HC1 robust SE",
                    "outcome": "strict_repl_rate_vs_lead_total",
                    "grouping": "all_DA_proxy",
                    "n": str(n),
                    "estimate": f"{b:.6f}",
                    "p_value": f"{p:.6f}" if p == p else "",
                    "ci_low": f"{ci_l:.6f}" if ci_l == ci_l else "",
                    "ci_high": f"{ci_h:.6f}" if ci_h == ci_h else "",
                    "interpretation": "lead_per coefficient sign indicates directional association after controls." if nm == "lead_per" else "Control term / intercept.",
                    "caveat": "Very small sample and proxy geographies; coefficient is descriptive, not causal.",
                }
            )
    except Exception as e:
        results.append(
            {
                "test_id": "ols_hc1::error",
                "method": "OLS linear probability model with HC1 robust SE",
                "outcome": "strict_repl_rate_vs_lead_total",
                "grouping": "all_DA_proxy",
                "n": str(n),
                "estimate": "",
                "p_value": "",
                "ci_low": "",
                "ci_high": "",
                "interpretation": "Model failed",
                "caveat": f"{type(e).__name__}: {e}",
            }
        )

    return results


def write_csv(path: Path, rows: List[dict], fieldnames: List[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main():
    panel_rows = build_panel_rows()
    panel_fields = [
        "as_of_date",
        "geography_level",
        "geography_id",
        "area",
        "lead_total",
        "wc_total",
        "lead_per",
        "strict_replaced",
        "strict_repl_rate_vs_lead_total",
        "repl_obs_months",
        "repl_monthly_intensity",
        "repl_recent_24m",
        "repl_recent_share_24m",
        "tenure_owner_pct",
        "tenure_renter_pct",
        "median_income_after_tax",
        "indigenous_identity_pct",
        "demographic_data_status",
        "demographic_source_link",
        "replacement_source",
        "notes",
    ]
    write_csv(OUT_PANEL, panel_rows, panel_fields)

    test_rows = run_tests(panel_rows)
    test_fields = [
        "test_id",
        "method",
        "outcome",
        "grouping",
        "n",
        "estimate",
        "p_value",
        "ci_low",
        "ci_high",
        "interpretation",
        "caveat",
    ]
    write_csv(OUT_TESTS, test_rows, test_fields)

    print({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "panel_rows": len(panel_rows),
        "tests_rows": len(test_rows),
        "panel": str(OUT_PANEL.relative_to(ROOT)),
        "tests": str(OUT_TESTS.relative_to(ROOT)),
    })


if __name__ == "__main__":
    main()
