from fastapi import FastAPI

from src.router import router as notes_router
from src.models import Base
from src.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Notes API")

app.include_router(notes_router, prefix="/api", tags=["notes"])

@app.get("/")
def root():
    return {"message": "Notes API is running!", "docs": "/docs"}