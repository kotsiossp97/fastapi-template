"""First commit

Revision ID: 904a59c2a1b0
Revises: 
Create Date: 2023-09-11 07:46:31.227816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '904a59c2a1b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ACCOUNTS',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ACCOUNTS_email'), 'ACCOUNTS', ['email'], unique=True)
    op.create_index(op.f('ix_ACCOUNTS_full_name'), 'ACCOUNTS', ['full_name'], unique=False)
    op.create_index(op.f('ix_ACCOUNTS_id'), 'ACCOUNTS', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ACCOUNTS_id'), table_name='ACCOUNTS')
    op.drop_index(op.f('ix_ACCOUNTS_full_name'), table_name='ACCOUNTS')
    op.drop_index(op.f('ix_ACCOUNTS_email'), table_name='ACCOUNTS')
    op.drop_table('ACCOUNTS')
    # ### end Alembic commands ###
