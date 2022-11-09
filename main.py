from fastapi import FastAPI
from create_post import add_post_to_db
from pydantic import BaseModel
import json
import uuid


app = FastAPI()


class Post(BaseModel):
    id: int
    created: str
    content: str


@app.get('/')
def root():
    with open('data.json', "r") as database:
        return json.load(database)


@app.post('/posts')
def create_post(post: Post):
    add_post_to_db(str(uuid.uuid4()), post.created, post.content)
