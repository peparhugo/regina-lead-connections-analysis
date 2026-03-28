#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'data' / 'derived' / 'npv_policy_summary_2026-03-06.csv'
ANCH = ROOT / 'reports' / 'cad_cost_anchor_assumptions_v4_2026-03-06.csv'
OUT = ROOT / 'data' / 'derived' / 'npv_policy_summary_cad_v4_2026-03-06.csv'
OUT_MD = ROOT / 'reports' / 'npv_policy_summary_cad_v4_2026-03-06.md'


def f(v, d=0.0):
    try:
        return float(v)
    except Exception:
        return d


def main():
    idx = [r for r in csv.DictReader(INDEX.open()) if r.get('endpoint') != 'COMBINED']
    anchors = {r['endpoint']: r for r in csv.DictReader(ANCH.open())}

    rows = []
    combined = {'best': 0.0, 'base': 0.0, 'worst': 0.0}

    for r in idx:
        ep = r['endpoint']
        band = r['band']
        a = anchors.get(ep)
        if not a:
            continue
        band_col = {'best': 'band_low', 'base': 'band_base', 'worst': 'band_high'}[band]
        a_val = f(a[band_col])
        npv_idx = f(r['npv_index'])
        npv_cad = npv_idx * a_val
        rows.append({
            'endpoint': ep,
            'band': band,
            'discount_rate': r['discount_rate'],
            'years': r['years'],
            'npv_index': r['npv_index'],
            'annual_cost_anchor_cad_per_1000_exposed': a_val,
            'npv_cad_per_1000_exposed': f'{npv_cad:.2f}',
            'anchor_source': a['source'],
            'anchor_notes': a['notes'],
        })
        combined[band] += npv_cad

    for b in ['best', 'base', 'worst']:
        rows.append({
            'endpoint': 'COMBINED',
            'band': b,
            'discount_rate': '',
            'years': '30',
            'npv_index': '',
            'annual_cost_anchor_cad_per_1000_exposed': '',
            'npv_cad_per_1000_exposed': f"{combined[b]:.2f}",
            'anchor_source': 'aggregate',
            'anchor_notes': 'Sum of endpoint CAD NPVs (caution band)',
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', newline='', encoding='utf-8') as fobj:
        w = csv.DictWriter(fobj, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    def val(ep, b):
        return next(f(x['npv_cad_per_1000_exposed']) for x in rows if x['endpoint'] == ep and x['band'] == b)

    md = [
        '# CAD-Calibrated NPV Policy Summary (per 1,000 exposed)',
        '',
        'This pass converts index NPVs to CAD using explicit anchor assumptions.',
        'Use for directional policy prioritization only until endpoint anchors are validated with CIHI/provincial micro-costing.',
        '',
        '## Combined caution band (CAD NPV per 1,000 exposed; 30 years)',
        f"- Best: `${combined['best']:,.0f}`",
        f"- Base: `${combined['base']:,.0f}`",
        f"- Worst: `${combined['worst']:,.0f}`",
        '',
        '## Endpoint breakdown (CAD NPV per 1,000 exposed)',
        '| Endpoint | Best | Base | Worst |',
        '|---|---:|---:|---:|',
        f"| IQ | ${val('IQ','best'):,.0f} | ${val('IQ','base'):,.0f} | ${val('IQ','worst'):,.0f} |",
        f"| ADHD | ${val('ADHD','best'):,.0f} | ${val('ADHD','base'):,.0f} | ${val('ADHD','worst'):,.0f} |",
        f"| CVD | ${val('CVD','best'):,.0f} | ${val('CVD','base'):,.0f} | ${val('CVD','worst'):,.0f} |",
        f"| CKD | ${val('CKD','best'):,.0f} | ${val('CKD','base'):,.0f} | ${val('CKD','worst'):,.0f} |",
        '',
        '## Guardrails',
        '- Anchors are explicit assumptions and should be replaced with CIHI/provincial validated cost lines as they become available.',
        '- Keep endpoint-level uncertainty separate in downstream decisions.',
    ]
    OUT_MD.write_text('\n'.join(md) + '\n', encoding='utf-8')
    print({'ok': True, 'out_csv': str(OUT.relative_to(ROOT)), 'out_md': str(OUT_MD.relative_to(ROOT))})


if __name__ == '__main__':
    main()
