# Ticket — Implement canonical tracker metadata validator

## Problem

Deliver the smallest vertical slice for Sub-Spec #8 without expanding beyond its parent requirement.

## Requirements

ADR-036–ADR-046, ADR-051

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`label/readiness validator`

## Files or modules in scope

docs/reference/agents/; .reports/checkpoints/

## Tests and evidence

- metadata fixture validation.
- Expected evidence: label and readiness report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #8.

## Risks

- Risk level: `medium`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#25

Hierarchy parent: Sub-Spec #8. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #2 → Sub-Spec #8 → ADR-036–ADR-046, ADR-051.
