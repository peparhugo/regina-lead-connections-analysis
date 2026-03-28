#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEOJSON = ROOT / "public" / "data" / "scene1_observed_area_replacements_2019_2025.geojson"
META = ROOT / "public" / "data" / "scene1_observed_area_replacements_2019_2025.meta.json"
JOIN_QA = ROOT / "reports" / "regina_public_scene1_join_qa_2026-03-21.json"
OUT = ROOT / "reports" / "regina_public_scene1_dataset_qa_2026-03-21.json"

REQUIRED_PROPS = {
    "scene_id",
    "layer_id",
    "confidence_class",
    "geography_type",
    "source_version_date",
    "time_window_start",
    "time_window_end",
    "area_name",
    "area_slug",
    "water_connections_total",
    "lead_connections_total",
    "lead_share_pct",
    "observed_replacements_2019_2025",
    "observed_replacement_share_of_lead",
    "tooltip_title",
    "tooltip_subtitle",
    "confidence_note",
}
FORBIDDEN_PROPS = {
    "ct_uid_code",
    "ct_dguid",
    "impacted_people_est",
    "impacted_children_0_14_est",
    "inferred_replacements_broad",
    "replaced_since_2026",
    "da_uid",
}


def fail(report: dict, reason: str) -> int:
    report["status"] = "BLOCKED"
    report.setdefault("issues", []).append(reason)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 1


def main() -> int:
    report = {"status": "PASS", "issues": []}

    for path in [GEOJSON, META, JOIN_QA]:
        if not path.exists():
            return fail(report, f"missing_required_file:{path.relative_to(ROOT)}")

    fc = json.loads(GEOJSON.read_text(encoding="utf-8"))
    meta = json.loads(META.read_text(encoding="utf-8"))
    join_qa = json.loads(JOIN_QA.read_text(encoding="utf-8"))

    if fc.get("type") != "FeatureCollection":
        return fail(report, "invalid_geojson_type")

    features = fc.get("features", [])
    if not features:
        return fail(report, "no_features")

    total = 0
    for idx, feature in enumerate(features):
        geom = feature.get("geometry")
        if not geom or geom.get("type") not in {"Polygon", "MultiPolygon"}:
            return fail(report, f"invalid_geometry:{idx}")

        props = feature.get("properties", {}) or {}
        missing = sorted(REQUIRED_PROPS - set(props))
        if missing:
            return fail(report, f"missing_props:{idx}:{missing}")

        forbidden = sorted(FORBIDDEN_PROPS & set(props))
        if forbidden:
            return fail(report, f"forbidden_props:{idx}:{forbidden}")

        if props.get("scene_id") != "scene1_observed_area_replacements_2019_2025":
            return fail(report, f"bad_scene_id:{idx}")
        if props.get("layer_id") != "obs_area_replacements_2019_2025":
            return fail(report, f"bad_layer_id:{idx}")
        if props.get("confidence_class") != "observed":
            return fail(report, f"bad_confidence_class:{idx}")
        if props.get("geography_type") != "area":
            return fail(report, f"bad_geography_type:{idx}")
        if props.get("time_window_start") != "2019-01-01" or props.get("time_window_end") != "2025-12-31":
            return fail(report, f"bad_time_window:{idx}")
        total += int(props.get("observed_replacements_2019_2025") or 0)

    if meta.get("confidence_class") != "observed":
        return fail(report, "meta_bad_confidence_class")
    if meta.get("sum_observed_replacements_2019_2025") != total:
        return fail(report, f"meta_total_mismatch:{meta.get('sum_observed_replacements_2019_2025')}:{total}")
    if join_qa.get("status") != "PASS":
        return fail(report, f"join_qa_not_pass:{join_qa.get('status')}")
    if join_qa.get("sum_observed_replacements_2019_2025") != total:
        return fail(report, f"join_qa_total_mismatch:{join_qa.get('sum_observed_replacements_2019_2025')}:{total}")

    report.update({
        "feature_count": len(features),
        "sum_observed_replacements_2019_2025": total,
        "meta_path": str(META.relative_to(ROOT)),
        "geojson_path": str(GEOJSON.relative_to(ROOT)),
        "join_qa_path": str(JOIN_QA.relative_to(ROOT)),
    })
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
