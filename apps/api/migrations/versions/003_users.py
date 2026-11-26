"""add users

Revision ID: 003_users
Revises: 002_inventory_history
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "003_users"
down_revision: Union[str, None] = "002_inventory_history"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(length=120), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("rol", sa.String(length=50), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.create_index("ix_usuarios_username", "usuarios", ["username"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_usuarios_username", table_name="usuarios")
    op.drop_table("usuarios")
