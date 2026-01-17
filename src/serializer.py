from typing import List
from src.models import Note


def serialize_note(note: Note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "slug": note.slug,
        "tags": [tag.title for tag in note.tags],
        "created_at": note.created_at,
        "updated_at": note.updated_at
    }

def serialize_notes(notes: List[Note]) -> List[dict]:
    return [serialize_note(note) for note in notes]