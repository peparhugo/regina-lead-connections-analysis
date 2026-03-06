#!/usr/bin/env python3
"""JTB worker: pin practical StatsCan variable IDs and update inventories."""
from __future__ import annotations

import csv
import datetime
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
SRCLOG = ROOT / "reports" / "new-sources-ingested.csv"
CPR = "https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json"
DGUID = "2016S05077050001.01"

patterns = {
    "tenure_total": "Total - Private households by tenure",
    "tenure_owner": "Owner",
    "tenure_renter": "Renter",
    "median_after_tax_income_households": "Median after-tax income of households in 2015",
    "lim_at_prevalence_pct": "Prevalence of low income based on the Low-income measure, after tax",
    "indigenous_identity_total": "Total - Aboriginal identity",
    "indigenous_identity_count": "Aboriginal identity",
    "age_0_14_total": "0 to 14 years",
    "private_dwellings_total": "Total private dwellings",
}


def parse_payload(text: str) -> list[dict]:
    # JSON mode
    try:
        payload = json.loads(text)
        cols = payload.get("COLUMNS", [])
        rows = payload.get("DATA", [])
        idx = {c: i for i, c in enumerate(cols)}
        return [
            {
                "h": r[idx.get("HIER_ID", 0)],
                "txt": r[idx.get("TEXT_NAME_NOM", idx.get("CHARACTERISTIC_NAME", 0))],
            }
            for r in rows
        ]
    except Exception:
        pass

    # XML fallback
    root = ET.fromstring(text)
    cols = [c.attrib.get("NAME", "") for c in root.find("COLUMNNAMES").findall("COLUMN")]
    idx = {c: i for i, c in enumerate(cols)}
    out = []
    for row in root.find("ROWS").findall("ROW"):
        vals = [(c.text or "") for c in row.findall("COLUMN")]
        out.append({"h": vals[idx["HIER_ID"]], "txt": vals[idx["TEXT_NAME_NOM"]]})
    return out


resp = requests.get(CPR, params={"lang": "E", "dguid": DGUID}, timeout=60)
resp.raise_for_status()
rows = parse_payload(resp.text)

pinned = {}
for key, needle in patterns.items():
    for r in rows:
        txt = (r.get("txt") or "").lower()
        if needle.lower() in txt:
            pinned[key] = r.get("h", "")
            break

# write compact pinned csv
out2 = ROOT / "reports" / "statscan_variable_ids_pinned_2026-03-06.csv"
with out2.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["indicator", "hier_id"])
    for k, v in pinned.items():
        w.writerow([k, v])

# append source log
now = datetime.datetime.now().isoformat(timespec="seconds")
SRCLOG.parent.mkdir(parents=True, exist_ok=True)
with SRCLOG.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([now, "statscan_api", f"{CPR}?lang=E&dguid={DGUID}", "Pinned CPR2016 HIER_IDs for equity indicators"])

print({"pinned_count": len(pinned), "out": str(out2.relative_to(ROOT))})
