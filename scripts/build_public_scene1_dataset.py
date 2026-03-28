#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
PUBLIC_DATA = ROOT / "public" / "data"
REPORTS = ROOT / "reports"
CACHE_DATA = ROOT / "data" / "cache"
PUBLIC_DATA.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
CACHE_DATA.mkdir(parents=True, exist_ok=True)

AREAS_URL = "https://opengis.regina.ca/arcgis/rest/services/CGISViewer/LeadConnectionAreas/MapServer/0/query"
SCENE_ID = "scene1_observed_area_replacements_2019_2025"
LAYER_ID = "obs_area_replacements_2019_2025"
TIME_START = "2019-01-01"
TIME_END = "2025-12-31"
TIME_START_MONTH = "2019-01"
TIME_END_MONTH = "2025-12"
GEOJSON_OUT = PUBLIC_DATA / f"{SCENE_ID}.geojson"
META_OUT = PUBLIC_DATA / f"{SCENE_ID}.meta.json"
QA_OUT = REPORTS / "regina_public_scene1_join_qa_2026-03-21.json"
AREA_CACHE_OUT = CACHE_DATA / "LeadConnectionAreas.geojson"
FIXED_TIMESTAMP = "2026-03-21T00:00:00Z"
FIXED_SOURCE_DATE = "2026-03-21"


def slugify(value: str) -> str:
    value = value.strip().lower().replace("/", "-")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def fetch_area_geojson() -> tuple[dict, str]:
    params = {
        "where": "1=1",
        "outFields": "NAME,WC_Total,Lead_Total,Lead_Per",
        "f": "geojson",
    }
    try:
        resp = requests.get(AREAS_URL, params=params, timeout=90)
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("type") != "FeatureCollection":
            raise RuntimeError(f"Unexpected area payload type: {payload.get('type')}")
        AREA_CACHE_OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload, "live"
    except Exception:
        if AREA_CACHE_OUT.exists():
            payload = json.loads(AREA_CACHE_OUT.read_text(encoding="utf-8"))
            if payload.get("type") != "FeatureCollection":
                raise RuntimeError("Cached area payload is not a FeatureCollection")
            return payload, "cache"
        raise


def load_monthly_counts(path: Path) -> tuple[dict[str, int], dict]:
    counts = defaultdict(int)
    total_all_rows = total_window_rows = pre_window_rows = post_window_rows = 0
    unknown_month_rows = unknown_area_rows = 0

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            area = (row.get("area") or "").strip()
            month = (row.get("month") or "").strip()
            count = int(row.get("count") or 0)
            total_all_rows += count

            if area == "Unknown":
                unknown_area_rows += count
            if not month:
                unknown_month_rows += count
                continue
            if month < TIME_START_MONTH:
                pre_window_rows += count
                continue
            if month > TIME_END_MONTH:
                post_window_rows += count
                continue
            if area == "Unknown":
                continue

            counts[area] += count
            total_window_rows += count

    summary = {
        "source_file": str(path.relative_to(ROOT)),
        "total_all_rows": total_all_rows,
        "total_window_rows": total_window_rows,
        "pre_window_rows": pre_window_rows,
        "post_window_rows": post_window_rows,
        "unknown_month_rows": unknown_month_rows,
        "unknown_area_rows": unknown_area_rows,
    }
    return dict(counts), summary


def to_float(value):
    if value in (None, ""):
        return None
    return float(value)


def to_int(value):
    if value in (None, ""):
        return None
    return int(round(float(value)))


