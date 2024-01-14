"""add gender column

Revision ID: 9f4e7e89bdc9
Revises: 6aaa14334cf8
Create Date: 2024-01-13 22:30:26.532158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9f4e7e89bdc9"
down_revision: Union[str, None] = "6aaa14334cf8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("profiles", sa.Column("gender", sa.String(10)))


def downgrade() -> None:
    op.drop_column("profiles", "gender")
