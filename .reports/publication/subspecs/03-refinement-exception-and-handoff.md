# Sub-Spec — Refinement Exception and Handoff

## Problem

This slice provides a bounded, reviewable part of the M0 — Baseline y gobierno Parent Spec.

## Goals

- Define atomic requirements and observable acceptance criteria.
- Identify the seam, tests and evidence required before readiness.

## Non-goals

Production certification, clinical validity and integrations outside the Parent Spec.

## Acceptance criteria

- Requirements are traceable to the Parent Spec and named criteria.
- The behavior has an explicit seam, test oracle and evidence expectation.
- Unexecuted behavior remains marked and cannot be claimed complete.

## Risks

- High risk requires review evidence before implementation.
- Partial existing coverage must not be mistaken for full completion.

## Dependencies

- Parent Spec #2.
- Native parent-child relation is required; hierarchy alone does not imply execution blocking.

## Validation

- `uv run pytest` for API behavior where applicable.
- Targeted tests and artifact validation named by downstream Tickets.
- `git diff --check`.

## Traceability

ADR-060, refinement-reconciliation-20261126.md

## Blocked by

Parent Spec #2 must remain `status:ready` or higher. Additional blockers require a real execution prerequisite.
