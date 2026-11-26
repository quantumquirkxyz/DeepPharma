from datetime import datetime

from sqlalchemy import (
    JSON,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Medicamento(Base):
    __tablename__ = "medicamentos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200), unique=True, index=True)


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    rol: Mapped[str] = mapped_column(String(50))
    activo: Mapped[bool] = mapped_column(default=True)


class ConjuntoDatos(Base):
    __tablename__ = "conjuntos_datos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    version: Mapped[str] = mapped_column(String(80))
    fuente: Mapped[str] = mapped_column(String(200))
    estado: Mapped[str] = mapped_column(String(30))
    registros: Mapped[int] = mapped_column(Integer)
    errores: Mapped[int] = mapped_column(Integer)
    datos: Mapped[list[dict[str, object]]] = mapped_column(JSON)
    recibido_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class CentroSalud(Base):
    __tablename__ = "centros_salud"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200), unique=True, index=True)


class InventarioActual(Base):
    __tablename__ = "inventario_actual"
    __table_args__ = (
        UniqueConstraint(
            "medicamento_id", "centro_salud_id", name="uq_inventario_medicamento_centro"
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    medicamento_id: Mapped[int] = mapped_column(ForeignKey("medicamentos.id"))
    centro_salud_id: Mapped[int] = mapped_column(ForeignKey("centros_salud.id"))
    stock_actual: Mapped[int] = mapped_column(Integer)
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    medicamento: Mapped[Medicamento] = relationship()
    centro_salud: Mapped[CentroSalud] = relationship()
    historial: Mapped[list["RegistroInventario"]] = relationship(
        back_populates="inventario", order_by="RegistroInventario.registrado_en"
    )


class RegistroInventario(Base):
    __tablename__ = "registro_inventario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    inventario_id: Mapped[int] = mapped_column(ForeignKey("inventario_actual.id"))
    stock_anterior: Mapped[int] = mapped_column(Integer)
    stock_nuevo: Mapped[int] = mapped_column(Integer)
    fuente: Mapped[str] = mapped_column(String(30), default="MANUAL")
    actor: Mapped[str] = mapped_column(String(120))
    registrado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    inventario: Mapped[InventarioActual] = relationship(back_populates="historial")


class PrediccionRiesgo(Base):
    __tablename__ = "predicciones_riesgo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    inventario_id: Mapped[int] = mapped_column(ForeignKey("inventario_actual.id"))
    probabilidad: Mapped[float] = mapped_column(Float)
    nivel: Mapped[str] = mapped_column(String(30))
    horizonte_dias: Mapped[int] = mapped_column(Integer)
    modelo_version: Mapped[str] = mapped_column(String(80))
    generado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    inventario: Mapped[InventarioActual] = relationship()


class AlertaDesabastecimiento(Base):
    __tablename__ = "alertas_desabastecimiento"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    inventario_id: Mapped[int] = mapped_column(ForeignKey("inventario_actual.id"))
    prediccion_id: Mapped[int] = mapped_column(ForeignKey("predicciones_riesgo.id"))
    nivel: Mapped[str] = mapped_column(String(30))
    estado: Mapped[str] = mapped_column(String(30), default="NUEVA")
    creada_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    inventario: Mapped[InventarioActual] = relationship()
    prediccion: Mapped[PrediccionRiesgo] = relationship()
    gestiones: Mapped[list["GestionAlerta"]] = relationship(
        back_populates="alerta", order_by="GestionAlerta.gestionada_en"
    )


class GestionAlerta(Base):
    __tablename__ = "gestion_alerta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    alerta_id: Mapped[int] = mapped_column(ForeignKey("alertas_desabastecimiento.id"))
    estado_anterior: Mapped[str] = mapped_column(String(30))
    estado_nuevo: Mapped[str] = mapped_column(String(30))
    actor: Mapped[str] = mapped_column(String(120))
    comentario: Mapped[str | None] = mapped_column(String(500), nullable=True)
    gestionada_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    alerta: Mapped[AlertaDesabastecimiento] = relationship(back_populates="gestiones")
