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


# Part 2: Implemented GET route to fetch posts from database.
@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute("""SELECT * FROM "Post"."Post" WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, 
                             detail = f"post with id : {id} was not found")
    return {"post_detail" : post}

# Part 3: Added POST route to insert new records into the database.
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    cursor.execute("""INSERT INTO "Post"."Post" (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
        (post.title, post.content, post.published)
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


# Part 4: Added DELETE route to remove records from the database.
@app.delete("/posts/{id}")
def delete_post(id : int):
    cursor.execute("""DELETE FROM "Post"."Post" WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id {id} does not exit")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
