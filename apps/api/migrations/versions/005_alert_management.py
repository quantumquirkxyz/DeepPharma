"""add alert management history

Revision ID: 005_alert_management
Revises: 004_risk_baseline
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "005_alert_management"
down_revision: Union[str, None] = "004_risk_baseline"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "gestion_alerta",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("alerta_id", sa.Integer(), nullable=False),
        sa.Column("estado_anterior", sa.String(length=30), nullable=False),
        sa.Column("estado_nuevo", sa.String(length=30), nullable=False),
        sa.Column("actor", sa.String(length=120), nullable=False),
        sa.Column("comentario", sa.String(length=500), nullable=True),
        sa.Column(
            "gestionada_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.ForeignKeyConstraint(["alerta_id"], ["alertas_desabastecimiento.id"]),
    )


def downgrade() -> None:
    op.drop_table("gestion_alerta")
