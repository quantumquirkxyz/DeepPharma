# DeepPharma Context

## Repository identity

- **Repository:** DeepPharma
- **Purpose:** Pharmaceutical and drug-discovery software repository.
- **Canonical skills:** `.agents/skills/`
- **Compatibility view:** `.claude/skills/` (generated symlinks; do not edit by hand)
- **Skill provenance:** `skills-lock.json`

## Local vocabulary

Use the repository name **DeepPharma** and the quirk Skills terms **canonical skill**, **compatibility view**, and **provenance**. Do not assume domain terms, workflows, or deployment details that are not documented in this repository.

## Skills operations

- Run the full bundle gate with `node .agents/skills/platform/check-all.mjs`.
- Validate the installation with `node .agents/skills/platform/validate-skills.mjs`.
- Audit semantics with `node .agents/skills/platform/audit-semantics.mjs`.
- Check compatibility drift with `node .agents/skills/platform/fix-compatibility-view.mjs --dry-run`.
- Keep canonical skills and the compatibility view synchronized; preserve symlinks and lockfile hashes.

## Scope discipline

Keep future work limited to the requested change. Preserve repository documentation and ADRs unless explicitly asked to change them.
