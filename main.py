# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db import init_db, close_db
from routes import auth,profile

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(
    title="FitMind AI Backend",
    description="Backend API for FitMind AI utilizing MongoDB and FastAPI",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", tags=["Root"])
async def home():
    return {"message": "Welcome to FitMind AI Backend!"}

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile.router)