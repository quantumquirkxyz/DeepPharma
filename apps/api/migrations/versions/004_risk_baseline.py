"""add deterministic risk baseline

Revision ID: 004_risk_baseline
Revises: 003_users
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "004_risk_baseline"
down_revision: Union[str, None] = "003_users"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "predicciones_riesgo",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("inventario_id", sa.Integer(), nullable=False),
        sa.Column("probabilidad", sa.Float(), nullable=False),
        sa.Column("nivel", sa.String(length=30), nullable=False),
        sa.Column("horizonte_dias", sa.Integer(), nullable=False),
        sa.Column("modelo_version", sa.String(length=80), nullable=False),
        sa.Column(
            "generado_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.ForeignKeyConstraint(["inventario_id"], ["inventario_actual.id"]),
    )
    op.create_table(
        "alertas_desabastecimiento",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("inventario_id", sa.Integer(), nullable=False),
        sa.Column("prediccion_id", sa.Integer(), nullable=False),
        sa.Column("nivel", sa.String(length=30), nullable=False),
        sa.Column("estado", sa.String(length=30), nullable=False),
        sa.Column(
            "creada_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.ForeignKeyConstraint(["inventario_id"], ["inventario_actual.id"]),
        sa.ForeignKeyConstraint(["prediccion_id"], ["predicciones_riesgo.id"]),
    )


def downgrade() -> None:
    op.drop_table("alertas_desabastecimiento")
    op.drop_table("predicciones_riesgo")
