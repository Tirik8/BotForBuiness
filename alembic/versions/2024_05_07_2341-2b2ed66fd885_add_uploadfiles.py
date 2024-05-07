"""add UploadFiles

Revision ID: 2b2ed66fd885
Revises: 04aa8ed15569
Create Date: 2024-05-07 23:41:22.194355

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2b2ed66fd885"
down_revision: Union[str, None] = "04aa8ed15569"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "uplead_files",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("file_idL", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("uplead_files")
    # ### end Alembic commands ###
