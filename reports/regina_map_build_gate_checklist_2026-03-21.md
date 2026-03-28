# Regina Map Build Gate Checklist — 2026-03-21

Purpose: define the acceptance gates for the bounded Regina map MVP build.

This checklist is written for the approved hybrid architecture and keeps the public MVP anchored to **Scene 1 only** unless a later approval explicitly widens scope.

---

## Gate vocabulary
- `PASS`
- `PASS_WITH_LIMITS`
- `BLOCKED`

---

## G5-A — Public Scene 1 contract ready

### Pass conditions
- `regina_public_scene1_data_contract_2026-03-21.md` is implemented in code/build form.
- A generated public Scene 1 payload exists.
- Payload uses area geography only.
- Payload is bounded to 2019–2025 only.
- Payload self-identifies as `observed`.

### Block triggers
- CT or proxy fields leak into Scene 1 payload.
- 2026 appears in public Scene 1 output.
- join mismatches remain unresolved.

---

## G5-B — Public app shell ready

### Pass conditions
- A MapLibre + deck.gl app shell exists under a clear public app directory.
- App loads Scene 1 successfully from generated data assets.
- Legend, tooltip, and side panel all show the `observed` framing.
- No unsupported toggles are present.

### Block triggers
- app defaults to CT estimated context
- unsupported layers become selectable
- public copy implies tract-level direct replacement truth

---

## G5-C — Confidence guardrails preserved

### Pass conditions
- UI uses the exact confidence taxonomy where relevant:
  - `observed`
  - `inferred`
  - `estimated`
  - `unsupported`
- Scene 1 foregrounds `observed` only.
- tooltip copy matches the approved observed wording materially.
- side-panel copy states that Scene 1 is the strongest direct replacement map surface currently approved.

### Block triggers
- any confidence-neutral wording such as “confirmed replacements” at CT level
- legend styling that makes estimated context look canonical
- public UI flattening observed and estimated into one story state

---

## G5-D — Analyst package baseline ready

### Pass conditions
- A versioned Kepler analyst package exists with manifest, config, and datasets.
- Observed, inferred, and CT estimated inputs remain separate.
- Default analyst view starts with observed area data.
- CT package notes preserve allocation caveats.

### Block triggers
- package lacks versioning
- package merges confidence classes into one dataset without clear flags
- package includes GTLO/My Maps as a validation layer

---

## G5-E — Git / PR discipline ready

### Pass conditions
- implementation is split into PR-sized units
- each PR has a stated scope, output files, and validation method
- data-contract changes, app-shell changes, and analyst-package changes are not all mixed together
- reports reference the PR split and acceptance logic

### Block triggers
- one mega-PR for data, app, and analyst work
- no artifact-to-PR traceability
- scene expansion introduced before Scene 1 passes

---

## Recommended PR sequence

### PR1 — Data contract + generated assets + QA
Scope:
- add public build scripts / generated data outputs for Scene 1
- generate `scene1_observed_area_replacements_2019_2025.*`
- add join/time-window QA output

Validation:
- row/feature counts
- 2019–2025 total check
- no CT/proxy fields

### PR2 — Public app shell (MapLibre + deck.gl)
Scope:
- create public app directory and bootstrap
- render Scene 1 layer, legend, tooltip, side panel
- keep Scene 1 as the only shipped view in MVP

Validation:
- app loads on GitHub Pages / static preview
- default behavior matches observed-only rules
- no unsupported layers

### PR3 — Analyst package baseline
Scope:
- create versioned Kepler package structure
- package observed, inferred, and CT estimated datasets separately
- add manifest and field dictionary

Validation:
- package opens cleanly in Kepler
- default visibility starts with observed area dataset
- notes preserve caveats

### PR4 — Hardening / docs / release checklist
Scope:
- docs, README updates, screenshots, operator notes
- release QA checklist
- only after PR1–PR3 pass

Validation:
- docs align with actual output paths and limits
- release notes repeat 2019–2025 and observed-first posture

---

## MVP definition (strict)

The Regina map MVP is done only when all five of these are true:
1. public map opens on observed area replacements for 2019–2025 only;
2. data pipeline produces a deterministic Scene 1 payload from approved source files;
3. legend/tooltips/panel preserve confidence wording and do not overclaim;
4. analyst Kepler package exists as a versioned separate surface;
5. CT estimated context, 2026, and unsupported layers remain deferred from the public default release.

---

## Deferred beyond MVP

Explicit deferrals:
- Public Scene 2 CT estimated context
- Public Scene 3 methods / explainer experience beyond the minimum panel needed for Scene 1
- 2026 provisional display
- impacted-children overlays
- DA/proxy layers
- unsupported/blocked diagnostic layers in public UI
- automation for merge-trigger rebuilds

---

## Drift trigger

Report `DRIFT_RISK` immediately if any of the following appear during implementation:
- pressure to add CT estimates into the MVP default view
- pressure to expose 2026 in public controls
- pressure to use GTLO/My Maps as validation or UI evidence
- pressure to add unsupported layers because the map feels too sparse
- pressure to widen claim wording beyond observed area program progress
