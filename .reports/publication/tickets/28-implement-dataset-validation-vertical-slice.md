# Ticket — Implement dataset validation vertical slice

## Problem

Deliver the smallest vertical slice for Sub-Spec #10 without expanding beyond its parent requirement.

## Requirements

AC-01–AC-02, ADR-002

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`DatasetValidator`

## Files or modules in scope

apps/api/app/datasets.py; apps/api/tests/

## Tests and evidence

- uv run pytest targeted dataset tests.
- Expected evidence: row-level validation evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #10.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

None

Hierarchy parent: Sub-Spec #10. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #3 → Sub-Spec #10 → AC-01–AC-02, ADR-002.
