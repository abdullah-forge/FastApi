#Initial FastAPI project setup with PostgreSQL database connection
#database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Admin123@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      
#main.py
from fastapi import FastAPI
from .database import engine
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

#models.py
from .database import Base


  
