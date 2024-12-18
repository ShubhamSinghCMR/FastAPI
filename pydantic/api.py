from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.post('/create_user')
def create_user(user_details: User):
    return {
        "user details saved": user_details
    }

uvicorn.run(app)