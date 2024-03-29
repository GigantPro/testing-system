"""Add tasks.build_output

Revision ID: 541129cddab6
Revises: 32beecc394c0
Create Date: 2023-12-07 22:34:04.035051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '541129cddab6'
down_revision: Union[str, None] = '32beecc394c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('build_output', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'build_output')
    # ### end Alembic commands ###
