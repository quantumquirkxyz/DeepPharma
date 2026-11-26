from typing import Any

from fastapi import APIRouter, Depends, Security
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from .auth import get_current_user
from .database import get_db
from .models import CentroSalud, ConjuntoDatos, Medicamento, Usuario

router = APIRouter(prefix="/api/v1/datasets", tags=["datasets"])


class DatasetPayload(BaseModel):
    version: str = Field(min_length=1, max_length=80)
    fuente: str = Field(min_length=1, max_length=200)
    registros: list[dict[str, Any]]


class ValidationIssue(BaseModel):
    fila: int
    codigo: str
    mensaje: str


class DatasetValidationResult(BaseModel):
    dataset_id: int
    estado: str
    registros: int
    errores: list[ValidationIssue]


REQUIRED_FIELDS = {"medicamento_id", "centro_salud_id", "stock_actual"}


def validate_records(
    records: list[dict[str, Any]], db: Session
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    seen: set[tuple[int, int]] = set()
    medication_ids = {item.id for item in db.query(Medicamento).all()}
    center_ids = {item.id for item in db.query(CentroSalud).all()}

    for row_number, record in enumerate(records, start=1):
        missing = REQUIRED_FIELDS - record.keys()
        if missing:
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="MISSING_FIELD",
                    mensaje=f"Faltan campos: {', '.join(sorted(missing))}",
                )
            )
            continue
        try:
            medication_id = int(record["medicamento_id"])
            center_id = int(record["centro_salud_id"])
            stock = int(record["stock_actual"])
        except (TypeError, ValueError):
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="INVALID_TYPE",
                    mensaje="Los identificadores y el stock deben ser enteros",
                )
            )
            continue

        key = (medication_id, center_id)
        if stock < 0:
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="NEGATIVE_STOCK",
                    mensaje="El stock no puede ser negativo",
                )
            )
        if medication_id not in medication_ids:
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="UNKNOWN_MEDICINE",
                    mensaje="El medicamento no existe",
                )
            )
        if center_id not in center_ids:
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="UNKNOWN_CENTER",
                    mensaje="El centro de salud no existe",
                )
            )
        if key in seen:
            issues.append(
                ValidationIssue(
                    fila=row_number,
                    codigo="DUPLICATE_KEY",
                    mensaje="La combinación medicamento-centro está duplicada",
                )
            )
        seen.add(key)
    return issues


@router.post("/validate", response_model=DatasetValidationResult)
def validate_dataset(
    payload: DatasetPayload,
    db: Session = Depends(get_db),
    _: Usuario = Security(get_current_user, scopes=["inventory:write"]),
) -> DatasetValidationResult:
    issues = validate_records(payload.registros, db)
    dataset = ConjuntoDatos(
        version=payload.version,
        fuente=payload.fuente,
        estado="VALIDO" if not issues else "RECHAZADO",
        registros=len(payload.registros),
        errores=len(issues),
        datos=payload.registros,
    )
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return DatasetValidationResult(
        dataset_id=dataset.id,
        estado=dataset.estado,
        registros=dataset.registros,
        errores=issues,
    )
