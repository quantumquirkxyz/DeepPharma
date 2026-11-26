# Parent Spec — M3 Alerts, Audit and Notifications

## Context

Operational risk becomes useful only when authorised users can manage alerts
with an auditable lifecycle and simulated notification behavior.

## Scope

- Alert lifecycle and terminal-state rules.
- Human review and authorization.
- Append-only audit history.
- Simulated notifications and retry behavior.

## Acceptance criteria

- Alert transitions follow ADR-018 and preserve actor, previous state, new
  state and comment.
- Terminal alerts cannot be modified.
- Unauthorized transitions and audit queries are rejected and recorded.
- Notifications never send institutional messages and record retry outcomes.

## Non-goals

Institutional notification channels, autonomous clinical actions and external
communication contracts.

## Risks

- Incorrect transition authorization could expose or mutate operational state.
- Notification retries must not duplicate side effects or contact institutions.

## Dependencies

- M0 governance (#2) and M2 risk result contract (#4).

## Validation

- State-machine transition table tests.
- Authorization and append-only audit tests.
- Simulated notification retry and failure tests.

## Traceability

`US-03–US-04`, `AC-08–AC-14`, `ADR-018`, `ADR-019`,
`ADR-029–ADR-031`.

## Blocked by

M0 Parent Spec (#2) and M2 Parent Spec (#4) reaching `status:ready`.

## Child Sub-Specs

Alert state machine, audit controls, notification adapter and failure behavior.

## Source

`docs/spec/mvp-inventory-risk.md` US-03/US-04, ADR-018, ADR-019 and
ADR-029–ADR-031.
