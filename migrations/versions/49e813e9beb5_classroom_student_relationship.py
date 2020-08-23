"""empty message

Revision ID: 49e813e9beb5
Revises: 418ece006925
Create Date: 2020-08-23 01:55:24.189492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49e813e9beb5'
down_revision = '418ece006925'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classroom_student',
    sa.Column('classroom_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classroom_id'], ['classroom.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classroom_student')
    # ### end Alembic commands ###