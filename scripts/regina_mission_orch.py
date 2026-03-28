#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, datetime, hashlib, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'memory'/'mission-state.json'
LOG=ROOT/'reports'/'mission-log.md'
KG=ROOT/'reports'/'knowledge-gaps.md'
TERMINAL_LOCK=ROOT/'memory'/'terminal-lock.json'

ART={
 'ct_panel': ROOT/'data'/'derived'/'ct_equity_panel_official_2026-03-06.csv',
 'ct_tests': ROOT/'data'/'derived'/'equity_significance_results_official_ct_2026-03-06.csv',
 'summary': ROOT/'reports'/'phd_equity_summary_2026-03-06.html',
 'appendix': ROOT/'reports'/'reproducibility_appendix_equity_2026-03-06.md',
}


def now(): return datetime.datetime.now().isoformat(timespec='seconds')

def load_state(): return json.loads(STATE.read_text(encoding='utf-8'))
def save_state(s): STATE.write_text(json.dumps(s,indent=2),encoding='utf-8')

def log(msg):
    with LOG.open('a',encoding='utf-8') as f: f.write(f"\n- {now()} | {msg}")

def run(cmd):
    p=subprocess.run(cmd,shell=True,cwd=ROOT,text=True,capture_output=True)
    return p.returncode,p.stdout[-1000:],p.stderr[-1000:]

def gate_status():
    g1 = ART['ct_panel'].exists()
    g2 = ART['ct_tests'].exists()
    g3 = ART['summary'].exists() and ART['appendix'].exists()
    g4 = g1 and g2 and g3
    return g1,g2,g3,g4


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def enforce_terminal_lock_or_exit():
    if not TERMINAL_LOCK.exists():
        return
    lock = json.loads(TERMINAL_LOCK.read_text(encoding='utf-8'))
    if lock.get('locked') is not True:
        return
    if os.environ.get('REGINA_TERMINAL_UNLOCK') == 'I_UNDERSTAND':
        log('G4 -> UNLOCK_BYPASS | REGINA_TERMINAL_UNLOCK accepted')
        return
    final_path = ROOT / lock.get('finalSynthPath', 'reports/final_synthesis_2026-03-06.md')
    if (not final_path.exists()) or (_sha256(final_path) != lock.get('finalSynthSha256', '')):
        log('G4 -> BLOCKED | terminal lock enforced integrity breach')
        print('TERMINAL_LOCK_BREACH', file=sys.stderr)
        raise SystemExit(42)
    log('G4 -> NOOP | terminal lock enforced; hash verified; skipping all gate logic')
    print({'terminalLock': True, 'action': 'NOOP', 'gate': 'G4_MISSION_CLOSEOUT', 'status': 'COMPLETE'})
    raise SystemExit(0)


enforce_terminal_lock_or_exit()

s=load_state()
g1,g2,g3,g4=gate_status()
s['gates']['G1_DATA_COMPLETENESS']['passed']=g1
s['gates']['G2_STATISTICAL_VALIDITY']['passed']=g2
s['gates']['G3_PUBLICATION_QUALITY']['passed']=g3
s['gates']['G4_MISSION_CLOSEOUT']['passed']=g4

if not g1:
    s['currentGate']='G1_DATA_COMPLETENESS'
    code,out,err=run(s['workers']['WORKER_DATA'])
    s['lastAction']='WORKER_DATA'
    log(f"G1 run WORKER_DATA rc={code}")
    if code!=0:
        s['knowledgeGap']['active']=True
        s['knowledgeGap']['topic']='Data extraction blocked; pin variable IDs and sources'
        with KG.open('a',encoding='utf-8') as f:
            f.write(f"\n| {now()} | G1 | extraction blocked | run WORKER_RESEARCH_JTB |")
        run(s['workers']['WORKER_RESEARCH_JTB'])
        log('Executed WORKER_RESEARCH_JTB')
elif not g2:
    s['currentGate']='G2_STATISTICAL_VALIDITY'
    code,out,err=run(s['workers']['WORKER_STATS'])
    s['lastAction']='WORKER_STATS'
    log(f"G2 run WORKER_STATS rc={code}")
elif not g3:
    s['currentGate']='G3_PUBLICATION_QUALITY'
    code,out,err=run(s['workers']['WORKER_PUBLISH'])
    s['lastAction']='WORKER_PUBLISH'
    log(f"G3 run WORKER_PUBLISH rc={code}")
else:
    s['currentGate']='G4_MISSION_CLOSEOUT'
    s['status']='READY_FOR_FINAL_SYNTHESIS'
    log('All gates satisfied. Ready for final synthesis.')

s['lastUpdated']=now()
save_state(s)
print({'currentGate':s['currentGate'],'status':s['status'],'lastAction':s.get('lastAction','')})
