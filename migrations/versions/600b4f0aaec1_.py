"""empty message

Revision ID: 600b4f0aaec1
Revises: 
Create Date: 2020-02-24 00:18:33.579752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '600b4f0aaec1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Actor')
    op.drop_table('Movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Movies',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Movies_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('release_date', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Movies_pkey')
    )
    op.create_table('Actor',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Actor_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Actor_pkey')
    )
    # ### end Alembic commands ###
