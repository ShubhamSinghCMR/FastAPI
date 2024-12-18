from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: Optional[str] = None

class UserProfile(User):
    id: int
    address: Optional[str] = None

app = FastAPI()

@app.post('/user/profile')
def create_user_profile(user_profile : UserProfile):
    return {
        "message": "User profile created",
        "details": user_profile
    }

if __name__=="__main__":
    uvicorn.run (app)