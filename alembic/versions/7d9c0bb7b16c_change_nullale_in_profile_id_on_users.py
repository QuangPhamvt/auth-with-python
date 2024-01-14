"""change nullale in profile_id on users

Revision ID: 7d9c0bb7b16c
Revises: 9f4e7e89bdc9
Create Date: 2024-01-14 01:32:20.995441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7d9c0bb7b16c"
down_revision: Union[str, None] = "9f4e7e89bdc9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users", "profile_id", existing_type=sa.Uuid(), nullable=True)


def downgrade() -> None:
    op.alter_column("users", "profile_id", existing_type=sa.Uuid(), nullable=False)
