"""adding name column

Revision ID: df0e7ae3ed9a
Revises: 62c7ce54d03c
Create Date: 2025-01-11 11:58:19.457366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df0e7ae3ed9a'
down_revision = '62c7ce54d03c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
