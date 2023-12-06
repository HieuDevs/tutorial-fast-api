"""add foreign-key to post table

Revision ID: bc35957dd16a
Revises: db1401b46b3c
Create Date: 2023-12-05 23:12:15.549110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bc35957dd16a"
down_revision: Union[str, None] = "db1401b46b3c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("owner_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", "posts")
    op.drop_column("posts", "owner_id")
    pass
