# Parent Spec — M2 Risk ML and Fallback

## Context

Risk evaluation must be reproducible and auditable while keeping a deterministic
fallback available when an ML model is unavailable.

## Scope

- Versioned risk evaluation seam.
- Deterministic `baseline-rules-1` fallback.
- Temporal evaluation and leakage controls.
- Result lineage, limitations and controlled monitoring.

## Acceptance criteria

- Risk results identify model or fallback version, horizon, source and trace.
- Fallback activation records cause and degradation state.
- Re-evaluation does not duplicate active alerts.
- ML claims remain operational and are not presented as clinical truth.

## Non-goals

Clinical prediction, unauthorised institutional data, automatic clinical or
irreversible replenishment actions.

## Risks

- Synthetic/public data cannot establish institutional or clinical validity.
- Model drift or unavailable models must fail safe and remain auditable.

## Dependencies

- M0 governance (#2) and M1 inventory/data (#3).

## Validation

- Reproducible experiment tests with fixed seed and dataset digest.
- Temporal split and leakage-control tests.
- Fallback and lineage integration tests.

## Traceability

`US-02`, `AC-05–AC-07`, `ADR-003`, `ADR-009`, `ADR-017`,
`ADR-024–ADR-029`.

## Blocked by

M0 Parent Spec (#2) and M1 Parent Spec (#3) reaching `status:ready`.

## Child Sub-Specs

Risk evaluator, reproducible experiment runner, fallback, lineage and
monitoring.

## Source

`docs/spec/mvp-inventory-risk.md` US-02, ADR-003, ADR-009, ADR-017,
ADR-024–ADR-029.
