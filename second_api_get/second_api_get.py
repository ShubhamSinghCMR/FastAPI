import fastapi
import uvicorn
from typing import Optional

api=fastapi.FastAPI()

# Default value
@api.get('/api/calculate')
def calculator():
    value= 54
    return {
        'value' : value,
    }

# User Input
@api.get('/api/sum')
def sum(x:int, y:int, z:Optional[int]=1):
    if z==0:
        return fastapi.responses.JSONResponse(
            content="{'error': 'z is zero'}"
            )
    
    value=(x+y)/z
    
    return {
        'sum':value,
    }

uvicorn.run(api)