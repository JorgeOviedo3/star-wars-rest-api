"""empty message

Revision ID: 554a2978106c
Revises: 3590630e2e62
Create Date: 2022-10-28 15:31:51.127084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '554a2978106c'
down_revision = '3590630e2e62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('terrain', sa.String(length=120), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###