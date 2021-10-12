import datetime
import databases
import sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str

class Poll(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/polls")
async def root():
    return {"polls": "Hello World"}

@app.get("/users")
async def root():
    return {"users": "Hello World"}

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll