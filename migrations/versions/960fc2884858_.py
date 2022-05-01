"""empty message

Revision ID: 960fc2884858
Revises: 
Create Date: 2021-11-24 13:27:25.846625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960fc2884858'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('friend_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('friendstatus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['status_id'], ['friends.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('postalcode', sa.String(length=120), nullable=False),
    sa.Column('about', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('postalcode', sa.String(length=120), nullable=False),
    sa.Column('about', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    op.drop_table('info')
    op.drop_table('friendstatus')
    op.drop_table('user')
    op.drop_table('friends')
    # ### end Alembic commands ###