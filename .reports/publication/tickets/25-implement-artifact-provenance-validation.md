# Ticket — Implement artifact provenance validation

## Problem

Deliver the smallest vertical slice for Sub-Spec #7 without expanding beyond its parent requirement.

## Requirements

AC-01–AC-14

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`artifact validation seam`

## Files or modules in scope

.agents/skills/platform/artifacts/; docs/requirements/

## Tests and evidence

- python3 -m json.tool; digest comparison.
- Expected evidence: validated artifact report.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #7.

## Risks

- Risk level: `medium`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

None

Hierarchy parent: Sub-Spec #7. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #2 → Sub-Spec #7 → AC-01–AC-14.
