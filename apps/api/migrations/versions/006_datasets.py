"""add validated datasets

Revision ID: 006_datasets
Revises: 005_alert_management
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "006_datasets"
down_revision: Union[str, None] = "005_alert_management"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "conjuntos_datos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("version", sa.String(length=80), nullable=False),
        sa.Column("fuente", sa.String(length=200), nullable=False),
        sa.Column("estado", sa.String(length=30), nullable=False),
        sa.Column("registros", sa.Integer(), nullable=False),
        sa.Column("errores", sa.Integer(), nullable=False),
        sa.Column("datos", sa.JSON(), nullable=False),
        sa.Column(
            "recibido_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )


def downgrade() -> None:
    op.drop_table("conjuntos_datos")
