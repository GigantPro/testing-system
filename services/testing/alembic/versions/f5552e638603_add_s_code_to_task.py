"""Add s_code to task

Revision ID: f5552e638603
Revises: 21b654a4c928
Create Date: 2023-12-06 21:55:18.779467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5552e638603'
down_revision: Union[str, None] = '21b654a4c928'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('s_code_for_run', sa.String(), nullable=True))
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=False))
    op.alter_column('tasks', 'code_languge',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'code_languge',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('tasks', 'priority')
    op.drop_column('tasks', 's_code_for_run')
    # ### end Alembic commands ###
