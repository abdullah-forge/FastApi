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
