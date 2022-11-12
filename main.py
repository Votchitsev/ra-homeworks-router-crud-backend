from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import json

from post import create_or_update
from find_post import find_post
from write_db import write


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Post(BaseModel):
    id: Optional[str]
    created: Optional[int]
    content: str


@app.get('/posts')
def root():
    with open('data.json', "r") as database:
        return json.load(database)


@app.get('/posts/{id}')
def get_post(id):
    with open('data.json', "r") as database:
        data = json.load(database)

        response_post = find_post(id, data)

        return response_post


@app.post('/posts')
def create_or_update_post(post: Post):
    create_or_update(post.id, post.created, post.content)


@app.delete('/posts/{id}')
def delete_post(id):
    with open('data.json', "r+") as database:
        data = json.load(database)
        data["data"].remove(find_post(id, data))

    write(data)

