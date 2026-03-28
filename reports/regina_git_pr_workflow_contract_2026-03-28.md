# Regina git / PR workflow contract — 2026-03-28

Status: active workflow discipline contract
Purpose: make Regina implementation auditable through branches, PRs, reviews, and merge checkpoints.

## Core rule
Regina changes should no longer live only in chat memory or direct commits to `main` when the change is material.

Material changes should go through:
1. branch
2. PR
3. review gate selection
4. merge checkpoint
5. artifact-linked summary

## Branch naming rule
Required format:
- `regina/<lane>/<short-slug>`

Allowed lane values:
- `control`
- `governance`
- `methods`
- `journalism`
- `graph`
- `property-tax`
- `automation`
- `delivery`

Examples:
- `regina/control/dream-runner-auditization`
- `regina/governance/pr-gate-discipline`
- `regina/automation/repo-history-refresh`

## What must use a PR
Use a PR for any change that:
- changes control/governance files
- changes public wording or claim envelope
- changes Dream/DMG or repo-history automation
- changes methods or evidence classification logic
- changes generated public/support reports that influence operator decisions

## What may skip a PR
Small local-only housekeeping may skip PRs if it does not affect control truth, claim envelope, or automation behavior.

Examples:
- temporary scratch notes
- non-authoritative formatting cleanup
- local exploratory artifacts that are explicitly disposable

## Review gate mapping
### provenance review
Use when:
- source references changed
- canonical or support artifacts were re-ranked
- new artifact links are introduced

### method review
Use when:
- analytic assumptions change
- model/matching logic changes
- burden/method framing changes

### reproducibility review
Use when:
- scripts/pipelines/automation changed
- Dream/DMG / repo-history behavior changed
- outputs should be replayable

### contradiction review
Use when:
- current-state / claim ceiling might have shifted
- a change may conflict with canonical-control artifacts

### claim-envelope review
Use when:
- wording, promotion level, or support-only/canonical boundaries are touched

### wording/legal caution review
Use when:
- public/journalist-facing text changes
- accusations, liability, or accountability wording shifts

### merge-owner signoff
Always required for material Regina PRs.

## Merge checkpoint requirement
Every material Regina PR should leave behind one of:
- updated existing control report
- new short status note in `reports/`
- clearly linked run/audit artifact bundle

The goal is that a later operator can answer:
- what changed
- why it changed
- what gate it touched
- what evidence or automation artifacts support it

## Current implementation note
The repo-history ingest now correctly records zero-PR truth when no PRs exist.
That means workflow discipline must be adopted in practice if we want the GitHub audit lane to become meaningfully informative.
