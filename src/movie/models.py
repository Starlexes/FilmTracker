from sqlalchemy import MetaData, String, Integer, Table, Column, ForeignKey, DateTime, event

from src.utils import auto_generate_slug

metadata = MetaData()

movie_director_association = Table(
    'movie_director',
    metadata,
    Column('movie_id', Integer, ForeignKey('movie.id'), primary_key=True),
    Column('director_id', Integer, ForeignKey('director.id'), primary_key=True)
)

movie_genre_association = Table(
    'movie_genre',
    metadata,
    Column('movie_id', Integer, ForeignKey('movie.id'), primary_key=True, nullable=False),
    Column('genre_id', Integer, ForeignKey('genre.id'), primary_key=True, nullable=False)
)

movie = Table(
    'movie',
    metadata,
    Column('id', Integer, primary_key=True, index=True, nullable=False),
    Column('slug', String, unique=True, index=True, nullable=False),
    Column('name', String, unique=True, index=True, nullable=False),
    Column('description', String, nullable=False),
    Column('rate', Integer, index=True, nullable=False),
    Column('release', DateTime, nullable=False),
    Column('preview', String, nullable=False)
)

screenshot = Table(
    'screenshot',
    metadata,
    Column('id', Integer, primary_key=True, index=True, nullable=False),
    Column('image_url', String, unique=True, nullable=False),
    Column('movie_id', Integer, ForeignKey('movie.id'), index=True, nullable=False)
)

director = Table(
    'director',
    metadata,
    Column('id', Integer, primary_key=True, index=True, nullable=False),
    Column('slug', String, unique=True, index=True, nullable=False),
    Column('name', String, index=True, unique=True, nullable=False)
)   

genre = Table(
    'genre',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False, index=True),
    Column('slug', String, unique=True, index=True, nullable=False),
    Column('title', String, unique=True, nullable=False, index=True)
)