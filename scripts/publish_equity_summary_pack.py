#!/usr/bin/env python3
from pathlib import Path
import datetime

ROOT=Path(__file__).resolve().parents[1]
summary=ROOT/'reports'/'phd_equity_summary_2026-03-06.html'
append=f"""
\n<!-- AUTONOMOUS_MISSION_UPDATE {datetime.datetime.now().isoformat(timespec='seconds')} -->
<section class=\"card\">\n<h2>Autonomous mission update</h2>\n<ul>\n<li>Mission orchestrator active with gates G1-G4.</li>\n<li>Official CT/DA StatsCan pull lane enabled (CT first, DA batched).</li>\n<li>Knowledge-gap fallback lane (JTB) enabled for variable pinning and source ingestion.</li>\n</ul>\n</section>\n"""
if summary.exists():
    t=summary.read_text(encoding='utf-8')
    if 'AUTONOMOUS_MISSION_UPDATE' not in t:
        t=t.replace('</main>', append+'\n</main>')
        summary.write_text(t,encoding='utf-8')
print({'updated':str(summary.relative_to(ROOT))})
