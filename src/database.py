from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from typing import Generator

SQLITE_URL = "sqlite:///./notes.db"
# POSTGRES_URL = "postgresql://user:pass@localhost/notes_db"

DATABASE_URL = os.getenv("DATABASE_URL", SQLITE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()