#ORM method (SQLAlchemy) instead of creating the database on PostgreSQL; every model represents a table, in this case, obviously we have two tables - Pokemon (Dataset) and Pokemon Stats
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database.connection import Base #Because all SQLAlchemy models/classes will inherit Base

class Pokemon(Base):
    __tablename__ = "Pokemon" #__tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) #each of the attributes represent columns
    name = Column(String(50))
    classification = Column(String(150))
    type1 = Column(String(50))
    type2 = Column(String(50))
    generation = Column(Integer)
    #1 to 1 relationship with PokemonStats - uselist=False means only one object from PokemonStats is related to an object of Pokemon
    stats = relationship("PokemonStats", backref="pokemon", uselist=False)

class PokemonStats(Base):
    __tablename__ = "Pokemon_stats"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("Pokemon.id"))
    height_m = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)
    attack = Column(Integer, nullable=True)
     

