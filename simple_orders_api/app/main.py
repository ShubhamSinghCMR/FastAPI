from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from app.frontend_routes import frontend_router

app = FastAPI()

app.include_router(router)  # API routes
app.include_router(frontend_router)  # Frontend routes

app.mount("/static", StaticFiles(directory="app/static"), name="static")
