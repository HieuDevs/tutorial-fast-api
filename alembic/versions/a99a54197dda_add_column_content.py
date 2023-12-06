"""add_column_content

Revision ID: a99a54197dda
Revises: ad3f356e2639
Create Date: 2023-12-05 22:57:26.294033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a99a54197dda"
down_revision: Union[str, None] = "ad3f356e2639"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(name="content", type_=sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", column_name="content")
    pass
