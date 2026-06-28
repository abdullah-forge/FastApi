# Part 1: Initialized FastAPI setup and PostgreSQL database connection.
import psycopg2
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import time
from psycopg2.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Admin123',
            port='5432',
            cursor_factory = RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful!!")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error : ",error)
        time.sleep(2)
