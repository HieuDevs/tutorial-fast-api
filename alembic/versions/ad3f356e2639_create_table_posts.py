"""create_table_posts

Revision ID: ad3f356e2639
Revises:
Create Date: 2023-12-05 22:42:36.276787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ad3f356e2639"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Integer,
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            "title",
            sa.String,
            nullable=False,
        ),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
