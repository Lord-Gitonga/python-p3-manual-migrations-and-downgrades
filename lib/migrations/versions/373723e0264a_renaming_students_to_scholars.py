"""Renaming students to scholars

Revision ID: 373723e0264a
Revises: 791279dd0760
Create Date: 2023-08-28 16:21:07.355175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '373723e0264a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
