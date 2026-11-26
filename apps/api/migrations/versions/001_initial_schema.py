"""initial inventory schema

Revision ID: 001_initial_schema
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "001_initial_schema"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "medicamentos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(length=200), nullable=False),
    )
    op.create_index("ix_medicamentos_nombre", "medicamentos", ["nombre"], unique=True)
    op.create_table(
        "centros_salud",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(length=200), nullable=False),
    )
    op.create_index("ix_centros_salud_nombre", "centros_salud", ["nombre"], unique=True)
    op.create_table(
        "inventario_actual",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("medicamento_id", sa.Integer(), nullable=False),
        sa.Column("centro_salud_id", sa.Integer(), nullable=False),
        sa.Column("stock_actual", sa.Integer(), nullable=False),
        sa.Column(
            "actualizado_en", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.ForeignKeyConstraint(["medicamento_id"], ["medicamentos.id"]),
        sa.ForeignKeyConstraint(["centro_salud_id"], ["centros_salud.id"]),
    )


def downgrade() -> None:
    op.drop_table("inventario_actual")
    op.drop_index("ix_centros_salud_nombre", table_name="centros_salud")
    op.drop_table("centros_salud")
    op.drop_index("ix_medicamentos_nombre", table_name="medicamentos")
    op.drop_table("medicamentos")
