"""add language to posts

Revision ID: 482e77b3c162
Revises: 6c6fb61e314f
Create Date: 2024-09-02 16:12:59.959058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '482e77b3c162'
down_revision = '6c6fb61e314f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###