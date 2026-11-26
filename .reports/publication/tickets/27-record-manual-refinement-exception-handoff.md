# Ticket — Record manual refinement exception handoff

## Problem

Deliver the smallest vertical slice for Sub-Spec #9 without expanding beyond its parent requirement.

## Requirements

ADR-060

## Acceptance criteria

- The declared behavior is implemented only through the named seam.
- Automated tests cover the acceptance path and failure path.
- Evidence is archived and linked to the requirement and Sub-Spec.
- No out-of-scope or production claim is introduced.

## Seam

`artifact handoff record`

## Files or modules in scope

docs/adr/; .agents/skills/platform/artifacts/

## Tests and evidence

- handoff schema validation.
- Expected evidence: exception and limitation evidence.

## Non-goals

Unrelated refactors, real institutional integrations, clinical claims and behavior outside Sub-Spec #9.

## Risks

- Risk level: `high`; explain residual risk in the implementation result.
- Preserve rollback and audit behavior for partial failure.

## Blocked by

#25

Hierarchy parent: Sub-Spec #9. Hierarchy is not itself a blocking edge.

## Delivery

One branch `issue/<number>-<slug>` and at most one PR. The PR copies this Ticket's labels and Milestone.

## Traceability

Parent Spec #2 → Sub-Spec #9 → ADR-060.
