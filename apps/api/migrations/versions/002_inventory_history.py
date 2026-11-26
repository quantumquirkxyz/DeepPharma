"""add inventory history

Revision ID: 002_inventory_history
Revises: 001_initial_schema
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002_inventory_history"
down_revision: Union[str, None] = "001_initial_schema"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("inventario_actual") as batch_op:
        batch_op.create_unique_constraint(
            "uq_inventario_medicamento_centro",
            ["medicamento_id", "centro_salud_id"],
        )
    op.create_table(
        "registro_inventario",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("inventario_id", sa.Integer(), nullable=False),
        sa.Column("stock_anterior", sa.Integer(), nullable=False),
        sa.Column("stock_nuevo", sa.Integer(), nullable=False),
        sa.Column("fuente", sa.String(length=30), nullable=False),
        sa.Column("actor", sa.String(length=120), nullable=False),
        sa.Column(
            "registrado_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.ForeignKeyConstraint(["inventario_id"], ["inventario_actual.id"]),
    )


def downgrade() -> None:
    op.drop_table("registro_inventario")
    with op.batch_alter_table("inventario_actual") as batch_op:
        batch_op.drop_constraint("uq_inventario_medicamento_centro", type_="unique")
