from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schemas import NoteCreate, NotePatch 
from src.dependencies import get_db
from src import crud
from src.serializer import serialize_note, serialize_notes

router = APIRouter()

@router.get('/notes')
def get_notes(
    tag: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
    ):
    if tag:
        notes = crud.get_notes_by_tag(db, tag)
    else:
        notes = crud.get_notes(db, skip, limit)
    return serialize_notes(notes)

@router.get('/notes/{note_id}')
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return serialize_note(note)

@router.get('/notes/slug/{slug}')
def get_note_by_slug(slug: str, db: Session = Depends(get_db)):
    note = crud.get_note_by_slug(db, slug)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return serialize_note(note)

@router.post('/notes', status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note =  crud.create_note(db, note)
    return serialize_note(new_note)

@router.patch('/notes/{note_id}')
def update_note(note_id: int, note_data: NotePatch, db: Session = Depends(get_db)):
    update_data = crud.update_note(db, note_id, note_data)
    if not update_data:
        raise HTTPException(status_code=404, detail="Note not found")
    return serialize_note(update_data)

@router.delete('/notes/{note_id}')
def delete_note(note_id: int, db: Session = Depends(get_db)):
    success = crud.delete_note(db, note_id)
    if not success: raise HTTPException(404, "Note not found")
    return {"message": "Note deleted"}