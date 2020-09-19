"""empty message

Revision ID: 89b4aa3e169b
Revises: b732f37b51dc
Create Date: 2020-08-31 11:52:05.412284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89b4aa3e169b'
down_revision = 'b732f37b51dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('absent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'absent')
    # ### end Alembic commands ###