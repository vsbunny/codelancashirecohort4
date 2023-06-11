#ORM method (SQLAlchemy) instead of creating the database on PostgreSQL; every model represents a table, in this case, obviously we have two tables - Pokemon (Dataset) and Pokemon Stats
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database.connection import Base #Because all SQLAlchemy models/classes will inherit Base

class Pokemon(Base):
    __tablename__ = "Pokemon" #__tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models

    id = Column(Integer, primary_key=True, index=True) #each of the attributes represent columns
    #drums = relationship("Drum", backref="owner")
    classification = Column(String,  index=True)
    name = Column(String,  index=True)
    type1 = Column(String, index=True)
    type2 = Column(String, index=True)
    generation = Column(Integer, index=True)
    
class PokemonStats(Base):
    __tablename__ = "Pokemon_stats"

    pokemon_id = Column(Integer, primary_key=True, index=True)
    height_m = Column(Float, index=True)
    weight_kg = Column(Float, index=True)
    attack = Column(Integer, index=True)
     

