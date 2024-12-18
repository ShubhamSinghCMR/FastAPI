from pydantic import BaseModel
from fastapi import FastAPI, responses, Depends
import uvicorn
from typing import Optional
import httpx  # Import httpx for async HTTP requests

# Pydantic Schema
class WeatherInput(BaseModel):
    city: str
    state: Optional[str]
    country: Optional[str]
    units: Optional[str]

app = FastAPI()

# Dependency function to extract query parameters and return WeatherInput
async def get_weather_input(city: str, state: Optional[str] = 'Delhi', country: Optional[str] = 'India', units: Optional[str] = 'Imperial') -> WeatherInput:
    return WeatherInput(city=city, state=state, country=country, units=units)

# Function to fetch weather data from Open-Meteo API asynchronously using httpx
async def get_weather_data(city: str):
    url = f'https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current_weather=true'
    
    async with httpx.AsyncClient(verify=False) as client:  # Set verify=False here
        try:
            response = await client.get(url)  # Perform the async get request
            if response.status_code == 200:
                return response.json()  # Returns the weather data in JSON format
        except httpx.RequestError as e:
            return {"error": str(e)}
    return None  # If no data found

# Async API to get weather data
@app.get('/weather/{city}')
async def get_weather_info(weather_input: WeatherInput = Depends(get_weather_input)):
    weather_data = await get_weather_data(weather_input.city)
    
    if weather_data:
        return responses.JSONResponse(weather_data) 
    else:
        return {"error": "Weather data not found"}

if __name__ == '__main__':
    uvicorn.run(app)
