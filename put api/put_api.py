from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class UserProfile(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    address: Optional[str] = None

# Simulating a database with an in-memory dictionary
fake_db = {
    1:{
        "id": 1,
        "name": "s",
        "email": "string",
        "address": "string"
        }
    }

@app.put("/user/profile/{user_id}")
def update_user_profile(user_id: int, user_profile: UserProfile):
    """
    API to update user profile
    """
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user's profile in the "fake database"
    fake_db[user_id] = user_profile
    return {"message": "User profile updated", "details": user_profile}

uvicorn.run(app)
