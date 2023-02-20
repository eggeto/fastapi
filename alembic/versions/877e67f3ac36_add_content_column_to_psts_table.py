"""add content column to psts table

Revision ID: 877e67f3ac36
Revises: 25dcc73ba790
Create Date: 2023-02-20 11:20:29.513906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877e67f3ac36'
down_revision = '25dcc73ba790'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False) 
                    )
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
