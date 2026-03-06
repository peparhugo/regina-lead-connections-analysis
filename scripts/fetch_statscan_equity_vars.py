#!/usr/bin/env python3
"""Fetch StatsCan 2016 CPR variables for Regina CT/DA geographies with explicit Regina filters.

Outputs:
- data/derived/statscan_ct_equity_vars_2016_regina.csv
- data/derived/statscan_da_equity_vars_2016_regina.csv
"""

from __future__ import annotations

import csv
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple

import requests

ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"

CR2016_GEO = "https://www12.statcan.gc.ca/rest/census-recensement/CR2016Geo.json"
CPR2016 = "https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json"

OUT_CT = DERIVED / "statscan_ct_equity_vars_2016_regina.csv"
OUT_DA = DERIVED / "statscan_da_equity_vars_2016_regina.csv"

# Regina scope filters (explicit, reproducible):
# - CT: Regina CMA CT DGUID prefix observed in prior official scaffold.
# - DA: Regina CD06 proxy via DA code prefix (4706xx..), keeping pulls Regina-area only.
REGINA_CT_DGUID_PREFIX = "2016S0507705"
REGINA_DA_CODE_PREFIX = "4706"

VARS = {
    # Core housing + income + equity
    "population_total": "1.1.1",
    "private_dwellings_total": "1.1.4",
    "median_after_tax_income_households": "4.2.1.2",
    "lim_at_prevalence_pct": "4.4.3",
    "lim_at_children_0_17_count": "4.4.2.1",
    "lim_at_children_0_17_pct": "4.4.3.1",
    "tenure_total": "9.1.1",
    "tenure_owner": "9.1.1.1",
    "tenure_renter": "9.1.1.2",
    "indigenous_identity_total": "6.1.1",
    "indigenous_identity_count": "6.1.1.1",

    # Child/population age structure
    "age_0_14_total": "1.2.1.1",
    "age_0_4_total": "1.2.1.1.1",
    "age_5_9_total": "1.2.1.1.2",
    "age_10_14_total": "1.2.1.1.3",

    # Additional socioeconomic profile fields (CT-level)
    "immigrant_count": "5.2.1.2",
    "visible_minority_count": "7.1.1.1",
    "lone_parent_family_count": "2.3.5",
    "couples_with_children_count": "2.3.4.2",
    "unemployment_rate_pct": "11.1.4",
    "education_no_certificate_25_64": "10.1.2.1",
    "education_bachelor_or_higher_25_64": "10.1.2.3.4",
}


def get_payload(url: str, **params) -> dict | str:
    r = requests.get(url, params=params, timeout=120)
    r.raise_for_status()
    try:
        return r.json()
    except Exception:
        return r.text


def parse_query_rows(payload: dict | str) -> Tuple[List[str], List[List[str]]]:
    if isinstance(payload, dict):
        cols = payload.get("COLUMNS", [])
        rows = payload.get("DATA", [])
        return cols, rows

    root = ET.fromstring(payload)
    cols = [c.attrib.get("NAME", "") for c in root.find("COLUMNNAMES").findall("COLUMN")]
    rows = []
    for row in root.find("ROWS").findall("ROW"):
        vals = [(c.text or "") for c in row.findall("COLUMN")]
        rows.append(vals)
    return cols, rows


def fetch_geos(geos: str, cpt: str = "47") -> List[dict]:
    cols, rows = parse_query_rows(get_payload(CR2016_GEO, lang="E", geos=geos, cpt=cpt))
    idx = {c: i for i, c in enumerate(cols)}
    out = []
    for r in rows:
        geo_uid = r[idx.get("GEO_UID", 0)]
        geo_code = r[idx.get("GEO_ID_CODE", 3)]

        # Explicit Regina-only filters
        if geos == "CT" and not str(geo_uid).startswith(REGINA_CT_DGUID_PREFIX):
            continue
        if geos == "DA" and not str(geo_code).startswith(REGINA_DA_CODE_PREFIX):
            continue

        out.append(
            {
                "geo_uid": geo_uid,
                "geo_id_code": geo_code,
                "geo_name": r[idx.get("GEO_NAME_NOM", 4)],
                "prov_code": r[idx.get("PROV_TERR_ID_CODE", 1)],
                "geo": geos,
                "regina_filter_tag": "CT_DGUID_PREFIX_2016S0507705" if geos == "CT" else "DA_GEOID_PREFIX_4706",
            }
        )
    return out


