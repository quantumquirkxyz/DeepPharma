# Ticket — Implement deterministic fallback lineage

## Problem

Deliver the smallest vertical slice for Sub-Spec #15 without expanding beyond its parent requirement.

## Requirements

AC-06b–AC-06c, ADR-024–ADR-025

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`risk lineage adapter`

## Files or modules in scope

apps/api/app/; migrations; tests

## Tests and evidence

- fallback failure and lineage tests.
- Expected evidence: traceId and new-result evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #15.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#30

Hierarchy parent: Sub-Spec #15. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #4 → Sub-Spec #15 → AC-06b–AC-06c, ADR-024–ADR-025.
