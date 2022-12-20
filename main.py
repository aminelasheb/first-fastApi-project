from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort:Optional[str] = None):
    if published:
        s = str(limit) + " published blogs from list"
        return {"data": s}
    else:
        s = str(limit) + " not published blogs from list"
        return {"data": s}


@app.get("/blog/unpublished")
def unpablished():
    return {"items": {'1', '2', '3'}}


@app.get("/blog/{id}")
def show(id: int):
    return {"item_id": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {'1', '2'}}

class Blog(BaseModel):
    title: str
    body:str
    published:Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return blog


