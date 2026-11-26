# DeepPharma Context

## Product context

DeepPharma is an academic and experimental software project whose purpose is to
manage medicine inventory and support anticipation of operational stockout risk
using data, a reproducible ML pipeline and an explicit deterministic fallback. The
MVP calls this result a **baseline determinista de riesgo operativo**, not a
clinical prediction. DeepPharma is not a clinical decision system and does not
claim institutional truth, clinical accuracy, or a production SALMI integration.

### Primary value actor

The pharmacist needs to consult current inventory, understand operational risk
and manage alerts within an authorised health-center scope.

### Supporting actors

- System administrator: identity, roles, configuration and audit.
- ML engineer: future datasets, experiments and model lifecycle.
- External source: a future authorised SALMI or public-data adapter; it is a
  system actor, not a human role.

### Product boundary

The MVP boundary contains current inventory, validated dataset intake,
deterministic operational-risk baseline, auditable alert lifecycle, backend
RBAC and a simulated external-source adapter. Historical ML training with real
data, real SALMI integration, institutional notifications and clinical
decisions are outside the MVP.

### Evidence posture

The current business process is hypothetical until real institutional evidence
is supplied. Synthetic fixtures are acceptable for development and prototypes;
they must remain labelled as synthetic.

## Repository identity

- **Repository:** DeepPharma
- **Purpose:** Academic and experimental medicine-inventory and stockout-risk
  software project.
- **Canonical skills:** `.agents/skills/`
- **Compatibility view:** `.claude/skills/` (generated symlinks; do not edit by hand)
- **Skill provenance:** `skills-lock.json`

## Project engineering baseline

- **Academic method:** RUP with UML 2.5.1.
- **Planning method:** SDD with constitution, spec, plan, tasks and verification.
- **Tracker:** GitHub Issues; spec issues precede implementation tickets.
- **Executable MVP:** inventory, dataset validation/import, deterministic risk
  baseline, auditable alerts, RBAC and simulated SALMI adapter.
- **ML boundary:** the MVP includes reproducible ML training/evaluation using
  synthetic or authorised public data, with real experiment metrics and
  explicit limitations. Institutional validity is not claimed.
- **Explicitly outside MVP:** using unauthorised institutional data and
  connecting to an authorised SALMI contract.
- **Data posture:** synthetic, public or authorised data only; no invented
  metrics or institutional evidence.
- **Current implementation:** FastAPI/SQLAlchemy/Alembic API and Next.js
  frontend, with SQLite for local development and PostgreSQL-compatible
  configuration.
- **Documentation status:** MVP requirements and architecture baseline approved
  for planning; tracker work items are published and metadata gates have passed.

## Local vocabulary

Use the repository name **DeepPharma** and the quirk Skills terms **canonical skill**, **compatibility view**, and **provenance**. Do not assume domain terms, workflows, or deployment details that are not documented in this repository.

Domain definitions and unresolved terms are maintained in
[`docs/glossary.md`](docs/glossary.md). When a domain fact is missing, record it
as an explicit clarification rather than silently choosing an institutional
meaning.

## Skills operations

- Run the full bundle gate with `node .agents/skills/platform/check-all.mjs`.
- Validate the installation with `node .agents/skills/platform/validate-skills.mjs`.
- Audit semantics with `node .agents/skills/platform/audit-semantics.mjs`.
- Check compatibility drift with `node .agents/skills/platform/fix-compatibility-view.mjs --dry-run`.
- Keep canonical skills and the compatibility view synchronized; preserve symlinks and lockfile hashes.

## Scope discipline

Keep future work limited to the requested change. Preserve repository documentation and ADRs unless explicitly asked to change them.

## Required workflow

Refine with `grill-with-docs`, establish the SDD artifacts, publish a spec
Issue, derive tickets, then implement one validated slice at a time. Do not
start implementation from an untracked idea or an unapproved requirement.
