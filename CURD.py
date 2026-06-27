#initial setup and basic route

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

my_post = [
    {
        "title" : "title of post 1",
        "content" : "Content of post",
        "id" : 1
    },
    {
        "title" : "Favourite Food",
        "content" : "Pizza",
        "id" : 2
    }
]

@app.get("/")
def root():
    return {"message" : "Hello World!!"}

@app.get("/posts")
def get_post():
    return{"data" : my_post}

# Data validation and create post

# Add these to your imports at the top:
from typing import Optional
from random import randrange
from fastapi import status

# Add this schema below app = FastAPI()
class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

# Add this POST route at the bottom
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict ['id'] = randrange(0,100000)
    my_post.append(post_dict)
    return{"data" : post_dict}

# error handling

# Add HTTPException to your fastapi imports at the top:
from fastapi import FastAPI, status, HTTPException

# Add this helper function below your my_post array
def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

# Add this GET route at the bottom
@app.get("/posts/{id}")
def get_post(id : int):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id : {id} was not found")
    return {"post_detail" : post}
