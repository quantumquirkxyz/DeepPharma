from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .auth import get_current_user, require_scope
from .models import CentroSalud, InventarioActual, Medicamento, RegistroInventario
from .models import Usuario
from .schemas import InventoryCreate, InventoryHistoryRead, InventoryRead

router = APIRouter(prefix="/api/v1/inventory", tags=["inventory"])


@router.get("", response_model=list[InventoryRead])
def list_inventory(
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[InventarioActual]:
    return list(db.scalars(select(InventarioActual).order_by(InventarioActual.id)))


@router.post("", response_model=InventoryRead, status_code=status.HTTP_201_CREATED)
def create_inventory(
    payload: InventoryCreate,
    db: Session = Depends(get_db),
    user: Usuario = Security(get_current_user, scopes=["inventory:write"]),
) -> InventarioActual:
    if db.get(Medicamento, payload.medicamento_id) is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    if db.get(CentroSalud, payload.centro_salud_id) is None:
        raise HTTPException(status_code=404, detail="Centro de salud no encontrado")

    inventory = (
        db.query(InventarioActual)
        .filter_by(
            medicamento_id=payload.medicamento_id,
            centro_salud_id=payload.centro_salud_id,
        )
        .one_or_none()
    )
    previous_stock = inventory.stock_actual if inventory else 0
    if inventory is None:
        inventory = InventarioActual(**payload.model_dump())
        db.add(inventory)
        db.flush()
    else:
        inventory.stock_actual = payload.stock_actual

    db.add(
        RegistroInventario(
            inventario_id=inventory.id,
            stock_anterior=previous_stock,
            stock_nuevo=payload.stock_actual,
            fuente="MANUAL",
            actor=user.username,
        )
    )
    db.commit()
    db.refresh(inventory)
    return inventory


@router.get("/{inventory_id}/history", response_model=list[InventoryHistoryRead])
def inventory_history(
    inventory_id: int,
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:read"]),
) -> list[RegistroInventario]:
    if db.get(InventarioActual, inventory_id) is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return list(
        db.scalars(
            select(RegistroInventario)
            .where(RegistroInventario.inventario_id == inventory_id)
            .order_by(RegistroInventario.registrado_en)
        )
    )
