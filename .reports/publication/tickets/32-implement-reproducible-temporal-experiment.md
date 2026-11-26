# Ticket — Implement reproducible temporal experiment

## Problem

Deliver the smallest vertical slice for Sub-Spec #14 without expanding beyond its parent requirement.

## Requirements

AC-06a, ADR-017, ADR-027

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`ExperimentRunner and TemporalEvaluator`

## Files or modules in scope

experiments/; tests; docs/quality/

## Tests and evidence

- reproducible experiment suite.
- Expected evidence: dataset digest and metrics report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #14.

## Risks

- Risk level: `critical`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#31

Hierarchy parent: Sub-Spec #14. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #4 → Sub-Spec #14 → AC-06a, ADR-017, ADR-027.
