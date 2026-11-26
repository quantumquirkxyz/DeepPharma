# Ticket — Implement simulated notifications and retry

## Problem

Deliver the smallest vertical slice for Sub-Spec #19 without expanding beyond its parent requirement.

## Requirements

AC-14, ADR-019

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`notification adapter`

## Files or modules in scope

apps/api/app/; tests

## Tests and evidence

- failure and retry integration tests.
- Expected evidence: idempotent retry evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #19.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#36, #37

Hierarchy parent: Sub-Spec #19. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #5 → Sub-Spec #19 → AC-14, ADR-019.
