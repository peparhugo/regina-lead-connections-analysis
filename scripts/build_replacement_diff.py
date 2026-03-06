#!/usr/bin/env python3
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://opengis.regina.ca/arcgis/rest/services"
CURRENT = f"{BASE}/CGISViewer/DomesticWaterNetworkTrace/MapServer/4/query"
SNAPSHOT = f"{BASE}/Collector/CBMH_Survey_Map/MapServer/12/query"
AREAS = f"{BASE}/CGISViewer/LeadConnectionAreas/MapServer/0/query"

OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "derived"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def fetch_all(url, out_fields="*", with_geom=False, page=2000):
    """
    Robust ArcGIS fetch using resultOffset paging.
    Avoid returnIdsOnly because some services cap/trim IDs.
    """
    rows = []
    offset = 0
    while True:
        params = {
            "f": "json",
            "where": "1=1",
            "outFields": out_fields,
            "returnGeometry": "true" if with_geom else "false",
            "outSR": 4326,
            "orderByFields": "OBJECTID ASC",
            "resultOffset": offset,
            "resultRecordCount": page,
        }
        j = requests.get(url, params=params, timeout=90).json()
        feats = j.get("features", [])
        if not feats:
            break
        rows.extend(feats)
        offset += len(feats)
        if not j.get("exceededTransferLimit"):
            break
    return rows


def fetch_areas_geojson():
    params = {
        "where": "1=1",
        "outFields": "NAME,WC_Total,Lead_Total,Lead_Per",
        "f": "geojson",
    }
    j = requests.get(AREAS, params=params, timeout=60).json()
    return j.get("features", [])


def line_centroid_xy(geom):
    paths = (geom or {}).get("paths") or []
    if not paths:
        return None
    pts = paths[0]
    if not pts:
        return None
    x = sum(p[0] for p in pts) / len(pts)
    y = sum(p[1] for p in pts) / len(pts)
    return (x, y)


def polygon_bbox(coords):
    xs, ys = [], []
    for ring in coords:
        for x, y in ring:
            xs.append(x)
            ys.append(y)
    return (min(xs), min(ys), max(xs), max(ys))


def point_in_ring(x, y, ring):
    inside = False
    n = len(ring)
    if n < 3:
        return False
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]
        xj, yj = ring[j]
        intersects = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / ((yj - yi) if (yj - yi) else 1e-12) + xi
        )
        if intersects:
            inside = not inside
        j = i
    return inside


def point_in_polygon(x, y, poly_coords):
    if not poly_coords:
        return False
    if not point_in_ring(x, y, poly_coords[0]):
        return False
    for hole in poly_coords[1:]:
        if point_in_ring(x, y, hole):
            return False
    return True


def material_is_lead(v):
    if v is None:
        return False
    s = str(v).strip().lower()
    return s in {"pb", "lead"}


def to_month(v):
    if v in (None, ""):
        return None
    s = str(v)
    try:
        if len(s) == 8 and s.isdigit():
            dt = datetime.strptime(s, "%Y%m%d")
            return dt.strftime("%Y-%m")
        iv = int(float(s))
        if iv > 10_000_000_000:  # epoch ms
            dt = datetime.fromtimestamp(iv / 1000, tz=timezone.utc)
            return dt.strftime("%Y-%m")
    except Exception:
        return None
    return None


def write_summary(rows, key_fields, out_name):
    c = Counter(tuple(r[k] for k in key_fields) for r in rows)
    out_path = OUT_DIR / out_name
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([*key_fields, "count"])
        for key, n in sorted(c.items()):
            w.writerow([*key, n])


def main():
    print("fetch current...")
    cur = fetch_all(CURRENT, out_fields="GISID,MATERIAL,STATUS,UPDATE_DATE,STATUSDATE", with_geom=True)
    print("fetch snapshot...")
    snap = fetch_all(SNAPSHOT, out_fields="GISID,MATERIAL,UPDATE_DATE,STATUSDATE", with_geom=False)
    print("fetch areas...")
    areas = fetch_areas_geojson()

    cur_map = {f["attributes"].get("GISID"): f for f in cur if f.get("attributes", {}).get("GISID")}
    snap_map = {f["attributes"].get("GISID"): f for f in snap if f.get("attributes", {}).get("GISID")}

    area_defs = []
    for a in areas:
        name = a.get("properties", {}).get("NAME")
        coords = (a.get("geometry") or {}).get("coordinates") or []
        if not name or not coords:
            continue
        bbox = polygon_bbox(coords)
        area_defs.append((name, coords, bbox))

    inferred = []
    for gid, c in cur_map.items():
        s = snap_map.get(gid)
        if not s:
            continue
        ca = c.get("attributes", {})
        sa = s.get("attributes", {})
        c_lead = material_is_lead(ca.get("MATERIAL"))
        s_lead = material_is_lead(sa.get("MATERIAL"))

        reason = None
        strict = False
        if s_lead and not c_lead:
            reason = "material_changed_from_lead"
            strict = True
        elif s_lead and c_lead and str(ca.get("UPDATE_DATE")) != str(sa.get("UPDATE_DATE")):
            reason = "lead_with_updated_record"

        if not reason:
            continue

        pt = line_centroid_xy(c.get("geometry"))
        area = "Unknown"
        if pt:
            x, y = pt
            for nm, poly, bb in area_defs:
                minx, miny, maxx, maxy = bb
                if not (minx <= x <= maxx and miny <= y <= maxy):
                    continue
                if point_in_polygon(x, y, poly):
                    area = nm
                    break

        month = to_month(ca.get("UPDATE_DATE")) or to_month(ca.get("STATUSDATE")) or "Unknown"
        inferred.append({
            "GISID": gid,
            "area": area,
            "reason": reason,
            "is_strict_replacement": "Y" if strict else "N",
            "current_material": ca.get("MATERIAL"),
            "snapshot_material": sa.get("MATERIAL"),
            "update_date": ca.get("UPDATE_DATE"),
            "status_date": ca.get("STATUSDATE"),
            "month": month,
        })

    detail_path = OUT_DIR / "inferred_replacements_detailed.csv"
    with detail_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "GISID", "area", "reason", "is_strict_replacement", "current_material", "snapshot_material", "update_date", "status_date", "month"
        ])
        w.writeheader()
        w.writerows(inferred)

    # Broad (legacy-compatible): includes both reasons
    write_summary(inferred, ["area", "month"], "inferred_replacements_by_area_month.csv")
    write_summary(inferred, ["area"], "inferred_replacements_by_area.csv")

    # Strict: only true material changes from lead
    strict_rows = [r for r in inferred if r["is_strict_replacement"] == "Y"]
    write_summary(strict_rows, ["area", "month"], "strict_replacements_by_area_month.csv")
    write_summary(strict_rows, ["area"], "strict_replacements_by_area.csv")

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "current_count": len(cur_map),
        "snapshot_count": len(snap_map),
        "common_gisid_count": len(set(cur_map).intersection(snap_map)),
        "inferred_count_broad": len(inferred),
        "inferred_count_strict": len(strict_rows),
        "reason_counts": {
            "material_changed_from_lead": sum(1 for r in inferred if r["reason"] == "material_changed_from_lead"),
            "lead_with_updated_record": sum(1 for r in inferred if r["reason"] == "lead_with_updated_record"),
        },
        "notes": [
            "Broad inferred set includes lead_with_updated_record for legacy continuity.",
            "Strict inferred set includes only snapshot lead -> current non-lead material changes.",
            "This is inferred analytics, not an official city replacement-event ledger.",
        ],
    }
    (OUT_DIR / "inferred_replacements_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
