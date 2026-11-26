# Canonical work-item format

## Required fields

- Title: concise, imperative and domain-specific.
- Body: problem, goals, non-goals, acceptance criteria, risks, dependencies,
  validation commands and traceability.
- Labels for publishable MVP work items: exactly one workflow label, one
  work-type label, one discipline label, one priority label and one risk label.
  Use `risk:unknown` when evaluation is not yet sufficient.
- The GitHub Project `Status` field mirrors the Issue `status:*` label and is
  not an independent workflow source of truth.
- Issues and PRs carry the canonical labels; the Project's native Labels field
  projects them. Priority and Risk remain labels, not duplicate Project fields.
- Parent Spec issues use `type:spec`, `area:requirements` and `status:ready`
  only after acceptance criteria are reviewable.
- Sub-Spec issues use `type:sub-spec`, `area:requirements` and a valid
  `status:*`; they remain children of a Parent Spec.
- Other documentation issues use `type:documentation`.

## Ticket requirements

Every implementation ticket must include:

1. parent spec issue;
2. requirements and acceptance criteria;
3. explicit seams;
4. blocking and blocked-by edges;
5. files or modules in scope;
6. tests and evidence required;
7. non-goals and residual risks.

The initial MVP hierarchy requires native sub-issues for Parent
Spec → Sub-Spec → Ticket relationships. A task list is not an equivalent
substitute.

The Parent Spec, Sub-Specs, and Tickets in one delivery share the same
Milestone; the Milestone groups delivery and does not replace parent-child
relationships.

Parent-child hierarchy does not imply blocking. Use native `blocked_by`
relationships only for real execution prerequisites and repeat them in the
Issue body.

Implementation delivery uses at most one PR per Ticket, with branch
`issue/<number>-<slug>` and copied labels/Milestone.

Readiness is hierarchical: a Sub-Spec cannot be `status:ready` before its
Parent Spec, and a Ticket cannot be `status:ready` before its criteria, seam,
tests, evidence, and blockers are resolved.

For the initial MVP hierarchy, Parent Specs, Sub-Specs, and their Tickets use
`area:requirements`; the `type:*` label still distinguishes the kind of item.

The tracker label contract is defined in
`docs/adr/ADR-045-contrato-de-labels-por-nivel.md`.

## State transitions

`status:triage → status:needs-info/status:ready → status:in-progress → status:review → status:done`

Use `status:needs-info` when clarification is required and `status:blocked`
when a real dependency prevents progress. Both require a reason in the body.
Use `status:ready` only when the ticket can be implemented without guessing.
