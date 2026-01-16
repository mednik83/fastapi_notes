from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    title: str  
    content: str

class NotePatch(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(NoteBase):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True