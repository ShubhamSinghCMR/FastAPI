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
    1: {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "address": "123 Main St"
    }
}

@app.delete("/user/profile/{user_id}")
def delete_user_profile(user_id: int):
    """
    API to delete a user profile
    """
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete the user's profile from the "fake database"
    del fake_db[user_id]
    return {"message": "User profile deleted"}

if __name__ == "__main__":
    uvicorn.run(app)
