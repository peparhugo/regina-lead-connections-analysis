#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
OUT = REPORTS / 'evidence_tier_ab_search_2026-03-06.csv'

QUERIES = [
    'childhood lead exposure meta-analysis IQ cohort study',
    'blood lead levels children longitudinal cohort cognitive outcomes',
    'lead exposure cardiovascular disease adulthood cohort',
    'lead exposure kidney disease cohort study',
]


def run_search(query: str):
    cmd = [
        'python3',
        '/root/.openclaw/workspace/skills/searxng-search/scripts/searxng_search.py',
        '--url', 'http://127.0.0.1:8888',
        '--query', query,
        '--count', '8',
    ]
    p = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(p.stdout)


def classify_tier(title: str, snippet: str) -> str:
    t = (title + ' ' + snippet).lower()
    if 'meta-analysis' in t or 'systematic review' in t or 'pooled analysis' in t:
        return 'A'
    if 'cohort' in t or 'longitudinal' in t or 'prospective' in t:
        return 'B'
    return 'C+'


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    rows = []
    ts = datetime.now(timezone.utc).isoformat()

    for q in QUERIES:
        data = run_search(q)
        for r in data.get('results', []):
            title = r.get('title', '')
            snippet = r.get('snippet', '')
            rows.append({
                'captured_at': ts,
                'query': q,
                'title': title,
                'url': r.get('url', ''),
                'engine': r.get('engine', ''),
                'published_date': r.get('publishedDate', ''),
                'tier_guess': classify_tier(title, snippet),
                'snippet': snippet,
            })

    # de-dupe on URL
    seen = set()
    uniq = []
    for r in rows:
        u = r['url']
        if not u or u in seen:
            continue
        seen.add(u)
        uniq.append(r)

    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(uniq[0].keys()) if uniq else [
            'captured_at', 'query', 'title', 'url', 'engine', 'published_date', 'tier_guess', 'snippet'
        ])
        w.writeheader()
        w.writerows(uniq)

    print({'rows': len(uniq), 'out': str(OUT.relative_to(ROOT))})


if __name__ == '__main__':
    main()
