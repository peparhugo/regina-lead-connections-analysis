#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path('/root/.openclaw/workspace')
REPO = WORKSPACE / 'projects' / 'regina-lead-github-pages'
DREAM_RUNS = WORKSPACE / 'projects' / 'dream-lab' / 'runs'
REPO_KNOWLEDGE = WORKSPACE / 'repo_knowledge' / 'regina-lead-connections-analysis'
RESEARCH = WORKSPACE / 'research'
UO = WORKSPACE / 'universal_objects' / 'store'
REPORTS = REPO / 'reports'


def sh(cmd: list[str], cwd: Path | None = None) -> str:
    return subprocess.check_output(cmd, cwd=str(cwd) if cwd else None, text=True)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def repo_status() -> dict:
    porcelain = sh(['git', '-C', str(REPO), 'status', '--porcelain'])
    modified = []
    untracked = []
    for line in porcelain.splitlines():
        status = line[:2]
        path = line[3:]
        if status == '??':
            untracked.append(path)
        else:
            modified.append({'status': status, 'path': path})
    return {
        'branch': sh(['git', '-C', str(REPO), 'branch', '--show-current']).strip(),
        'head': sh(['git', '-C', str(REPO), 'rev-parse', 'HEAD']).strip(),
        'recent_commits': sh(['git', '-C', str(REPO), 'log', '--oneline', '-n', '8']).splitlines(),
        'modified_count': len(modified),
        'untracked_count': len(untracked),
        'modified_sample': modified[:40],
        'untracked_sample': untracked[:120],
    }


def list_paths(base: Path, pattern: str = '*', max_items: int = 200) -> list[str]:
    if not base.exists():
        return []
    return [str(p) for p in sorted(base.glob(pattern))[:max_items]]


def regina_dream_runs() -> list[str]:
    if not DREAM_RUNS.exists():
        return []
    paths = sorted([p for p in DREAM_RUNS.iterdir() if p.is_dir() and 'regina' in p.name.lower()])
    return [str(p) for p in paths[-60:]]


def research_surface() -> dict:
    out = {}
    for name in ['regina-budget', 'regina-burden', 'regina-master', 'regina-politics', 'regina-senior-gov']:
        base = RESEARCH / name
        out[name] = {
            'exists': base.exists(),
            'ledger_files': [str(p) for p in sorted((base / 'ledger').glob('*'))] if (base / 'ledger').exists() else [],
            'note_files': [str(p) for p in sorted((base / 'notes').glob('*'))[:20]] if (base / 'notes').exists() else [],
        }
    return out


def repo_knowledge_surface() -> dict:
    history = REPO_KNOWLEDGE / 'history'
    payload = {
        'exists': REPO_KNOWLEDGE.exists(),
        'top_files': [str(p) for p in sorted(REPO_KNOWLEDGE.glob('*')) if p.is_file()],
        'history_files': [str(p) for p in sorted(history.glob('*')) if p.is_file()] if history.exists() else [],
    }
    for name in ['repo_history_profile.json', 'repo_history_manifest.json']:
        p = history / name
        if p.exists():
            try:
                payload[name] = json.loads(p.read_text())
            except Exception:
                payload[name] = {'_error': 'parse_failed'}
    return payload


def universal_object_surface() -> dict:
    targets = {}
    for folder in ['beliefs', 'claims', 'decisions', 'lookup_traces', 'memory_update_proposals', 'tasks', 'behavior_packets', 'context_packets', 'draft_skills', 'hypotheses']:
        base = UO / folder
        if not base.exists():
            continue
        hits = sorted([p for p in base.glob('*regina*')])
        if hits:
            targets[folder] = [str(p) for p in hits[:40]]
    return targets


def main() -> None:
    snapshot = {
        'snapshot_version': 'regina_control_snapshot.v1',
        'captured_at': now_iso(),
        'repo': repo_status(),
        'dream_runs': regina_dream_runs(),
        'research_surface': research_surface(),
        'repo_knowledge_surface': repo_knowledge_surface(),
        'universal_object_surface': universal_object_surface(),
    }
    out_json = REPORTS / 'regina_full_surface_control_snapshot_2026-03-28.json'
    out_md = REPORTS / 'regina_full_surface_control_snapshot_2026-03-28.md'
    out_json.write_text(json.dumps(snapshot, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# Regina full-surface control snapshot — 2026-03-28',
        '',
        f"Captured at: {snapshot['captured_at']}",
        '',
        '## Repo state',
        f"- branch: {snapshot['repo']['branch']}",
        f"- head: {snapshot['repo']['head']}",
        f"- modified_count: {snapshot['repo']['modified_count']}",
        f"- untracked_count: {snapshot['repo']['untracked_count']}",
        '',
        '### Recent commits',
    ]
    lines.extend([f'- {row}' for row in snapshot['repo']['recent_commits']])
    lines.extend(['', '## Repo dirty-state sample', '### Modified sample'])
    lines.extend([f"- {row['status']} {row['path']}" for row in snapshot['repo']['modified_sample'][:25]])
    lines.extend(['', '### Untracked sample'])
    lines.extend([f'- {row}' for row in snapshot['repo']['untracked_sample'][:40]])
    lines.extend(['', '## Dream / DMG Regina run surface'])
    lines.append(f"- run_dir_count_listed: {len(snapshot['dream_runs'])}")
    lines.extend([f'- {row}' for row in snapshot['dream_runs'][:25]])
    lines.extend(['', '## Research surface'])
    for name, data in snapshot['research_surface'].items():
        lines.append(f'- {name}: exists={data["exists"]} ledger_files={len(data["ledger_files"])} note_files={len(data["note_files"])}')
    lines.extend(['', '## Repo knowledge / history surface'])
    rk = snapshot['repo_knowledge_surface']
    lines.append(f"- exists: {rk['exists']}")
    profile = rk.get('repo_history_profile.json', {})
    lines.append(f"- history pull_request_count: {profile.get('pull_request_count')}")
    lines.append(f"- history merged_pr_count: {profile.get('merged_pr_count')}")
    lines.append(f"- history open_pr_count: {profile.get('open_pr_count')}")
    lines.append(f"- history contributor_count: {profile.get('contributor_count')}")
    lines.extend(['', '## Universal object / external state surface'])
    for folder, hits in snapshot['universal_object_surface'].items():
        lines.append(f'- {folder}: {len(hits)} relevant artifact(s)')
    lines.extend(['', '## Blunt operator reading'])
    lines.append('- Regina project state is broader than repo state.')
    lines.append('- Material work currently exists across the repo dirty tree, research ledgers, Dream runs, repo_knowledge history artifacts, and universal object/KG-style stores.')
    lines.append('- GitHub/PR tracking is now live, but it still represents only a subset of total Regina work unless this wider surface is tracked repeatedly.')
    out_md.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'ok': True, 'json': str(out_json), 'markdown': str(out_md)}, indent=2))


if __name__ == '__main__':
    main()
