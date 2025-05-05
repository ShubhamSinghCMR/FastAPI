"""Initial tables

Revision ID: 0c0e8c775e07
Revises:
Create Date: 2025-05-06 02:32:32.106400

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "0c0e8c775e07"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
