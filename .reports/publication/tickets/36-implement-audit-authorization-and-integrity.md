# Ticket — Implement audit authorization and integrity

## Problem

Deliver the smallest vertical slice for Sub-Spec #18 without expanding beyond its parent requirement.

## Requirements

AC-06g–AC-06h, ADR-030–ADR-032

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`audit store and scoped query API`

## Files or modules in scope

apps/api/app/; migrations; tests

## Tests and evidence

- tamper and scope tests.
- Expected evidence: append-only integrity report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #18.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#36

Hierarchy parent: Sub-Spec #18. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #5 → Sub-Spec #18 → AC-06g–AC-06h, ADR-030–ADR-032.
