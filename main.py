from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from create_post import add_post_to_db
from pydantic import BaseModel
import json
import uuid


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Post(BaseModel):
    created: int
    content: str

def find_post(id, data):
    return [post for post in data["data"] if post["id"] == id][0]


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
def create_post(post: Post):
    add_post_to_db(str(uuid.uuid4()), post.created, post.content)


@app.delete('/posts/{id}')
def delete_post(id):
    with open('data.json', "r+") as database:
        data = json.load(database)
        data["data"].remove(find_post(id, data))

    with open("data.json", "w"):
        pass

    with open("data.json", "w") as database:
        json.dump(data, database, indent=4)
