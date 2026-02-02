from fastapi import FastAPI
from pydantic import BaseModel

new_app = FastAPI()

class NumbersInput(BaseModel):
    first_number: int
    second_number: int



@new_app.post("/calculate")
async def calculate_sum(data: NumbersInput):
    result = data.first_number + data.second_number
    return {"result": result}