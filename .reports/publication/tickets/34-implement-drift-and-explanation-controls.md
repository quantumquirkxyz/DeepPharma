# Ticket — Implement drift and explanation controls

## Problem

Deliver the smallest vertical slice for Sub-Spec #16 without expanding beyond its parent requirement.

## Requirements

AC-06d–AC-06e, ADR-026, ADR-028

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`monitoring and explanation ports`

## Files or modules in scope

apps/api/app/; docs/; tests

## Tests and evidence

- drift fixture and explanation tests.
- Expected evidence: reference comparison report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #16.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#32, #33

Hierarchy parent: Sub-Spec #16. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #4 → Sub-Spec #16 → AC-06d–AC-06e, ADR-026, ADR-028.
