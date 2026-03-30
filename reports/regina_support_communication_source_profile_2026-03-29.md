tags: [regina:canonical, regina:support-communication, regina:source-profile, regina:dream]
created_by: ChaosClaw
created_at: 2026-03-29T16:03:00+02:00

# Regina support-communication source profile — 2026-03-29

Status: canonical route/profile note
Purpose: define the dedicated external source profile for support-communication comparison work so this question family no longer rides generic technical or overly broad public-web retrieval paths.

---

## Executive decision

Support-communication comparison requires its own source profile.

It should not be treated as a generic benchmark/comparison query, and it should not inherit the Regina technical/entity-resolution retrieval profile.

---

## Intended use

This profile is for questions about:
- uncertainty communication
- risk communication
- public-health communication guidance
- technical appendix vs headline claim discipline
- bounded/modelled estimate communication
- scenario-envelope communication
- pseudo-precision avoidance
- public-interest evidence framing

---

## Preferred source classes

### Tier 1 — institutional/public-health guidance
- `who.int`
- `cdc.gov`
- `canada.ca`
- `gov.uk`
- `nih.gov`

### Tier 2 — medical/public-health literature surfaces
- `pubmed.ncbi.nlm.nih.gov`
- `pmc.ncbi.nlm.nih.gov`
- selected public-health / medical journal hosts

### Tier 3 — policy / guidance / academic communication sources
- reputable `.gov`
- reputable `.edu`
- selected `.org` with clear communication/guidance relevance

---

## Preferred query families

### Family A — uncertainty communication guidance
Examples:
- communicating uncertainty public health guidance
- risk communication uncertainty guidance public health
- communication of modeled estimates public guidance

### Family B — appendix vs summary/public communication
Examples:
- technical appendix executive summary communication guidance
- appendix vs headline claim communication
- reporting modeled estimates for public audiences

### Family C — scenario / bounded-estimate communication
Examples:
- scenario communication public health guidance
- bounded estimate communication framework
- communicating uncertain risk ranges to the public

---

## Reject / suppress classes

Suppress results dominated by:
- entity resolution
- record linkage
- geospatial matching
- technical benchmarking
- municipal graph workflows
- random unrelated `.gov` pages with incidental appendix language
- generic communication pages without uncertainty/risk/evidence framing relevance

---

## Acceptance rule

A source should only survive if it materially helps one of these:
- separating appendix from headline/public claim language
- communicating uncertainty or bounded estimates responsibly
- preventing pseudo-precision
- preserving public usefulness under uncertainty
- explaining evidence/risk communication principles applicable to Regina support work

---

## Operational implication

This source profile should be treated as a dedicated route-profile for Stack C-style work, not just as another benchmark/comparison variant.
