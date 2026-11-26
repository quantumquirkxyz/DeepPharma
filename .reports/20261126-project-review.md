# DeepPharma Project Review — 2026-11-26

## Executive summary

DeepPharma is **viable for incremental implementation**, but it is not yet a
complete MVP or production-ready system.

The executable tracer bullet is functional: the API has 12 passing tests, the
web application passes lint and production build, and the isolated migration
chain is usable. The current implementation covers inventory CRUD, basic JWT
scopes, dataset validation, a deterministic risk baseline and simple alert
history.

Implementation may begin on Tickets **#25** and **#28**, the only tickets
currently marked `status:ready`. Tickets #26–#42 remain blocked by explicit
dependencies or missing evidence.

## Verification performed

| Check | Result | Evidence |
|---|---|---|
| API tests | PASS: 12 passed | `apps/api/tests/test_health.py` |
| API coverage | 93% of 386 statements | `uv run pytest --cov=app` |
| Web lint | PASS | `apps/web/package.json` |
| Web production build | PASS | Next.js build |
| Isolated Alembic migration | PASS | `.reports/execution/20261126/alembic-upgrade-isolated.txt` |
| Existing local DB migration check | BLOCKED | Database is not at the migration head |
| Skill bundle gate | BLOCKED | Missing referenced external fixtures |
| Acceptance traceability | PARTIAL | `docs/requirements/acceptance-traceability-mvp.md` |

## Findings

### F1 — Coverage formula is not implemented

- **Severity:** High
- **Confidence:** High
- **Evidence:** `apps/api/app/risk.py:19-25` classifies only current stock;
  `docs/adr/ADR-057-formula-consumo-cobertura.md` requires a 30-day
  consumption-based denominator and `INDETERMINATE`.
- **Impact:** Risk results do not yet implement the approved domain rule.
- **Remediation:** Implement Ticket #30 after Tickets #28 and #29.

### F2 — Authorization scope is incomplete

- **Severity:** High
- **Confidence:** High
- **Evidence:** `apps/api/app/catalog.py:11-20` exposes catalogs without
  authentication; `apps/api/app/inventory.py:14-19` lists all inventory
  records without health-center scope filtering; ADR-006 and ADR-020 require
  scoped, deny-by-default access.
- **Impact:** The tracer bullet does not satisfy the approved access boundary.
- **Remediation:** Implement Ticket #38 with explicit role/scope integration
  tests.

### F3 — Alert state transitions are under-specified in code

- **Severity:** High
- **Confidence:** High
- **Evidence:** `apps/api/app/risk.py:105-116` checks allowed target states but
  does not enforce a transition graph; `GET /alerts` excludes `RESUELTA` but
  still returns `DESCARTADA`.
- **Impact:** Invalid transitions and terminal alert visibility can diverge
  from ADR-018.
- **Remediation:** Implement Ticket #35 with a transition table and terminal
  state tests.

### F4 — Valid datasets are validated but not safely applied

- **Severity:** High
- **Confidence:** High
- **Evidence:** `apps/api/app/datasets.py:106-129` persists validation output,
  but there is no application endpoint or import service; AC-03/AC-04 require
  transactional application and provenance.
- **Impact:** The current flow cannot complete the inventory import use case.
- **Remediation:** Implement Ticket #29 after Ticket #28.

### F5 — Migration ownership is mixed with runtime schema creation

- **Severity:** Medium
- **Confidence:** High
- **Evidence:** `apps/api/app/main.py:31` calls
  `Base.metadata.create_all(bind=engine)` while Alembic is also the migration
  mechanism; `.reports/execution/20261126/alembic-upgrade.txt` records the
  stale local database condition.
- **Impact:** Runtime startup can hide migration drift and create divergent
  environments.
- **Remediation:** Remove runtime schema creation from production startup and
  make migration state an explicit operational prerequisite.

### F6 — Audit, lineage, notification and ML evidence remain incomplete

- **Severity:** High
- **Confidence:** High
- **Evidence:** AC-06c–AC-06i and AC-11–AC-14 are `Partial` or `Not executed`
  in `docs/requirements/acceptance-traceability-mvp.md`; the corresponding
  domain tables and adapters are not present in the current API.
- **Impact:** The system must not be described as auditable ML, production
  notification, institutional integration or clinical decision support.
- **Remediation:** Implement the blocked Tickets #31–#42 incrementally and
  preserve typed evidence.

### F7 — Alembic model/migration nullability drift

- **Severity:** Medium
- **Confidence:** High
- **Evidence:** A fresh SQLite database upgrades through revision `006_datasets`,
  but `uv run alembic check` reports six `modify_nullable` operations for
  timestamp columns. The model declarations are in
  `apps/api/app/models.py:69-142`; the migration chain is under
  `apps/api/migrations/versions/`.
- **Impact:** Schema drift can remain undetected and may complicate PostgreSQL
  deployment or future migrations.
- **Remediation:** Create a dedicated migration-hardening Ticket to choose and
  test the canonical nullability contract; do not rewrite historical
  migrations in place.

## Readiness decision

### Start now

- **#25 — Implement artifact provenance validation**
- **#28 — Implement dataset validation vertical slice**

These are the current executable frontier. Each implementation should create
one branch, add focused tests, update evidence and open at most one PR.

### Do not start yet

Tickets #26–#42 remain blocked. In particular, do not begin coverage, risk
lineage, alert hardening, authorization, notifications or final verification
until their declared dependencies are resolved.

## README changes

The root README now documents:

- actual current capabilities versus unimplemented MVP commitments;
- modular-monolith architecture and runtime request flow diagrams;
- Project hierarchy and current ready tickets;
- reproducible local setup;
- API surface;
- verification evidence and known limitations;
- documentation, security and contribution links.

## Residual limitations

- No production deployment or CI workflow is present.
- Security and privacy verification is not complete.
- The skill-bundle gate depends on missing external fixtures.
- Local benchmark evidence is not institutional or production assurance.
- The local SQLite file must be fresh or migrated before running Alembic checks.
