#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / 'data' / 'derived'
OUT = ROOT / 'reports' / 'qa_validation_report_2026-03-06.json'


def read_csv(path: Path):
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def check_not_empty(path: Path, issues: list):
    if not path.exists() or path.stat().st_size == 0:
        issues.append(f'missing_or_empty:{path.name}')
        return []
    rows = read_csv(path)
    if not rows:
        issues.append(f'no_rows:{path.name}')
    return rows


def check_required_columns(rows: list, required: list, label: str, issues: list):
    if not rows:
        return
    cols = set(rows[0].keys())
    for c in required:
        if c not in cols:
            issues.append(f'missing_col:{label}:{c}')


def check_null_rate(rows: list, col: str, label: str, max_null_rate: float, issues: list):
    if not rows:
        return
    vals = [r.get(col, '') for r in rows]
    nulls = sum(1 for v in vals if v in ('', None))
    rate = nulls / len(vals)
    if rate > max_null_rate:
        issues.append(f'high_null_rate:{label}:{col}:{rate:.3f}')


def main():
    issues = []

    ct = check_not_empty(DER / 'statscan_ct_equity_vars_2016_regina.csv', issues)
    da = check_not_empty(DER / 'statscan_da_equity_vars_2016_regina.csv', issues)
    panel = check_not_empty(DER / 'ct_equity_panel_official_2026-03-06_regina.csv', issues)
    tests = check_not_empty(DER / 'equity_significance_results_official_ct_2026-03-06_regina.csv', issues)

    check_required_columns(ct, ['geo_uid', 'geo_id_code', 'tenure_renter_pct', 'median_after_tax_income_households'], 'ct_vars', issues)
    check_required_columns(da, ['geo_uid', 'geo_id_code', 'tenure_renter_pct', 'median_after_tax_income_households'], 'da_vars', issues)
    check_required_columns(panel, ['ct_dguid', 'strict_replaced', 'active_lead_count', 'tenure_renter_pct'], 'ct_panel', issues)
    check_required_columns(tests, ['test_id', 'estimate', 'interpretation'], 'tests', issues)

    check_null_rate(panel, 'ct_dguid', 'ct_panel', 0.0, issues)
    check_null_rate(panel, 'strict_replaced', 'ct_panel', 0.0, issues)
    check_null_rate(panel, 'tenure_renter_pct', 'ct_panel', 0.2, issues)

    # Key constraints
    if panel:
        dg = [r.get('ct_dguid', '') for r in panel]
        if len(dg) != len(set(dg)):
            issues.append('duplicate_key:ct_panel:ct_dguid')

    report = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'status': 'PASS' if not issues else 'WARN',
        'issue_count': len(issues),
        'issues': issues,
        'counts': {
            'ct_rows': len(ct),
            'da_rows': len(da),
            'panel_rows': len(panel),
            'tests_rows': len(tests),
        },
    }

    OUT.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(report)


if __name__ == '__main__':
    main()
