#Connection to Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection string: 
SQLALCHEMY_DATABASE_URL = "postgresql://vsbunny:ZVh8hXgem8i1vEOqhCbHnh1epuGwh5el@dpg-chueorndvk4olip46pkg-a.frankfurt-postgres.render.com/pokedex_crap"
#Session Engine - this is what connects the ORM to the database 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Each of the SQLAlchemy models/classes inherit the Base class below 
Base = declarative_base()
#Dependency Function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()