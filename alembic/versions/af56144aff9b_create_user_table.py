"""create_user_table

Revision ID: af56144aff9b
Revises: 
Create Date: 2021-10-12 00:10:35.095699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af56144aff9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),

    )


def downgrade():
    op.drop_table('users')
