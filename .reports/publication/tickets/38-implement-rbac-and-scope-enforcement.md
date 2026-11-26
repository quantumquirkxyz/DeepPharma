# Ticket — Implement RBAC and scope enforcement

## Problem

Deliver the smallest vertical slice for Sub-Spec #20 without expanding beyond its parent requirement.

## Requirements

AC-06f, AC-06h, AC-08, ADR-006, ADR-020

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`authorization dependency`

## Files or modules in scope

apps/api/app/auth.py; tests

## Tests and evidence

- RBAC and scope tests.
- Expected evidence: deny-by-default evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #20.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#25, #36

Hierarchy parent: Sub-Spec #20. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #6 → Sub-Spec #20 → AC-06f, AC-06h, AC-08, ADR-006, ADR-020.
