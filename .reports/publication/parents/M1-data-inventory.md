# Parent Spec — M1 Data and Inventory

## Context

The MVP must validate inventory datasets before applying them and expose a
consistent inventory state without silent mutation.

## Scope

- Dataset schema/type/reference/duplicate validation.
- Immutable dataset intake and provenance.
- Safe application of valid inventory data.
- Inventory and coverage calculation using ADR-057.

## Acceptance criteria

- Invalid datasets report row-level errors and do not alter current inventory.
- Valid datasets preserve source, version, state and record count.
- Inventory uniqueness and non-negative stock are enforced.
- Coverage uses the 30-day valid-consumption formula and returns
  `INDETERMINATE` when no valid denominator exists.

## Non-goals

Real institutional data, real SALMI integration, clinical decisions and
production capacity claims.

## Risks

- Invalid data could mutate operational inventory if transaction boundaries
  are wrong.
- Coverage is indeterminate when valid consumption is unavailable.

## Dependencies

- M0 Parent Spec (#2) and approved domain formula ADR-057.

## Validation

- `uv run pytest apps/api/tests/test_health.py`.
- Integration tests for valid, invalid, duplicate and rollback paths.
- Migration validation on an isolated SQLite database.

## Traceability

`US-01`, `AC-01–AC-04`, `ADR-002`, `ADR-057`.

## Blocked by

M0 Parent Spec (#2) reaching `status:ready`.

## Child Sub-Specs

Dataset validation, safe import, inventory state, and coverage calculation.

## Source

`docs/spec/mvp-inventory-risk.md` US-01, ADR-002, ADR-057 and
`docs/requirements/acceptance-traceability-mvp.md`.
