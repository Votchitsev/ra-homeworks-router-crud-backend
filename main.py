from fastapi import FastAPI
from create_post import add_post_to_db
from pydantic import BaseModel
import json
import uuid


app = FastAPI()


class Post(BaseModel):
    created: int
    content: str


@app.get('/posts')
def root():
    with open('data.json', "r") as database:
        return json.load(database)


@app.get('/posts/{id}')
def get_post(id):
    with open('data.json', "r") as database:
        data = json.load(database)

        response_post = [post for post in data["data"] if post["id"] == id][0]

        return response_post


@app.post('/posts')
def create_post(post: Post):
    add_post_to_db(str(uuid.uuid4()), post.created, post.content)
