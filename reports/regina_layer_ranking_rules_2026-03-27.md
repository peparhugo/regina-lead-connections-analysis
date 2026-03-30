tags: [regina:canonical, regina:ranking, regina:control]
created_by: ChaosClaw
created_at: 2026-03-27T15:43:40+01:00

Regina knowledge-layer and retrieval-ranking rules

- layer model: canonical control docs (tag: regina:canonical) are authoritative for state/status queries and must be ranked above repo-memory/non-canonical artifacts
- query-time rules:
  - if intent matches: {"current state", "status", "project completeness", "is X part of core"} → boost documents with tag regina:canonical by weight +3 and suppress documents tagged regina:non-canonical by -2
  - otherwise: normal ranking applies
- indexing note: place these documents under memory/ or canonical/ and ensure they are included in the first-pass index and given high embedding priority

Verification: run smoke probes for the three canonical questions and confirm top-1/top-3 sources contain regina:canonical docs.
