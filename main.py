from random import randrange
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

post_data = [
    {
        "title": "best restaurent to visit",
        "content": "top places to visit in florida",
        "id": 1,
    },
    {
        "title": "best beaches to visit",
        "content": "top beaches to visit in Goa",
        "id": 2,
    },
]


def find_post_id(id):
    for post in post_data:
        if post.get("id") == id:
            return post


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Hello API Development is going on"}


@app.get("/posts")
def get_posts():
    return {"message": "this is your post"}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 100000)
    post_data.append(post_dict)
    return {"data": post_data}


@app.get("/posts/latest")
def get_latest_post():
    post = post_data[len(post_data)-1]
    print(post)
    return {"data": post}


@app.get("/posts/{id}")
def get_post(id: int):
    print(type(id))
    post = find_post_id(id)
    print(post)
    return {"data": post}
