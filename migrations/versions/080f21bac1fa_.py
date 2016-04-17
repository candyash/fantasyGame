"""empty message

Revision ID: 080f21bac1fa
Revises: 43c9a86e3419
Create Date: 2016-04-14 18:24:27.795000

"""

# revision identifiers, used by Alembic.
revision = '080f21bac1fa'
down_revision = '43c9a86e3419'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(length=20), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('knockout', sa.Integer(), nullable=True),
    sa.Column('submission', sa.Integer(), nullable=True),
    sa.Column('decision_score', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.add_column(u'user_info', sa.Column('city', sa.String(length=30), nullable=True))
    op.add_column(u'user_info', sa.Column('country', sa.String(length=30), nullable=True))
    op.add_column(u'user_info', sa.Column('phonenumber', sa.Integer(), nullable=True))
    op.drop_column(u'user_info', 'bio')
    op.drop_column(u'user_info', 'age')
    op.drop_column(u'user_info', 'location')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'user_info', sa.Column('location', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column(u'user_info', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'user_info', sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column(u'user_info', 'phonenumber')
    op.drop_column(u'user_info', 'country')
    op.drop_column(u'user_info', 'city')
    op.drop_table('team')
    ### end Alembic commands ###
