"""change value password

Revision ID: 6a7347834dc3
Revises: bb1ec5084cd6
Create Date: 2024-03-10 03:16:44.436438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a7347834dc3'
down_revision: Union[str, None] = 'bb1ec5084cd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=75),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=75),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)
    # ### end Alembic commands ###