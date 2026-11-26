# Ticket — Implement migration rollback and kill switch

## Problem

Deliver the smallest vertical slice for Sub-Spec #22 without expanding beyond its parent requirement.

## Requirements

AC-06i, ADR-007, ADR-014, ADR-035

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`operational control plane`

## Files or modules in scope

apps/api/migrations/; docs/operations/; tests

## Tests and evidence

- isolated migration and rollback tests.
- Expected evidence: restore and kill-switch evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #22.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#25

Hierarchy parent: Sub-Spec #22. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #6 → Sub-Spec #22 → AC-06i, ADR-007, ADR-014, ADR-035.
