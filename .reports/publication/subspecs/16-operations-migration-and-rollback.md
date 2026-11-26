# Sub-Spec — Operations Migration and Rollback

## Problem

This slice provides a bounded, reviewable part of the M4 — Seguridad, operación y verificación Parent Spec.

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

- Parent Spec #6.
- Native parent-child relation is required; hierarchy alone does not imply execution blocking.

## Validation

- `uv run pytest` for API behavior where applicable.
- Targeted tests and artifact validation named by downstream Tickets.
- `git diff --check`.

## Traceability

AC-06i, ADR-007, ADR-014, ADR-035

## Blocked by

Parent Spec #6 must remain `status:ready` or higher. Additional blockers require a real execution prerequisite.
