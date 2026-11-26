# Ticket — Implement safe dataset application

## Problem

Deliver the smallest vertical slice for Sub-Spec #11 without expanding beyond its parent requirement.

## Requirements

AC-03–AC-04, ADR-002

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`InventoryImportService`

## Files or modules in scope

apps/api/app/; migrations; tests

## Tests and evidence

- rollback and valid-apply integration tests.
- Expected evidence: transaction and provenance report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #11.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#28

Hierarchy parent: Sub-Spec #11. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #3 → Sub-Spec #11 → AC-03–AC-04, ADR-002.
