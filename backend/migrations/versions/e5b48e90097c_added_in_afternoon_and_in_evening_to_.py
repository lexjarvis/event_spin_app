"""Added in_afternoon and  in_evening to EventData model

Revision ID: e5b48e90097c
Revises: 50f085af4a1f
Create Date: 2023-07-25 13:45:37.375564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b48e90097c'
down_revision = '50f085af4a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('in_afternoon', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('in_evening', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_data', schema=None) as batch_op:
        batch_op.drop_column('in_evening')
        batch_op.drop_column('in_afternoon')

    # ### end Alembic commands ###