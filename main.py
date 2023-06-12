from fastapi import FastAPI
#from database.dataset import drumDataBase (import database)
from schemas.pokemons import Pokemon,PokemonStats
from routes.pokemon_routes import router as pokemonRouter
# importing the engine and models from the database folder 
from database.connection import engine
from database import models

models.Base.metadata.create_all(bind=engine)
description = """
PokeDex App API helps you do awesome stuff. Well, awesome for those who like Pokemon anyway.


## Users

You will be able to:

* **Get a list of all Pokemons**.
* **Get a Pokemon by its id/name**.
"""
app = FastAPI(title="Pokedex App",
    description=description,
    version="0.0.1",
    contact={
        "name": "Vanny",
        "email": "vannyaspasova@gmail.com",
    })  

app.include_router(pokemonRouter)



#@app.get("/")
#response function:
#def testing():
    #return{"message":"This will be the Pokedex App"}

#I have to create two routes: one for getting all Pokemons, and another for getting Pokemons based on names (this will be in a routes folder)
#I have to upload the csv files to the database - there is a filehandling code on GitHub to help with that - import ONLY ONCE
#For the file import: there should be Two PUT routes which handle the file import - one for Pokemon & one for PokemonStats
#there should be two SQLAlchemy models one for Pokemon and another one for Pokemon Stats 
#Create a folder for the database, create a folder for routes, create a folder for schemas