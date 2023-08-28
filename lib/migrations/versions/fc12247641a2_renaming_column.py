"""Renaming column

Revision ID: fc12247641a2
Revises: 373723e0264a
Create Date: 2023-08-28 16:49:23.520956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc12247641a2'
down_revision = '373723e0264a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name='students',
        column_name='name',
        new_column_name='jina',
        existing_nullable=True 
    )
    pass


def downgrade() -> None:
    op.alter_column(
        table_name='students',
        column_name='jina',
        new_column_name='name',
        existing_nullable=True
    )
    pass
