"""Load synthetic development data only."""

import os

from pwdlib import PasswordHash

from app.database import Base, SessionLocal, engine
from app.models import CentroSalud, InventarioActual, Medicamento, Usuario

Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    demo_user = db.query(Usuario).filter_by(username="farmaceutico.demo").one_or_none()
    if demo_user is None:
        password = os.getenv("DEMO_PASSWORD")
        if not password:
            raise RuntimeError("Set DEMO_PASSWORD before running the seed.")
        db.add(
            Usuario(
                username="farmaceutico.demo",
                hashed_password=PasswordHash.recommended().hash(password),
                rol="farmaceutico",
            )
        )

    medicamento = (
        db.query(Medicamento).filter_by(nombre="Amoxicilina 500mg").one_or_none()
    )
    if medicamento is None:
        medicamento = Medicamento(nombre="Amoxicilina 500mg")
        db.add(medicamento)

    centro = (
        db.query(CentroSalud)
        .filter_by(nombre="Centro de Salud Juan Díaz")
        .one_or_none()
    )
    if centro is None:
        centro = CentroSalud(nombre="Centro de Salud Juan Díaz")
        db.add(centro)

    db.flush()
    existing = (
        db.query(InventarioActual)
        .filter_by(medicamento_id=medicamento.id, centro_salud_id=centro.id)
        .one_or_none()
    )
    if existing is None:
        db.add(
            InventarioActual(
                medicamento_id=medicamento.id,
                centro_salud_id=centro.id,
                stock_actual=50,
            )
        )
    db.commit()
    print("Synthetic seed loaded.")
