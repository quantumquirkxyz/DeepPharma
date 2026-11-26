from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .models import CentroSalud, Medicamento

router = APIRouter(prefix="/api/v1/catalog", tags=["catalog"])


@router.get("/medicamentos")
def list_medicamentos(db: Session = Depends(get_db)) -> list[dict[str, int | str]]:
    items = db.scalars(select(Medicamento).order_by(Medicamento.nombre))
    return [{"id": item.id, "nombre": item.nombre} for item in items]


@router.get("/centros-salud")
def list_centros_salud(db: Session = Depends(get_db)) -> list[dict[str, int | str]]:
    items = db.scalars(select(CentroSalud).order_by(CentroSalud.nombre))
    return [{"id": item.id, "nombre": item.nombre} for item in items]
