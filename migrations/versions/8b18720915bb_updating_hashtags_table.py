"""updating hashtags table

Revision ID: 8b18720915bb
Revises: 
Create Date: 2017-11-12 15:29:28.116719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b18720915bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('hashtags_tweet_id_fkey', 'hashtags', type_='foreignkey')
    op.drop_column('hashtags', 'tweet_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashtags', sa.Column('tweet_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('hashtags_tweet_id_fkey', 'hashtags', 'tweets', ['tweet_id'], ['id'])
    # ### end Alembic commands ###
