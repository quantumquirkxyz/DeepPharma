# Ticket — Implement data protection and retention controls

## Problem

Deliver the smallest vertical slice for Sub-Spec #21 without expanding beyond its parent requirement.

## Requirements

ADR-008, ADR-021, ADR-032–ADR-034

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`restricted dataset repository`

## Files or modules in scope

apps/api/app/; migrations; docs/; tests

## Tests and evidence

- security and retention test plan.
- Expected evidence: retention and incident evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #21.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#25

Hierarchy parent: Sub-Spec #21. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #6 → Sub-Spec #21 → ADR-008, ADR-021, ADR-032–ADR-034.
