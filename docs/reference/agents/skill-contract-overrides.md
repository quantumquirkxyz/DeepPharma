# Repository overrides for generic Skills

DeepPharma applies the following repository-specific overrides when generic
Skills mention different tracker labels:

| Generic reference | DeepPharma contract |
|---|---|
| `spec` | `type:spec` for Parent Specs |
| `ready-for-agent` | `status:ready` |
| generic documentation spec | `type:sub-spec` for Sub-Specs |
| missing priority/risk | exactly one `priority:*` and one `risk:*`; use `risk:unknown` when needed |
| `needs-info` mapped to `area:requirements` | `status:needs-info` |

These overrides preserve the local vocabulary in
`docs/reference/agents/triage-labels.md` and
`docs/reference/agents/work-item-format.md`. Generic Skill defaults must not
create conflicting labels.

## Post-grill automatic-refinement input

When deriving `automatic-refinement` input from the
`GrillWithDocsArtifact`, the required `idea` is the artifact's `objective`
copied verbatim. The `context` is the structured combination of the artifact's
context, documents, decisions, evidence, constraints and residual risks.
This deterministic rule avoids inventing an additional discovery statement.