def main() -> int:
    area_fc, area_source_mode = fetch_area_geojson()
    monthly_counts, monthly_summary = load_monthly_counts(DERIVED / "strict_replacements_by_area_month.csv")

    seen_area_names: set[str] = set()
    duplicate_area_names: list[str] = []
    features_out: list[dict] = []

    for feature in area_fc.get("features", []):
        props = feature.get("properties", {}) or {}
        geom = feature.get("geometry")
        area_name = (props.get("NAME") or "").strip()
        if not area_name:
            continue
        if area_name in seen_area_names:
            duplicate_area_names.append(area_name)
        seen_area_names.add(area_name)

        lead_total = to_int(props.get("Lead_Total"))
        water_total = to_int(props.get("WC_Total"))
        lead_share_pct = to_float(props.get("Lead_Per"))
        observed = int(monthly_counts.get(area_name, 0))
        observed_share = None if lead_total in (None, 0) else observed / lead_total

        out_props = {
            "scene_id": SCENE_ID,
            "layer_id": LAYER_ID,
            "confidence_class": "observed",
            "geography_type": "area",
            "source_version_date": FIXED_SOURCE_DATE,
            "time_window_start": TIME_START,
            "time_window_end": TIME_END,
            "area_name": area_name,
            "area_slug": slugify(area_name),
            "water_connections_total": water_total,
            "lead_connections_total": lead_total,
            "lead_share_pct": lead_share_pct,
            "observed_replacements_2019_2025": observed,
            "observed_replacement_share_of_lead": observed_share,
            "tooltip_title": area_name,
            "tooltip_subtitle": "Observed area replacements, 2019–2025",
            "confidence_note": "Observed area replacements from the area/month source backbone.",
        }
        features_out.append({"type": "Feature", "geometry": geom, "properties": out_props})

    features_out.sort(key=lambda f: f["properties"]["area_name"])
    area_names_out = {f["properties"]["area_name"] for f in features_out}
    unmatched_csv_areas = sorted(set(monthly_counts) - area_names_out)
    duplicate_matches = sorted(set(duplicate_area_names))
    zero_observation_area_names = sorted(name for name in area_names_out if monthly_counts.get(name, 0) == 0)
    public_sum = sum(f["properties"]["observed_replacements_2019_2025"] for f in features_out)

    qa = {
        "generated_at": FIXED_TIMESTAMP,
        "status": "PASS",
        "scene_id": SCENE_ID,
        "area_geometry_source_mode": area_source_mode,
        "feature_count": len(features_out),
        "matched_area_count": len([name for name in monthly_counts if name in area_names_out]),
        "unmatched_area_names": unmatched_csv_areas,
        "duplicate_matches": duplicate_matches,
        "zero_observation_area_names": zero_observation_area_names,
        "sum_observed_replacements_2019_2025": public_sum,
        "monthly_window_summary": monthly_summary,
        "checks": {
            "uses_area_geography_only": True,
            "bounded_to_2019_2025": True,
            "confidence_class_observed_only": True,
            "forbidden_public_fields_present": False,
            "deterministic_feature_sort": True,
        },
    }

    errors: list[str] = []
    if unmatched_csv_areas:
        errors.append(f"unmatched_area_names:{unmatched_csv_areas}")
    if duplicate_matches:
        errors.append(f"duplicate_area_matches:{duplicate_matches}")
    if public_sum != monthly_summary["total_window_rows"]:
        errors.append(f"window_total_mismatch:payload={public_sum}:window={monthly_summary['total_window_rows']}")

    if errors:
        qa["status"] = "BLOCKED"
        qa["errors"] = errors
        QA_OUT.write_text(json.dumps(qa, indent=2), encoding="utf-8")
        print(json.dumps(qa, indent=2))
        return 1

    fc_out = {"type": "FeatureCollection", "features": features_out}
    GEOJSON_OUT.write_text(json.dumps(fc_out, indent=2), encoding="utf-8")

    meta = {
        "scene_id": SCENE_ID,
        "layer_id": LAYER_ID,
        "confidence_class": "observed",
        "time_window": {"start": TIME_START, "end": TIME_END},
        "source_files": [
            "OpenGIS LeadConnectionAreas service",
            "data/cache/LeadConnectionAreas.geojson",
            "data/derived/strict_replacements_by_area_month.csv",
            "data/derived/strict_replacements_by_area.csv",
        ],
        "build_script": str((ROOT / "scripts" / "build_public_scene1_dataset.py").relative_to(ROOT)),
        "generated_at": FIXED_TIMESTAMP,
        "area_geometry_source_mode": area_source_mode,
        "feature_count": len(features_out),
        "sum_observed_replacements_2019_2025": public_sum,
        "join_validation": {
            "matched_area_count": qa["matched_area_count"],
            "unmatched_area_names": unmatched_csv_areas,
            "duplicate_matches": duplicate_matches,
            "zero_observation_area_names": zero_observation_area_names,
        },
        "notes": [
            "Scene 1 is area-native and observed.",
            "This file does not encode tract-level replacement truth.",
            "2026 is intentionally excluded.",
        ],
    }
    META_OUT.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    QA_OUT.write_text(json.dumps(qa, indent=2), encoding="utf-8")
    print(json.dumps({"status": "PASS", "feature_count": len(features_out), "sum": public_sum, "area_geometry_source_mode": area_source_mode}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
