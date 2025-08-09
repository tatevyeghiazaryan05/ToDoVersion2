"""Something

Revision ID: e214baad0a1d
Revises: 8f1d33bf9e53
Create Date: 2025-07-04 14:51:33.437567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e214baad0a1d'
down_revision: Union[str, Sequence[str], None] = '8f1d33bf9e53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: set default False for status and archived columns in todo table."""
    op.alter_column('todo', 'status',
                    existing_type=sa.Boolean(),
                    server_default=sa.text('false'),
                    existing_nullable=True)

    op.alter_column('todo', 'archived',
                    existing_type=sa.Boolean(),
                    server_default=sa.text('false'),
                    existing_nullable=True)


def downgrade() -> None:
    """Downgrade schema: remove default values for status and archived columns."""
    op.alter_column('todo', 'status',
                    existing_type=sa.Boolean(),
                    server_default=None,
                    existing_nullable=True)

    op.alter_column('todo', 'archived',
                    existing_type=sa.Boolean(),
                    server_default=None,
                    existing_nullable=True)
