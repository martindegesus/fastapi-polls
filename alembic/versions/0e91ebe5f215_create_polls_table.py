"""create_polls_table

Revision ID: 0e91ebe5f215
Revises: af56144aff9b
Create Date: 2021-10-12 01:21:08.206651

"""
import enum
from alembic import op
from pydantic.main import BaseModel
from pydantic.types import StrBytes
import sqlalchemy as sa


class PollType(enum.Enum):
    text = 1
    image = 2

# revision identifiers, used by Alembic.
revision = '0e91ebe5f215'
down_revision = 'af56144aff9b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(PollType), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('polls')
