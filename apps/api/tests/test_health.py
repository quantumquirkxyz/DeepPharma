import os

os.environ.setdefault("SECRET_KEY", "test-only-key-with-at-least-32-bytes")

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import CentroSalud, Medicamento
from app.models import Usuario
from app.auth import create_access_token, password_hash


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def seed_reference_data() -> None:
    db = TestingSession()
    if db.get(Medicamento, 1) is None:
        db.add(Medicamento(id=1, nombre="Medicamento de prueba"))
    if db.get(CentroSalud, 1) is None:
        db.add(CentroSalud(id=1, nombre="Centro de prueba"))
    if db.query(Usuario).filter_by(username="test.user").one_or_none() is None:
        db.add(
            Usuario(
                username="test.user",
                hashed_password=password_hash.hash("test-password"),
                rol="farmaceutico",
            )
        )
    db.commit()
    db.close()


def auth_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {create_access_token('test.user', ['inventory:read', 'inventory:write', 'alerts:manage'])}"
    }


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "deeppharma-api"}


def test_inventory_starts_with_explicit_empty_state() -> None:
    seed_reference_data()
    response = client.get("/api/v1/inventory", headers=auth_headers())

    assert response.status_code == 200
    assert response.json() == []


def test_inventory_rejects_negative_stock() -> None:
    seed_reference_data()
    response = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": -1},
        headers=auth_headers(),
    )

    assert response.status_code == 422


def test_inventory_creates_valid_update() -> None:
    seed_reference_data()

    response = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 50},
        headers=auth_headers(),
    )

    assert response.status_code == 201
    assert response.json()["stock_actual"] == 50

    update = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 40},
        headers=auth_headers(),
    )
    assert update.status_code == 201

    current = client.get("/api/v1/inventory", headers=auth_headers())
    assert len(current.json()) == 1
    assert current.json()[0]["stock_actual"] == 40

    history = client.get("/api/v1/inventory/1/history", headers=auth_headers())
    assert history.status_code == 200
    assert [
        (entry["stock_anterior"], entry["stock_nuevo"]) for entry in history.json()
    ] == [
        (0, 50),
        (50, 40),
    ]


def test_inventory_rejects_unknown_reference() -> None:
    seed_reference_data()
    response = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 999, "centro_salud_id": 999, "stock_actual": 10},
        headers=auth_headers(),
    )

    assert response.status_code == 404


def test_catalog_lists_medicines_and_health_centers() -> None:
    seed_reference_data()

    medicines = client.get("/api/v1/catalog/medicamentos")
    centers = client.get("/api/v1/catalog/centros-salud")

    assert medicines.status_code == 200
    assert medicines.json()[-1]["nombre"] == "Medicamento de prueba"
    assert centers.status_code == 200
    assert centers.json()[-1]["nombre"] == "Centro de prueba"


def test_inventory_requires_authentication() -> None:
    response = client.get("/api/v1/inventory")

    assert response.status_code == 401


def test_token_endpoint_authenticates_demo_user() -> None:
    seed_reference_data()

    response = client.post(
        "/token",
        data={"username": "test.user", "password": "test-password"},
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_token_scopes_follow_user_role() -> None:
    seed_reference_data()
    db = TestingSession()
    db.add(
        Usuario(
            username="ml.user",
            hashed_password=password_hash.hash("ml-password"),
            rol="ingeniero_ml",
        )
    )
    db.commit()
    db.close()

    token_response = client.post(
        "/token",
        data={"username": "ml.user", "password": "ml-password"},
    )
    assert token_response.status_code == 200

    response = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 5},
        headers={"Authorization": f"Bearer {token_response.json()['access_token']}"},
    )
    assert response.status_code == 401


def test_dataset_validation_persists_valid_source() -> None:
    seed_reference_data()
    response = client.post(
        "/api/v1/datasets/validate",
        json={
            "version": "fixture-2026-01",
            "fuente": "fixture-sintetico",
            "registros": [
                {"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 25}
            ],
        },
        headers=auth_headers(),
    )

    assert response.status_code == 200
    assert response.json()["estado"] == "VALIDO"
    assert response.json()["errores"] == []


def test_invalid_dataset_does_not_change_inventory() -> None:
    seed_reference_data()
    before = client.get("/api/v1/inventory", headers=auth_headers()).json()
    response = client.post(
        "/api/v1/datasets/validate",
        json={
            "version": "fixture-invalid",
            "fuente": "fixture-sintetico",
            "registros": [
                {"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": -2},
                {"medicamento_id": 999, "centro_salud_id": 1, "stock_actual": 5},
                {"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 5},
            ],
        },
        headers=auth_headers(),
    )

    assert response.status_code == 200
    assert response.json()["estado"] == "RECHAZADO"
    assert {issue["codigo"] for issue in response.json()["errores"]} == {
        "NEGATIVE_STOCK",
        "UNKNOWN_MEDICINE",
        "DUPLICATE_KEY",
    }
    assert client.get("/api/v1/inventory", headers=auth_headers()).json() == before


def test_risk_evaluation_creates_prediction_and_critical_alert() -> None:
    seed_reference_data()
    created = client.post(
        "/api/v1/inventory",
        json={"medicamento_id": 1, "centro_salud_id": 1, "stock_actual": 5},
        headers=auth_headers(),
    )
    assert created.status_code == 201

    evaluated = client.post("/api/v1/risk/evaluate", headers=auth_headers())
    assert evaluated.status_code == 200
    assert evaluated.json()[0]["nivel"] == "CRITICA"
    assert evaluated.json()[0]["modelo_version"] == "baseline-rules-1"

    alerts = client.get("/api/v1/alerts", headers=auth_headers())
    assert alerts.status_code == 200
    assert alerts.json()[0]["nivel"] == "CRITICA"
    assert alerts.json()[0]["estado"] == "NUEVA"

    reevaluated = client.post("/api/v1/risk/evaluate", headers=auth_headers())
    assert reevaluated.status_code == 200
    assert len(client.get("/api/v1/alerts", headers=auth_headers()).json()) == 1

    alert_id = alerts.json()[0]["id"]
    updated = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"estado": "RECONOCIDA", "comentario": "Revisada por farmacia"},
        headers=auth_headers(),
    )
    assert updated.status_code == 200
    assert updated.json()["estado"] == "RECONOCIDA"

    history = client.get(f"/api/v1/alerts/{alert_id}/history", headers=auth_headers())
    assert history.status_code == 200
    assert history.json()[0]["actor"] == "test.user"
    assert history.json()[0]["estado_anterior"] == "NUEVA"
