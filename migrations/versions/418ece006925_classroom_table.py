"""classroom table

Revision ID: 418ece006925
Revises: 4824dbadaad2
Create Date: 2020-08-23 01:19:46.442387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418ece006925'
down_revision = '4824dbadaad2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classroom_external_id'), 'classroom', ['external_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_classroom_external_id'), table_name='classroom')
    op.drop_table('classroom')
    # ### end Alembic commands ###