#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

import shapefile  # pyshp
from pyproj import Transformer

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data" / "derived" / "ct_equity_panel_official_2026-03-06_regina.csv"
SHP = ROOT / "data" / "raw" / "ct_boundary_2021" / "lct_000b21a_e.shp"
OUT_GEOJSON = ROOT / "data" / "derived" / "ct_factor_diagnostics_kepler_2026-03-06.geojson"
OUT_CSV = ROOT / "data" / "derived" / "ct_factor_diagnostics_kepler_2026-03-06.csv"
OUT_CROSSWALK = ROOT / "reports" / "ct_geometry_crosswalk_2026-03-06.csv"

# Deterministic surrogate mapping for CTUIDs that no longer exist in 2021 boundary vintage.
SURROGATE = {
    "7050004.00": "7050004.01",
    "7050006.00": "7050006.01",
    "7050100.04": "7050100.05",
    "7050100.09": "7050100.10",
    "7050100.12": "7050100.11",
}


def f(v: str) -> float:
    try:
        return float(v)
    except Exception:
        return 0.0


def main():
    panel_rows = list(csv.DictReader(PANEL.open("r", encoding="utf-8", newline="")))
    panel_by_ct = {r["ct_uid_code"]: r for r in panel_rows}

    r = shapefile.Reader(str(SHP))
    geom_by_ct = {}
    for sr in r.iterShapeRecords():
        rec = sr.record.as_dict()
        ctuid = rec.get("CTUID", "")
        if rec.get("PRUID") == "47" and ctuid.startswith("705"):
            geom_by_ct[ctuid] = sr.shape

    tr = Transformer.from_crs("EPSG:3347", "EPSG:4326", always_xy=True)

    features = []
    crosswalk_rows = []
    matched = 0
    surrogate = 0

    for ctuid, prow in panel_by_ct.items():
        src_ct = ctuid
        match_type = "exact"
        if src_ct not in geom_by_ct:
            src_ct = SURROGATE.get(ctuid, "")
            if not src_ct or src_ct not in geom_by_ct:
                continue
            match_type = "crosswalk_surrogate"
            surrogate += 1
        else:
            matched += 1

        shp = geom_by_ct[src_ct]
        pts = shp.points
        parts = list(shp.parts) + [len(pts)]
        rings = []
        for i in range(len(parts) - 1):
            ring = pts[parts[i]:parts[i + 1]]
            rings.append([list(tr.transform(x, y)) for x, y in ring])

        geom = {"type": "Polygon", "coordinates": rings} if len(rings) == 1 else {"type": "MultiPolygon", "coordinates": [rings]}

        props = {
            "ct_uid_code": ctuid,
            "geometry_source_ctuid": src_ct,
            "geometry_match_type": match_type,
            "ct_dguid": prow.get("ct_dguid", ""),
            "active_lead_count": f(prow.get("active_lead_count", "0")),
            "replaced_since_2019": f(prow.get("strict_replaced", "0")),
            "replacement_rate": f(prow.get("strict_repl_rate_vs_active_lead", "0")),
            "impacted_people_est": f(prow.get("impacted_people_est", "0")),
            "impacted_children_0_14_est": f(prow.get("impacted_children_0_14_est", "0")),
            "tenure_renter_pct": f(prow.get("tenure_renter_pct", "0")),
            "median_after_tax_income_households": f(prow.get("median_after_tax_income_households", "0")),
            "lim_at_prevalence_pct": f(prow.get("lim_at_prevalence_pct", "0")),
            "unemployment_rate_pct": f(prow.get("unemployment_rate_pct", "0")),
            "children_0_14_pct": f(prow.get("children_0_14_pct", "0")),
            "indigenous_identity_pct": f(prow.get("indigenous_identity_pct", "0")),
            "visible_minority_count": f(prow.get("visible_minority_count", "0")),
            "immigrant_count": f(prow.get("immigrant_count", "0")),
            "lone_parent_family_count": f(prow.get("lone_parent_family_count", "0")),
        }

        features.append({"type": "Feature", "properties": props, "geometry": geom})
        crosswalk_rows.append({"ct_uid_code": ctuid, "geometry_source_ctuid": src_ct, "geometry_match_type": match_type})

    geo = {"type": "FeatureCollection", "features": features}
    OUT_GEOJSON.write_text(json.dumps(geo), encoding="utf-8")

    with OUT_CSV.open("w", encoding="utf-8", newline="") as fobj:
        fields = list(features[0]["properties"].keys())
        w = csv.DictWriter(fobj, fieldnames=fields)
        w.writeheader()
        w.writerows([f["properties"] for f in features])

    with OUT_CROSSWALK.open("w", encoding="utf-8", newline="") as fobj:
        w = csv.DictWriter(fobj, fieldnames=["ct_uid_code", "geometry_source_ctuid", "geometry_match_type"])
        w.writeheader()
        w.writerows(sorted(crosswalk_rows, key=lambda x: x["ct_uid_code"]))

    print({
        "panel_total": len(panel_by_ct),
        "features_written": len(features),
        "exact_matches": matched,
        "surrogate_matches": surrogate,
        "coverage_pct": round(100.0 * len(features) / len(panel_by_ct), 2) if panel_by_ct else 0.0,
        "geojson": str(OUT_GEOJSON.relative_to(ROOT)),
        "crosswalk": str(OUT_CROSSWALK.relative_to(ROOT)),
    })


if __name__ == "__main__":
    main()
