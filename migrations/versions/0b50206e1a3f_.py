"""empty message

Revision ID: 0b50206e1a3f
Revises: 
Create Date: 2021-05-16 10:17:22.709354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0b50206e1a3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    # ### end Alembic commands ###