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
