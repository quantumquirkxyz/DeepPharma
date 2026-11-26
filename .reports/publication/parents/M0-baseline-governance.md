# Parent Spec — M0 Baseline and Governance

## Context

DeepPharma needs a durable, reviewable engineering baseline before execution
work is claimed. The repository baseline is approved for MVP planning under
ADR-060's temporary manual refinement exception.

## Scope

- Preserve the constitution, requirements, architecture and traceability
  artifacts as the planning source of truth.
- Define tracker metadata, readiness, dependency and publication controls.
- Preserve explicit limitations for local benchmark evidence and unexecuted
  acceptance criteria.

## Acceptance criteria

- Requirements and architecture artifacts have stable IDs, fixed points,
  digests and approval records.
- AC-01–AC-14 have owner, status, planned verification and evidence fields.
- Canonical labels and readiness rules are documented and reconciled.
- The manual refinement exception is recorded and does not claim automatic
  refinement success.

## Non-goals

Production certification, clinical validity, institutional SALMI integration and
implementation of product behavior.

## Risks

- Manual refinement may hide drift unless every handoff remains versioned.
- Unexecuted criteria must not be interpreted as completed evidence.

## Dependencies

- None for planning; child Sub-Specs depend on this Parent Spec reaching
  `status:ready`.

## Validation

- `python3 -m json.tool` on the RequirementsArtifact and ArchitectureArtifact.
- `git diff --check`.
- Read-only Project and label reconciliation.

## Traceability

`AC-01–AC-14`, `ADR-060`,
`docs/requirements/acceptance-traceability-mvp.md`.

## Blocked by

None.

## Child Sub-Specs

Governance evidence, tracker contract, and refinement exception closeout.

## Source

`docs/spec/constitution.md`, `docs/engineering/refinement-baseline.md`,
`docs/requirements/acceptance-traceability-mvp.md`, ADR-060.
