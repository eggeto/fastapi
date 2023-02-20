"""add foreing-key to posts table

Revision ID: 773487af2e6e
Revises: 77b5428b2001
Create Date: 2023-02-20 11:54:14.366289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '773487af2e6e'
down_revision = '77b5428b2001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
                  
                  
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
