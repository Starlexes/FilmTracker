"""Initial

Revision ID: df6965aced80
Revises: 
Create Date: 2024-09-28 18:46:23.012835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df6965aced80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.Column('preview', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    op.create_index(op.f('ix_movie_name'), 'movie', ['name'], unique=False)
    op.create_index(op.f('ix_movie_rate'), 'movie', ['rate'], unique=False)
    op.create_table('screenshot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_screenshot_id'), 'screenshot', ['id'], unique=False)
    op.create_index(op.f('ix_screenshot_image_url'), 'screenshot', ['image_url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_screenshot_image_url'), table_name='screenshot')
    op.drop_index(op.f('ix_screenshot_id'), table_name='screenshot')
    op.drop_table('screenshot')
    op.drop_index(op.f('ix_movie_rate'), table_name='movie')
    op.drop_index(op.f('ix_movie_name'), table_name='movie')
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###