# Ticket — Implement inventory state and coverage

## Problem

Deliver the smallest vertical slice for Sub-Spec #12 without expanding beyond its parent requirement.

## Requirements

ADR-057, ADR-059

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`coverage calculator and inventory domain`

## Files or modules in scope

apps/api/app/; tests

## Tests and evidence

- domain and API tests.
- Expected evidence: coverage indeterminate evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #12.

## Risks

- Risk level: `medium`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#29

Hierarchy parent: Sub-Spec #12. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #3 → Sub-Spec #12 → ADR-057, ADR-059.
