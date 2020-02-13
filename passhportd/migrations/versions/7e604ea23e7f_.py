"""empty message

Revision ID: 7e604ea23e7f
Revises: 9757d86a4c2c
Create Date: 2019-11-11 21:59:57.757970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e604ea23e7f'
down_revision = '9757d86a4c2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_passentry_password', table_name='passentry')
    op.drop_index('ix_passentry_salt', table_name='passentry')
    op.alter_column('user', 'sshkeyhash',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.create_index(op.f('ix_user_sshkeyhash'), 'user', ['sshkeyhash'], unique=True)
    op.drop_index('ix_user_comment', table_name='user')
    op.drop_constraint('user_sshkey_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_sshkey_key', 'user', ['sshkey'])
    op.create_index('ix_user_comment', 'user', ['comment'], unique=False)
    op.drop_index(op.f('ix_user_sshkeyhash'), table_name='user')
    op.alter_column('user', 'sshkeyhash',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)
    op.create_index('ix_passentry_salt', 'passentry', ['salt'], unique=False)
    op.create_index('ix_passentry_password', 'passentry', ['password'], unique=False)
    # ### end Alembic commands ###
