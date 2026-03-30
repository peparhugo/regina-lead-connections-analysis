tags: [regina:canonical, regina:dream, regina:dmg, regina:experiment-review]
created_by: ChaosClaw
created_at: 2026-03-29T08:25:00+02:00

# Regina Wave A Dream/DMG experiment review — 2026-03-29

Status: canonical experiment review
Purpose: summarize the first 12-question Wave A experiment, identify winning routes, diagnose failed routes, and define the most sensible next moves.

---

## Executive result

Wave A produced a clear answer quickly.

### Winning lane family
- `focused / validation_or_contradiction`
- `focused / operator_decision_support`

### Losing lane family in this run
- `focused / benchmark_or_comparison`
- `focused / failure_diagnosis`

### Important correction
The losing external lanes did **not** fail because they were conceptually bad.
They failed because the external live-learning runner booted incorrectly in this execution path:
- `ModuleNotFoundError: No module named 'services'`

So Wave A proves:
- the internal lanes are immediately productive;
- the external lanes are still pending fair evaluation because the runner path was broken.

---

## Wave A execution summary

Run id:
- `regina_waveA_dmg_experiment_20260329`

Question structure:
- 4 lanes
- 3 questions per lane
- 12 total questions

Execution summary:
- total runs: 12
- successful runs: 6
- failed runs: 6

Lane-level outcome:
- validation_or_contradiction: 3/3 success, 24 accepted findings total
- operator_decision_support: 3/3 success, 24 accepted findings total
- benchmark_or_comparison: 0/3 success (runner failure)
- failure_diagnosis: 0/3 success (runner failure)

---

## What the winning internal lanes tell us

### 1. The rebuilt control plane is good at internal contradiction review
The validation lane consistently produced accepted findings from internal artifacts.
That means the recovery/control work was worth it: the system can now reason over current Regina materials in a structured way.

### 2. Operator-decision routing is also immediately useful
The operator_decision_support lane also produced strong accepted-findings counts.
That suggests the next-best-step problem is now more about selective use of the current artifact base than about rebuilding basics.

### 3. The current highest-yield path is still internal-first
For the immediate post-recovery period, the system is strongest when it:
- interrogates current internal artifacts,
- preserves artifact ordering,
- and turns contradiction pressure into explicit operator decisions.

---

## Internal-lane substantive takeaway

The strongest emerging conclusion from the successful runs remains consistent with the support-layer contradiction review:
- support-layer burden artifacts are generally preservable,
- but they need explicit support-only boundaries,
- and they should not silently widen canonical/public truth.

So the successful Wave A runs reinforce the current lane policy rather than overturning it.

---

## Why the external lanes failed

### Actual failure class
Infrastructure/bootstrap failure, not evidence failure.

Observed error:
- `ModuleNotFoundError: No module named 'services'`

### Meaning
The `project_scoped_live_learning.py` path was invoked without the import environment it expects.
Because of that:
- no external tasks were actually executed;
- no live-learning result artifacts were created;
- and the benchmark/failure-diagnosis lanes did not get a fair trial.

### What this invalidates
It invalidates any claim like:
- “external benchmark routes are weak for Regina”
- or “failure_diagnosis is low-yield”

We do **not** know that yet.
We only know the external runner bootstrap was wrong.

---

## Correct next moves

### Next move 1 — use the winning internal findings now
Proceed with the current internal-first strength:
- keep contradiction review active;
- use operator-decision outputs to choose the next immediate support/control refinements;
- preserve support-layer boundaries in retrieval and project truth.

### Next move 2 — repair the external runner path
Before judging the external lanes, rerun them under the correct environment (for example with the right `PYTHONPATH` or canonical runner invocation).

### Next move 3 — run a fair external Wave A retry
Retry only the failed external half of Wave A:
- benchmark_or_comparison (3)
- failure_diagnosis (3)

That produces a fair route comparison without re-running the already successful internal half.

---

## Best current operator judgment

Wave A already answered one important question:
- the rebuilt Regina control plane is capable of useful internal contradiction and decision learning.

It has **not yet** answered the external-route quality question, because the external runner path failed before execution.

So the right interpretation is:
- internal lanes = validated winners
- external lanes = not yet evaluated fairly

---

## Recommendation

Do not abandon the external lanes.
Repair the runner path and rerun only the 6 failed external questions.
That is the cleanest next experiment step.
