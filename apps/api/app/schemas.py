from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InventoryCreate(BaseModel):
    medicamento_id: int = Field(gt=0)
    centro_salud_id: int = Field(gt=0)
    stock_actual: int = Field(ge=0)


class InventoryRead(InventoryCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    actualizado_en: datetime


class InventoryHistoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    inventario_id: int
    stock_anterior: int
    stock_nuevo: int
    fuente: str
    actor: str
    registrado_en: datetime


class PredictionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    inventario_id: int
    probabilidad: float
    nivel: str
    horizonte_dias: int
    modelo_version: str
    generado_en: datetime


class AlertRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    inventario_id: int
    prediccion_id: int
    nivel: str
    estado: str
    creada_en: datetime


class AlertUpdate(BaseModel):
    estado: str
    comentario: str | None = None


class AlertManagementRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    alerta_id: int
    estado_anterior: str
    estado_nuevo: str
    actor: str
    comentario: str | None
    gestionada_en: datetime
