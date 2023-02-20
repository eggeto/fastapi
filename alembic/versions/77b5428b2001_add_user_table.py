"""add user table

Revision ID: 77b5428b2001
Revises: 877e67f3ac36
Create Date: 2023-02-20 11:37:25.069094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b5428b2001'
down_revision = '877e67f3ac36'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
