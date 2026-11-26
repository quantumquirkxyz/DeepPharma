# Ticket — Implement versioned risk evaluation contract

## Problem

Deliver the smallest vertical slice for Sub-Spec #13 without expanding beyond its parent requirement.

## Requirements

AC-05–AC-06, ADR-003

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`RiskEvaluator`

## Files or modules in scope

apps/api/app/risk.py; tests

## Tests and evidence

- risk integration tests.
- Expected evidence: version and limitation evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #13.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#30

Hierarchy parent: Sub-Spec #13. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #4 → Sub-Spec #13 → AC-05–AC-06, ADR-003.
