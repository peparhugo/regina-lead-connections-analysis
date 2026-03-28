#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports' / 'data_provenance_ledger_2026-03-06.csv'

# Canonical source map for current pipeline artifacts.
SOURCE_MAP = {
    'data/derived/statscan_ct_equity_vars_2016_regina.csv': {
        'source_url': 'https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json',
        'query_params': 'lang=E; dguid=<CT dguid>; CT filter prefix 2016S0507705',
        'upstream_dataset': 'StatsCan CPR2016 + CR2016Geo',
    },
    'data/derived/statscan_da_equity_vars_2016_regina.csv': {
        'source_url': 'https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json',
        'query_params': 'lang=E; dguid=<DA dguid>; DA GEO_ID prefix 4706',
        'upstream_dataset': 'StatsCan CPR2016 + CR2016Geo',
    },
    'data/derived/ct_equity_panel_official_2026-03-06_regina.csv': {
        'source_url': 'local transform',
        'query_params': 'build_official_ct_equity_panel.py',
        'upstream_dataset': 'statscan_ct_equity_vars_2016_regina.csv + area_priority_signals.csv',
    },
    'data/derived/equity_significance_results_official_ct_2026-03-06_regina.csv': {
        'source_url': 'local transform',
        'query_params': 'build_official_ct_equity_panel.py',
        'upstream_dataset': 'ct_equity_panel_official_2026-03-06_regina.csv',
    },
    'data/derived/ct_da_equity_panel_2026-03-06.csv': {
        'source_url': 'https://opengis.regina.ca/arcgis/rest/services/CGISViewer/Neighbourhood_Profile/MapServer/0/query',
        'query_params': 'f=json; where=1=1; outFields=CA,PDF_Link',
        'upstream_dataset': 'area_priority_signals.csv + strict_replacements_by_area_month.csv + Neighbourhood_Profile',
    },
    'data/derived/equity_significance_results_2026-03-06.csv': {
        'source_url': 'local transform',
        'query_params': 'build_equity_panel_and_tests.py',
        'upstream_dataset': 'ct_da_equity_panel_2026-03-06.csv',
    },
    'reports/evidence_tier_ab_search_2026-03-06.csv': {
        'source_url': 'http://127.0.0.1:8888',
        'query_params': 'SearXNG meta-search queries in scripts/evidence_search_tier_ab.py',
        'upstream_dataset': 'SearXNG engines composite',
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    rows = []
    now = datetime.now(timezone.utc).isoformat()

    for rel, meta in SOURCE_MAP.items():
        p = ROOT / rel
        rows.append({
            'captured_at': now,
            'artifact_path': rel,
            'exists': p.exists(),
            'size_bytes': p.stat().st_size if p.exists() else 0,
            'sha256': sha256_file(p) if p.exists() else '',
            'source_url': meta['source_url'],
            'query_params': meta['query_params'],
            'upstream_dataset': meta['upstream_dataset'],
            'access_date_utc': now,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print({'rows': len(rows), 'out': str(OUT.relative_to(ROOT))})


if __name__ == '__main__':
    main()
