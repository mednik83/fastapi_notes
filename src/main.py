import json
import os
from fastapi import FastAPI

from src.config import DATA_PATH
from src.router import router as notes_router

if not os.path.exists(DATA_PATH):
    with open(DATA_PATH, 'w') as f:
        json.dump([], f)

app = FastAPI()

app.include_router(notes_router)