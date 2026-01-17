from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str
    tags: List[str] = []

class NoteCreate(NoteBase):
    title: str  
    content: str
    tags: List[str] = []

class NotePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None

class TagBase(BaseModel):
    title: str