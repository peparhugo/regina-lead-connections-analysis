tags: [regina:canonical, regina:dream, regina:dmg, regina:external-retry-review]
created_by: ChaosClaw
created_at: 2026-03-29T08:31:00+02:00

# Regina Wave A external retry review — 2026-03-29

Status: canonical retry review
Purpose: review the retried external half of Wave A after fixing the runner bootstrap, separate genuine route quality from question/query mismatch, and define the next patch.

---

## Executive result

The external retry clarified the situation substantially.

### What changed
The external lanes now execute correctly after the bootstrap fix.
So external-lane outcomes are now meaningful.

### Main result
- `failure_diagnosis` is a real winner
- `benchmark_or_comparison` remains weak-to-mixed in its current question/query form

### Why benchmark_or_comparison underperformed
Not because the lane is inherently bad.
It underperformed because the current Regina external query construction still inherits technical/entity-resolution vocabulary that does not fit support-layer communication questions.

---

## Retry outcomes observed so far

### benchmark_or_comparison
- run 1: 0 accepted / 4 rejected
- run 2: 1 accepted / 3 rejected
- run 3: 1 accepted / 3 rejected

#### Interpretation
Weak-to-mixed.
The route can produce something, but the retrieval target is misaligned with the actual question class.

### failure_diagnosis
- run 1: 3 accepted / 0 rejected
- run 2: 1 accepted / 2 rejected
- run 3: still running or pending at the time of this review

#### Interpretation
Strong.
This lane is now clearly useful for Regina because the question class aligns better with the currently inherited retrieval vocabulary around retrieval, ranking, reranking, and debugging.

---

## Core diagnosis

### benchmark_or_comparison mismatch
The benchmark/comparison questions were about:
- public-interest framing
- technical appendix vs headline claims
- scenario-envelope handling
- public-health burden communication
- pseudo-precision prevention

But the generated external queries remained dominated by:
- entity resolution
- record linkage
- geospatial matching
- precision/recall
- knowledge graph / municipal data implementation terms

That is the wrong topical anchor for this question family.

### failure_diagnosis fit
The failure_diagnosis questions were about:
- retrieval/ranking failure modes
- promoted governance claims vs generic residue
- diagnostic levers for query/ranking quality

Those questions actually fit the currently inherited Regina technical retrieval vocabulary.
That is why this lane started producing accepted findings once the runner worked.

---

## What this means for next steps

### Keep and likely expand
- `focused / failure_diagnosis`

This lane is producing useful external signal now and should be treated as a validated route.

### Patch before rerunning broadly
- `focused / benchmark_or_comparison`

This lane needs support/communication-specific topical anchoring before it gets a fair comparison.

---

## Required patch

For support-layer communication / framing questions, the external lane generator should prefer scope terms like:
- public-health communication
- uncertainty communication
- risk communication
- scenario envelope
- bounded estimate
- technical appendix
- headline claim
- burden communication
- pseudo-precision
- evidence communication
- public-interest reporting

And it should suppress, for this question class:
- entity resolution
- record linkage
- geospatial matching
- municipal graph workflows
- address matching
- parcel linkage
- precision/recall benchmark language unrelated to communication framing

---

## Updated operator judgment

The external half of Wave A is no longer “failed.”
It is now split into:

### validated external route
- failure_diagnosis

### not yet fairly tuned route
- benchmark_or_comparison for support/communication questions

That is a good experiment outcome because it tells us exactly what to patch next.

---

## Recommended immediate next move

Patch the Regina DMG question generator so that support/communication benchmark questions use support/communication-specific scope terms rather than inherited technical Regina implementation terms.
Then rerun only the benchmark/comparison trio.
