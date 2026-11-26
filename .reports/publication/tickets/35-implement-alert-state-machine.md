# Ticket — Implement alert state machine

## Problem

Deliver the smallest vertical slice for Sub-Spec #17 without expanding beyond its parent requirement.

## Requirements

AC-07–AC-10, ADR-018

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`alert transition service`

## Files or modules in scope

apps/api/app/risk.py; tests

## Tests and evidence

- transition table and authorization tests.
- Expected evidence: terminal-state evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #17.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#30

Hierarchy parent: Sub-Spec #17. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #5 → Sub-Spec #17 → AC-07–AC-10, ADR-018.
