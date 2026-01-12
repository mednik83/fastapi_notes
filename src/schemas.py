from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteCreate(NoteBase):
    title: str  
    content: str

class NotePut(NoteCreate):
    pass

class NotePatch(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime