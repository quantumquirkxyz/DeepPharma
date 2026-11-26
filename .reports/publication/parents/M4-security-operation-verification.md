# Parent Spec — M4 Security, Operations and Verification

## Context

The MVP requires explicit security boundaries, reproducible operations and
evidence-based verification before it can be treated as an engineering slice.

## Scope

- RBAC and authorization boundaries.
- Migration, retention, incident and rollback controls.
- Observability and benchmark evidence.
- Final traceability and release verification.

## Acceptance criteria

- Protected endpoints enforce role and scope.
- Migration and rollback procedures are reproducible and evidenced.
- Restricted data, retention and incident controls have executable tests or
  explicit deferred tickets.
- Quality evidence distinguishes local evaluation from production assurance.

## Non-goals

Production certification, legal compliance claims, institutional deployment and
unverified availability guarantees.

## Risks

- Missing scope checks or retention controls could expose restricted data.
- Local benchmark evidence cannot establish production SLOs.

## Dependencies

- M0 governance (#2), M1 data (#3), M2 risk (#4) and M3 alerts (#5).

## Validation

- `uv run pytest`.
- Isolated Alembic upgrade.
- HTTP benchmark with recorded environment, volume, percentiles and limits.
- Security, rollback and traceability verification.

## Traceability

`AC-06f–AC-06i`, `AC-08–AC-14`, `ADR-006–ADR-008`,
`ADR-013–ADR-014`, `ADR-020–ADR-021`, `ADR-030–ADR-035`.

## Blocked by

M0–M3 Parent Specs (#2–#5) reaching `status:ready`.

## Child Sub-Specs

Authorization, data protection, operations, observability and final
verification.

## Source

`docs/spec/plan-mvp-inventory-risk.md`, `docs/quality/evidence-register.md`,
ADR-006–ADR-008, ADR-013–ADR-014, ADR-020–ADR-021 and ADR-030–ADR-035.
