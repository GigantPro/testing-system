"""Add task.box_solutions

Revision ID: b074ca6fff7e
Revises: 42643050c080
Create Date: 2023-12-11 20:27:55.750626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b074ca6fff7e'
down_revision: Union[str, None] = '42643050c080'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('box_solutions', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'box_solutions')
    # ### end Alembic commands ###
