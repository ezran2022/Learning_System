"""Moving is_active to user table

Revision ID: 8970367828d9
Revises: 4d2024ded4ff
Create Date: 2022-11-05 23:18:03.318066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8970367828d9'
down_revision = '4d2024ded4ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'is_active')
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.add_column('profiles', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###