def fetch_cpr_vars(dguid: str) -> Dict[str, str]:
    cols, rows = parse_query_rows(get_payload(CPR2016, lang="E", dguid=dguid))
    idx = {c: i for i, c in enumerate(cols)}
    out = {k: "" for k in VARS}
    for r in rows:
        hid = r[idx["HIER_ID"]]
        val = r[idx["T_DATA_DONNEE"]]
        for name, target in VARS.items():
            if hid == target:
                out[name] = val
    return out


def as_float(v, default=0.0):
    try:
        if v in (None, ""):
            return default
        return float(v)
    except Exception:
        return default


def write_rows(rows, out_path: Path, append: bool = False):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if append and out_path.exists() else "w"
    with out_path.open(mode, encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":
            w.writeheader()
        w.writerows(rows)


def build(geos: str, out_path: Path, limit: int = 0, checkpoint_every: int = 20, start: int = 0, append: bool = False):
    items = fetch_geos(geos)
    if start and start > 0:
        items = items[start:]
    if limit and limit > 0:
        items = items[:limit]
    rows = []
    for i, item in enumerate(items, start=1):
        dguid = item["geo_uid"]
        vars_ = fetch_cpr_vars(dguid)

        ten_total = as_float(vars_.get("tenure_total"))
        owner = as_float(vars_.get("tenure_owner"))
        renter = as_float(vars_.get("tenure_renter"))
        ind_total = as_float(vars_.get("indigenous_identity_total"))
        ind_count = as_float(vars_.get("indigenous_identity_count"))

        pop_total = as_float(vars_.get("population_total"))
        age_0_14 = as_float(vars_.get("age_0_14_total"))

        rows.append(
            {
                **item,
                **vars_,
                "tenure_owner_pct": f"{(100.0 * owner / ten_total):.6f}" if ten_total else "",
                "tenure_renter_pct": f"{(100.0 * renter / ten_total):.6f}" if ten_total else "",
                "indigenous_identity_pct": f"{(100.0 * ind_count / ind_total):.6f}" if ind_total else "",
                "children_0_14_pct": f"{(100.0 * age_0_14 / pop_total):.6f}" if pop_total else "",
            }
        )

        if i % checkpoint_every == 0:
            write_rows(rows, out_path, append=append)
            print(f"{geos}: checkpoint {i}/{len(items)}")
            rows = []
            append = True
            time.sleep(0.2)

    if rows:
        write_rows(rows, out_path, append=append)
    return i if 'i' in locals() else 0


def main():
    import os
    mode = os.getenv("STATSCAN_MODE", "ct_first").lower()
    da_limit = int(os.getenv("STATSCAN_DA_LIMIT", "0") or "0")
    da_start = int(os.getenv("STATSCAN_DA_START", "0") or "0")
    da_append = os.getenv("STATSCAN_DA_APPEND", "0").lower() in {"1", "true", "yes"}

    if mode == "ct_only":
        n_ct = build("CT", OUT_CT)
        print({"mode": mode, "ct_rows": n_ct, "ct_out": str(OUT_CT.relative_to(ROOT))})
        return

    if mode == "ct_first":
        n_ct = build("CT", OUT_CT)
        n_da = build("DA", OUT_DA, limit=da_limit if da_limit else 150)
        print({
            "mode": mode,
            "ct_rows": n_ct,
            "da_rows": n_da,
            "ct_out": str(OUT_CT.relative_to(ROOT)),
            "da_out": str(OUT_DA.relative_to(ROOT)),
            "note": "DA is intentionally batched; rerun with STATSCAN_DA_LIMIT or full mode.",
        })
        return

    if mode == "da_only":
        n_da = build("DA", OUT_DA, limit=da_limit if da_limit else 10, start=da_start, append=da_append)
        print({"mode": mode, "da_rows": n_da, "da_out": str(OUT_DA.relative_to(ROOT)), "da_start": da_start, "da_append": da_append})
        return

    # full
    n_ct = build("CT", OUT_CT)
    n_da = build("DA", OUT_DA)
    print({
        "mode": mode,
        "ct_rows": n_ct,
        "da_rows": n_da,
        "ct_out": str(OUT_CT.relative_to(ROOT)),
        "da_out": str(OUT_DA.relative_to(ROOT)),
    })


if __name__ == "__main__":
    main()
