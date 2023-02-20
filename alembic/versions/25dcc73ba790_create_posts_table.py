"""create posts table

Revision ID: 25dcc73ba790
Revises: 
Create Date: 2023-02-20 10:58:29.197504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25dcc73ba790'
down_revision = None
branch_labels = None
depends_on = None

#handles the changes
def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)    
                    )
    

#handles the roll back
def downgrade():
    op.drop_table('posts')
