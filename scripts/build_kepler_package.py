#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
PUBLIC_DATA = ROOT / "public" / "data"
PACKAGE_ROOT = ROOT / "analyst" / "kepler" / "2026-03-21"
DATASETS = PACKAGE_ROOT / "datasets"
DATASETS.mkdir(parents=True, exist_ok=True)

AREAS_URL = "https://opengis.regina.ca/arcgis/rest/services/CGISViewer/LeadConnectionAreas/MapServer/0/query"


def slugify(value: str) -> str:
    value = value.strip().lower().replace("/", "-")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def fetch_area_geojson() -> dict:
    params = {"where": "1=1", "outFields": "NAME,WC_Total,Lead_Total,Lead_Per", "f": "geojson"}
    resp = requests.get(AREAS_URL, params=params, timeout=90)
    resp.raise_for_status()
    return resp.json()


def load_csv_map(path: Path, key_field: str, value_field: str) -> dict[str, int]:
    out = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row.get(key_field) or "").strip()
            if not key or key == "Unknown":
                continue
            out[key] = int(row.get(value_field) or 0)
    return out


def build_inferred_area_dataset() -> tuple[int, list[str]]:
    inferred_counts = load_csv_map(DERIVED / "inferred_replacements_by_area.csv", "area", "count")
    meta = json.loads((DERIVED / "inferred_replacements_meta.json").read_text(encoding="utf-8"))
    areas = fetch_area_geojson()
    out_features = []
    unmatched = sorted(set(inferred_counts) - {f.get("properties", {}).get("NAME", "").strip() for f in areas.get("features", [])})

    for feature in areas.get("features", []):
        props = feature.get("properties", {}) or {}
        area_name = (props.get("NAME") or "").strip()
        if not area_name:
            continue
        out_props = {
            "dataset_id": "area_inferred_broad",
            "area_name": area_name,
            "area_slug": slugify(area_name),
            "lead_connections_total": int(round(float(props.get("Lead_Total") or 0))),
            "water_connections_total": int(round(float(props.get("WC_Total") or 0))),
            "lead_share_pct": float(props.get("Lead_Per") or 0),
            "inferred_replacements_broad": int(inferred_counts.get(area_name, 0)),
            "confidence_class": "inferred",
            "method_note": "Inferred continuity layer from record-comparison logic; not a direct replacement-event ledger.",
            "meta_generated_at": meta.get("generated_at"),
        }
        out_features.append({"type": "Feature", "geometry": feature.get("geometry"), "properties": out_props})

    out = {"type": "FeatureCollection", "features": out_features}
    (DATASETS / "area_inferred_broad.geojson").write_text(json.dumps(out, indent=2), encoding="utf-8")
    return len(out_features), unmatched


def build_ct_estimated_dataset() -> int:
    src = json.loads((DERIVED / "ct_factor_diagnostics_kepler_2026-03-06.geojson").read_text(encoding="utf-8"))
    for feature in src.get("features", []):
        props = feature.setdefault("properties", {})
        props["confidence_class"] = "estimated"
        props["notes"] = "Estimated tract allocation derived from observed area-level source data; not direct observed tract replacement counts."
        props["dataset_id"] = "ct_estimated_context"
    (DATASETS / "ct_estimated_context.geojson").write_text(json.dumps(src, indent=2), encoding="utf-8")
    return len(src.get("features", []))


def copy_observed_dataset() -> int:
    src = PUBLIC_DATA / "scene1_observed_area_replacements_2019_2025.geojson"
    dst = DATASETS / "area_observed_2019_2025.geojson"
    shutil.copy2(src, dst)
    fc = json.loads(dst.read_text(encoding="utf-8"))
    return len(fc.get("features", []))


def main() -> int:
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    observed_n = copy_observed_dataset()
    inferred_n, unmatched = build_inferred_area_dataset()
    ct_n = build_ct_estimated_dataset()

    manifest = {
        "package_name": "regina-kepler-analyst-package",
        "package_version": "2026-03-21",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "kepler_config_file": "kepler_config.json",
        "datasets": [
            {"id": "area_observed_2019_2025", "path": "datasets/area_observed_2019_2025.geojson", "confidence_class": "observed", "feature_count": observed_n},
            {"id": "area_inferred_broad", "path": "datasets/area_inferred_broad.geojson", "confidence_class": "inferred", "feature_count": inferred_n},
            {"id": "ct_estimated_context", "path": "datasets/ct_estimated_context.geojson", "confidence_class": "estimated", "feature_count": ct_n},
        ],
        "source_files": [
            "public/data/scene1_observed_area_replacements_2019_2025.geojson",
            "data/derived/inferred_replacements_by_area.csv",
            "data/derived/inferred_replacements_meta.json",
            "data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson",
            "reports/kepler_config_phase_a_2026-03-06.json",
        ],
        "confidence_taxonomy": ["observed", "inferred", "estimated", "unsupported"],
        "restrictions": [
            "Not a public approval artifact by itself",
            "2026 promoted counts are excluded",
            "GTLO/My Maps excluded as validation backbone",
            "Unsupported layers not included in this package version"
        ],
        "warnings": [
            "Analyst package contains support-only and estimated layers.",
            "CT estimated context is allocation-based, not direct tract replacement truth.",
            "Use observed area data as the default first view."
        ],
        "join_notes": {"unmatched_inferred_area_names": unmatched}
    }
    (PACKAGE_ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps({"status": "PASS", "observed": observed_n, "inferred": inferred_n, "ct": ct_n, "unmatched": unmatched}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
