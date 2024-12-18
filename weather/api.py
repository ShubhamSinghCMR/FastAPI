from pydantic import BaseModel
from fastapi import FastAPI, responses, Depends
import uvicorn
from typing import Optional
import requests

# Pydantic Schema
class WeatherInput(BaseModel):
    city: str
    state: Optional[str]
    country: Optional[str]
    units: Optional[str]

app = FastAPI()

# Dependency function to extract query parameters and return WeatherInput
def get_weather_input(city: str, state: Optional[str] = 'Delhi', country: Optional[str] = 'India', units: Optional[str] = 'Imperial') -> WeatherInput:
    return WeatherInput(city=city, state=state, country=country, units=units)

# Function to fetch weather data from Open-Meteo API
def get_weather_data(city: str):
    url = f'https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current_weather=true'
    
    try:
        response = requests.get(url, verify=False)  # Disabling SSL verification for testing
        if response.status_code == 200:
            return response.json()  # Returns the weather data in JSON format
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    return None  # If no data found

# API to get weather data
@app.get('/weather/{city}')
def get_weather_info(weather_input: WeatherInput = Depends(get_weather_input)):
    weather_data = get_weather_data(weather_input.city)
    
    if weather_data:
        return responses.JSONResponse(weather_data) 
    else:
        return {"error": "Weather data not found"}

if __name__ == '__main__':
    uvicorn.run(app)
