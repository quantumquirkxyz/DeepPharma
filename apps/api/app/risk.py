from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy import select
from sqlalchemy.orm import Session

from .auth import get_current_user
from .database import get_db
from .models import (
    AlertaDesabastecimiento,
    GestionAlerta,
    InventarioActual,
    PrediccionRiesgo,
    Usuario,
)
from .schemas import AlertManagementRead, AlertRead, AlertUpdate, PredictionRead

router = APIRouter(prefix="/api/v1", tags=["risk"])


def classify_stock(stock: int) -> tuple[str, float]:
    """Deterministic baseline; this is not an ML model."""
    if stock <= 10:
        return "CRITICA", 0.95
    if stock <= 30:
        return "MEDIA", 0.65
    return "BAJA", 0.15


def evaluate_inventory(
    db: Session, inventory: InventarioActual
) -> tuple[PrediccionRiesgo, AlertaDesabastecimiento | None]:
    level, probability = classify_stock(inventory.stock_actual)
    prediction = PrediccionRiesgo(
        inventario_id=inventory.id,
        probabilidad=probability,
        nivel=level,
        horizonte_dias=30,
        modelo_version="baseline-rules-1",
    )
    db.add(prediction)
    db.flush()

    alert = None
    if level == "CRITICA":
        active_alert = db.scalars(
            select(AlertaDesabastecimiento)
            .where(
                AlertaDesabastecimiento.inventario_id == inventory.id,
                AlertaDesabastecimiento.estado.not_in(["RESUELTA", "DESCARTADA"]),
            )
            .limit(1)
        ).first()
        if active_alert is None:
            alert = AlertaDesabastecimiento(
                inventario_id=inventory.id,
                prediccion_id=prediction.id,
                nivel=level,
                estado="NUEVA",
            )
            db.add(alert)
    return prediction, alert


@router.post("/risk/evaluate", response_model=list[PredictionRead])
def evaluate_risk(
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[PrediccionRiesgo]:
    inventories = db.scalars(
        select(InventarioActual).order_by(InventarioActual.id)
    ).all()
    predictions = [evaluate_inventory(db, inventory)[0] for inventory in inventories]
    db.commit()
    return predictions


@router.get("/predictions", response_model=list[PredictionRead])
def list_predictions(
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[PrediccionRiesgo]:
    return list(db.scalars(select(PrediccionRiesgo).order_by(PrediccionRiesgo.id)))


@router.get("/alerts", response_model=list[AlertRead])
def list_alerts(
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[AlertaDesabastecimiento]:
    return list(
        db.scalars(
            select(AlertaDesabastecimiento)
            .where(AlertaDesabastecimiento.estado != "RESUELTA")
            .order_by(AlertaDesabastecimiento.id)
        )
    )


@router.patch("/alerts/{alert_id}", response_model=AlertRead)
def update_alert(
    alert_id: int,
    payload: AlertUpdate,
    db: Session = Depends(get_db),
    user: Usuario = Security(get_current_user, scopes=["alerts:manage"]),
) -> AlertaDesabastecimiento:
    allowed_states = {"RECONOCIDA", "EN_REVISION", "RESUELTA", "DESCARTADA"}
    if payload.estado not in allowed_states:
        raise HTTPException(status_code=422, detail="Estado de alerta no válido")

    alert = db.get(AlertaDesabastecimiento, alert_id)
    if alert is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    if alert.estado in {"RESUELTA", "DESCARTADA"}:
        raise HTTPException(status_code=409, detail="La alerta ya está cerrada")

    previous_state = alert.estado
    alert.estado = payload.estado
    db.add(
        GestionAlerta(
            alerta_id=alert.id,
            estado_anterior=previous_state,
            estado_nuevo=payload.estado,
            actor=user.username,
            comentario=payload.comentario,
        )
    )
    db.commit()
    db.refresh(alert)
    return alert


@router.get("/alerts/{alert_id}/history", response_model=list[AlertManagementRead])
def alert_history(
    alert_id: int,
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[GestionAlerta]:
    if db.get(AlertaDesabastecimiento, alert_id) is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return list(
        db.scalars(
            select(GestionAlerta)
            .where(GestionAlerta.alerta_id == alert_id)
            .order_by(GestionAlerta.id)
        )
    )
