from sqlalchemy import String, Integer, Table, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database import Base, metadata


movie_director_association = Table(
    'movie_director',
    metadata,
    Column('movie_id', Integer, ForeignKey('movie.id'), primary_key=True),
    Column('director_id', Integer, ForeignKey('director.id'), primary_key=True)
)

movie_genre_association = Table(
    'movie_genre',
    metadata,
    Column('movie_id', Integer, ForeignKey('movie.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genre.id'), primary_key=True)
)

movie_country_association = Table(
    'movie_country',
    metadata,
    Column('movie_id', Integer, ForeignKey('movie.id'), primary_key=True),
    Column('country_id', Integer, ForeignKey('country.id'), primary_key=True)
)

class Movie(Base):
    __tablename__ = 'movie'
    
    id_ = Column(Integer, primary_key=True, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    rate = Column(Integer, index=True, nullable=False)
    release = Column(DateTime, nullable=False)
    preview = Column(String, nullable=False)
    directors = relationship('Director', secondary=movie_director_association, 
                             back_populates='movies', cascade='all, delete-orphan')
    genres = relationship('Genre', secondary=movie_genre_association, 
                          back_populates='movies', cascade='all, delete-orphan')
    countries = relationship('Country', secondary=movie_country_association, 
                          back_populates='movies', cascade='all, delete-orphan')

class Screenshot(Base):
    __tablename__ = 'screenshot'

    id_ = Column(Integer, primary_key=True, index=True, nullable=False)
    image_url = Column(String, unique=True, nullable=False)
    
    movie_id = Column(Integer, ForeignKey('movie.id'), index=True, nullable=False)

    
class Director(Base):
    __tablename__ = 'director'

    id_ = Column(Integer, primary_key=True, index=True, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, unique=True, nullable=False)
    movies = relationship('Movie', secondary=movie_director_association, 
                          back_populates='directors', cascade='all, delete-orphan')

class Genre(Base):
    __tablename__ = 'genre'

    id_ = Column(Integer, primary_key=True, nullable=False, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, unique=True, nullable=False, index=True)
    movies = relationship('Movie', secondary=movie_genre_association, 
                            back_populates='genres', cascade='all, delete-orphan')
    
class Country(Base):
    __tablename__ = 'country'

    id_ = Column(Integer, primary_key=True, nullable=False, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, unique=True, nullable=False, index=True)
    movies = relationship('Movie', secondary=movie_country_association, 
                            back_populates='countries', cascade='all, delete-orphan')