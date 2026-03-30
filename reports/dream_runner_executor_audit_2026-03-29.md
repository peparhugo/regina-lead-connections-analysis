tags: [regina:canonical, regina:dream, regina:executor-audit, regina:boundary-correction]
created_by: ChaosClaw
created_at: 2026-03-29T16:16:00+02:00

# Dream runner / executor audit — 2026-03-29

Status: canonical audit note
Purpose: verify whether a Dream runner / executor was created, distinguish the thin runner from the richer Dream Monkey execution surface, and explain what Stack C is currently using versus what exists in the repo.

---

## Executive answer

Yes.
A Dream runner / executor **was** created.

But there are **two different execution surfaces** in the repo:

1. a **thin Dream-learn-DMG runner** currently used for bounded question-routing runs;
2. a **richer Dream Monkey / full Dream pipeline executor surface** with packets, branches, triage, bridge handoff, and staged orchestration.

These are not the same thing.

---

## Surface 1 — thin Dream-learn-DMG runner

### File
- `projects/dream-lab/scripts/run_dream_learn_dmg_cycle.py`

### What it does
This runner is real and functional.
It:
- creates a run manifest;
- invokes `dmg_question_generator.py`;
- writes question/suggestion artifacts;
- routes introspective suggestions to `internal_validation_service.py`;
- routes external suggestions to `project_scoped_live_learning.py`;
- runs `dream_run_audit.py` afterward.

### What this means
This is a true runner/executor for:
- question generation
- routed learning execution
- basic audit packaging

### What it is *not*
It is not the full rich Dream Monkey orchestration surface.
It does not itself expose:
- branch competition
- candidate merging
- triage score arbitration
- handoff packet sequencing
- bridge-stage multi-step feedback
- model-backed branch generation
- full simulation/materialization flow

---

## Surface 2 — richer Dream Monkey / full Dream executor surface

### Confirmed artifacts
The repo contains richer Dream execution artifacts and related scripts, including:
- `projects/dream-lab/scripts/dream_monkey_generator.py`
- `projects/dream-lab/scripts/jtb_bridge.py`
- `projects/dream-lab/scripts/jtb_adapter.py`
- `projects/dream-lab/runs/dream_full_v0_actual_20260326/*`
- `projects/dream-lab/runs/dream_full_v0_live_20260326T1529Z/*`
- `projects/dream-lab/bridge_runs/*`

### Full Dream pipeline report evidence
`dream_full_v0_actual_20260326/execution_report.md` explicitly states:
- orchestration is real for persistence, merge, scoring, and packet emission;
- JTB-safe handoff packets are emitted;
- the runner executes a full stage chain;
- but some branch-thinking stages are still fallback-generated rather than model-generated.

### Stage chain confirmed
The full Dream pipeline surface includes stages like:
- goal pack / local context
- dream seed generation
- branch outputs
- merged candidates
- triage scores
- JTB handoff summary
- packet emission
- metrics / state summary

### Honest limitation
The fuller Dream executor exists, but it is still partially symbolic/fallback in branch-generation stages.
So it is richer than the thin runner, but not yet fully model-backed in all stages.

---

## Surface 3 — custom adapter / bridge machinery

There is also experiment-specific adapter machinery, especially in recall-answer-quality work, such as:
- `projects/dream-lab/experiments/recall-answer-quality/build_dmg_mutations_from_battery_v1.py`
- mutation/adapter artifacts under the recall-answer-quality runs

This is important because it shows another layer:
- custom adapters were built to bridge specific experiment forms into Dream/DMG flows.

That means not all useful execution was first-class inside one generic runner.
Some of it was bridged on purpose.

---

## What Stack C has actually been using

Stack C has been executed mostly through the **thin runner / direct route surface**, meaning:
- `run_dream_learn_dmg_cycle.py` style question routing,
- or direct `project_scoped_live_learning.py` runs,
- plus manual patching of route/source/scoring layers.

### What Stack C has *not* really been using yet
Not in a meaningful full way:
- full Dream branch competition
- candidate merge / triage surface
- bridge/handoff packet loop
- richer mutation-family comparison from the broader Dream Monkey surface

So the user intuition was correct:
Stack C has been running through a narrower surface than the fuller Dream executor available in the repo.

---

## Corrected judgment

### Yes, a Dream runner/executor exists.
That was forgotten / under-accounted for.

### But the execution surfaces differ materially.
- The thin runner is real and useful for bounded learning runs.
- The fuller Dream executor is richer, but still partly fallback in branch generation.
- Stack C has mostly been using the thin side, not the richer side.

This is the key reason Stack C can feel underpowered relative to the intended Dream Monkey capability surface.

---

## Operational implication

If Stack C is meant to test the full Dream Monkey + DMG optimization design, then the current execution posture is incomplete.

### Current posture
- enough for thin routed learning runs,
- not enough to claim full rich Dream Monkey execution.

### Next high-value action
Design a Stack C path that explicitly uses more of the fuller Dream executor surface, such as:
- multi-candidate branch outputs,
- triage/merge comparison,
- handoff/bridge packetization,
- mutation-family comparison,
- refinement after branch comparison.

That is the missing step if we want Stack C to feel like true Dream Monkey optimization rather than just patched external learning.
