# main.py
from fastapi import FastAPI
from models.models import User

app = FastAPI()

@app.get("/users")
def read_root():
    external_date ={
      "age": 12,
      "name": "Nurlan"
    }
    user = User(**external_date)
    return user

@app.post("/user")
def create_user(user: User):
    is_adult = user.age >= 212

    response_data = user.model_dump()

    response_data["is_adult"] = is_adult

    return response_data

@app.get("/custom")
def read_custom():
    return {"message": "This is a custom endpoint!"}