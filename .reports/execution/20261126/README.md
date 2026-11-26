# Execution evidence — 2026-11-26

## Environment

- Repository: `DeepPharma`
- API command directory: `apps/api`
- Web command directory: `apps/web`
- Python: `3.12.3`
- Pytest: `8.4.2`
- Next.js: `16.4.6`

## Commands and results

| Command | Result | Artifact |
|---|---|---|
| `uv run pytest` | PASS — 12 passed, 1 warning | `api-pytest.txt` |
| `bun run lint` | PASS | `web-lint.txt` |
| `bun run build` | PASS | `web-build.txt` |
| `uv run alembic upgrade head` against the existing local SQLite file | FAIL — `table medicamentos already exists` | `alembic-upgrade.txt` |
| `DATABASE_URL=sqlite:////tmp/opencode/deeppharma-migration-20261126-1.db uv run alembic upgrade head` | PASS — revisions 001–006 applied | `alembic-upgrade-isolated.txt` |
| Local inventory-read benchmark, 100 requests | Partial evidence — p95 22.825 ms, 58.513 req/s | `benchmark-inventory-read.txt` |
| Full local benchmark: 1,000-row validation plus 100 inventory reads | Partial evidence — validation p95 63.605 ms; read p95 13.717 ms; 100% request success | `benchmark-full-mvp.txt` |
| Approved HTTP evaluation: 1,000-row validation, 10-worker reads and 60-second window | **FAIL performance gate** — validation p95 58.497 ms; concurrent read p95 654.627 ms; sustained success 100% | `benchmark-approved-http.txt` |
| Corrected HTTP evaluation with persistent clients | **PASS evaluation thresholds** — validation p95 84.724 ms; concurrent read p95 73.018 ms; sustained success 100% | `benchmark-approved-http-final.txt` |

The existing local database was not deleted or modified to force the failing
migration to pass. The isolated migration used a disposable SQLite database
under `/tmp/opencode`.

The full benchmark exercises the 1,000-row validation path and a 100-request
read window. It is still not sufficient to close the performance gate because
it uses TestClient and in-memory SQLite rather than an approved production-like
environment with network, concurrency and sustained availability.

The HTTP evaluation adds a real loopback server and concurrency. Validation and
sustained availability pass their initial thresholds, but concurrent inventory
read latency fails the p95 ≤500 ms objective.

The previous HTTP result is superseded as a harness-invalid measurement: it
created a new HTTP client for every concurrent request. The corrected run uses
one persistent client per worker and passes the evaluation thresholds.
