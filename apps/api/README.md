# DeepPharma API

## Run

```bash
uv run fastapi dev app/main.py
```

Apply schema and load synthetic data:

```bash
uv run alembic upgrade head
uv run python -m scripts.seed
```

The tracer bullet uses SQLite by default for local development. Set
`DATABASE_URL` to a PostgreSQL SQLAlchemy URL for the target environment.
Set `SECRET_KEY` to a securely generated value before starting the API.

## Current endpoints

- `GET /health`
- `GET /api/v1/inventory`
- `POST /api/v1/inventory`
- `GET /api/v1/inventory/{inventory_id}/history`
- `GET /api/v1/catalog/medicamentos`
- `GET /api/v1/catalog/centros-salud`
- `POST /api/v1/risk/evaluate`
- `GET /api/v1/predictions`
- `GET /api/v1/alerts`
- `PATCH /api/v1/alerts/{alert_id}`
- `GET /api/v1/alerts/{alert_id}/history`
- `POST /api/v1/datasets/validate`

Risk evaluation currently uses the documented deterministic baseline
`baseline-rules-1`: stock `<= 10` is critical, `11–30` is medium, and
values above `30` are low. It is not an ML model and has no claimed accuracy.
Alert transitions are audited with actor, previous state, new state and optional
comment.

Authentication, audit history and SALMI integration remain planned increments.
