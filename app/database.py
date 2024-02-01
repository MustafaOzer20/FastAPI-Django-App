from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

URL_DATABASE = env_vars["URL_DATABASE"]
TABLE_NAME = env_vars["TABLE_NAME"]

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()