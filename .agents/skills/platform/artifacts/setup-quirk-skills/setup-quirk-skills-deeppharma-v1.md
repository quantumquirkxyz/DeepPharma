# SetupQuirkSkillsArtifact

- **Operation ID:** `setup-quirk-skills-deeppharma-v1`
- **Repository:** `quantumquirkxyz/DeepPharma`
- **Provider:** GitHub Issues
- **Scope:** Repository configuration and approved GitHub label reconciliation.
- **Layout:** Single-context (`CONTEXT.md` and `docs/adr/`)
- **Approval:** User approved the draft and selected root `AGENTS.md`.

## Generated projections

- `AGENTS.md`
- `docs/reference/agents/issue-tracker.md`
- `docs/reference/agents/triage-labels.md`
- `docs/reference/agents/domain.md`

## Idempotency

Re-running this operation with the same operation ID reconciles these files and updates the managed `## Agent skills` block without duplicating it.

## Rollback

Remove the generated projection files and the managed Agent skills block from `AGENTS.md`, preserving unrelated content.

## Validation

Generated paths validated. GitHub authentication and repository access were confirmed. All 28 approved namespaced labels were reconciled; existing unrelated labels were preserved.
