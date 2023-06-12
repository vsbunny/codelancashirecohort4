from fastapi import APIRouter, Depends, File, UploadFile
from schemas.pokemons import Pokemon, PokemonResponseModel, PokemonStats, PokemonStatsRepsonseModel
from database.models import Pokemon as PokemonTable 
from database.models import PokemonStats as PokemonStatsTable
import csv
from database.connection import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/pokemons",tags=["PokeDex App"]) 
#router.get and router.put etc... 

#Upload the PokemonData File First; UploadFile=File(...) db:Session=Depends(get_db) is the connection to PostgreSQL
@router.post("/uploadPokemonData")
def uploadPokemonData(file: UploadFile = File(...), db: Session=Depends(get_db)):
    # extract data from file
    fileContent = file.file.read().decode("utf-8")
    
    # convert data to rows using csv module. Its a built in module in python
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
  
    # skip the first row as it contains the column names
    next(rows)

    # iterate over the rows and add them to the database
    for row in rows:
        # uncomment the line below and see the output in terminal it should show you the data in each row (list of rows)
        print(row)

        # add the row to the database. Remember the sequence of the data in the row matters
        # we will create a bulk insert to avoid performance issue and also to avoid multiple commits
        # on the first iteration of the loop
        # row[0] means first row first column cell. We skipped the first row as it contains the column names
        # row[1] means first row second column cell so on and so forth
        # on next iteration of the loop row[0] will be second row first column cell and so on and so forth
        pokemon = PokemonTable(classification=row[1], name=row[3], type1=row[5], type2=row[6], generation=row[7])
        # here we are adding the pokemon object to the database session and not to the database itself
        db.add(pokemon)
    
    # commit the changes to the database which will insert the data into the database 
    db.commit()
    return{"message":"The file has been uploaded"}
    # check the result in the database using pgadmin

#Upload PokemonStats to the database; logic, same as above
@router.post("/uploadPokemonStats")
def uploadPokemonStats(file: UploadFile=File(...), db: Session=Depends(get_db)):
    # the process is similar to the above function
    # extract data from file
    fileContent2 = file.file.read().decode("utf-8")
    
    # convert data to rows using csv module. Its a built in module in python
    rows = csv.reader(fileContent2.splitlines(), delimiter=",")
  
    # skip the first row as it contains the column names
    next(rows)

     # iterate over the rows and add them to the database
    for row in rows:
        # uncomment the line below and see the output in terminal it should show you the data in each row (list of rows)
        print(row)

        # add the row to the database. Remember the sequence of the data in the row matters
        # we will create a bulk insert to avoid performance issue and also to avoid multiple commits
        # on the first iteration of the loop
        # row[0] means first row first column cell. We skipped the first row as it contains the column names
        # row[1] means first row second column cell so on and so forth
        # on next iteration of the loop row[0] will be second row first column cell and so on and so forth
        # on some rows, there are missing values for height and weight. we need to make sure to handle these edge cases as well
        # we are using the if condition to check if the value is present or not. If it is present then we are using it else we are using None
        # To accepts None values, we need to make sure that the column in the database is nullable
        # I have made the height_m and weight_kg columns nullable in the models.py and also changed their data type to Float
        # To migrate a new table with nullable columns, we need to drop the table and then create it again
        # To drop the table, we need to go to pgadmin and drop the table manually by right clicking on the table and selecting Delete/Drop

        pokemonStats = PokemonStatsTable(pokemon_id=row[0], height_m=row[26] if row[26] else None, weight_kg=row[31] if row[31] else None, attack=row[19])
        # here we are adding the pokemon object to the database session and not to the database itself
        db.add(pokemonStats)
    
    # commit the changes to the database which will insert the data into the database 
    db.commit()
    return{"message":"The file has been uploaded!"}
    # check the result in the database using pgadmin

#to get all pokemons
#Thinking the Pokemon Response_model should be a dictionary, so can see both pokemondata + pokemonStats
#@router.get("/", response_model=list[DrumResponseModel])
#def getDrums(db: Session = Depends(get_db)): #get the data from the database
    #drums = db.query(DrumTableModel).all() #queries the database, the SQL syntax is SELECT * from...
    #return{"data": drums} #return it as object
    #return drums #we are modifying the response model here to a list instead of a dictionary

#dynamic end-point - example of using a dumy database defined on top; to get a specific pokemon by name
#@router.get("/{drumName}")
#def getSpecificDrum(drumName: str, db: Session = Depends(get_db)):
    #return {"whateveryoupassedafterdrums": drumName}
    #for drum in drumDataBase:
        #if drum["name"] == drumName.lower(): #put in lowecase to make case sensitive, the database is in lower case
            #return drum #whichever element matches in the database, return that name. 
#the query below lists any drums corresponding to the input - if there are any matching letters e.g. 'sur' it will display surdo1, etc. basically if anything is like the name of the drum, it will display it
    #drum = db.query(DrumTableModel).filter(DrumTableModel.title.ilike(f"%{drumName}%")).first()
    #if drum: #if there is a record, return the data for that drum
        #return {"data":drum}
    #return {"message": "Found nothing!"}