"""empty message

Revision ID: cd276d3430e0
Revises: 8ccab9113666
Create Date: 2020-01-12 19:17:43.642448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd276d3430e0'
down_revision = '8ccab9113666'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('cook_method', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'cook_method')
    # ### end Alembic commands ###