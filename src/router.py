from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from src.schemas import NoteCreate, NotePatch, NoteResponse
from src.database import get_db
from src.models import Note


router = APIRouter()

@router.get('/notes', response_model=List[NoteResponse])
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes

@router.get('/notes/{note_id}', response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post('/notes', response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):

    db_note = Note(
        title=note.title,
        content=note.content,
        created_at=func.now(),
        updated_at=func.now()
    )
    
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

@router.delete('/notes/{note_id}')
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(db_note)
    db.commit()

    return {"message": "Note deleted"}

@router.patch('/notes/{note_id}', response_model=NoteResponse)
def update_note(note_id: int, note_data: NotePatch, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")   

    update_data = note_data.model_dump(exclude_unset=True) 
    if update_data:
        update_data['updated_at'] = func.now()
        for field, value in update_data.items():
            setattr(db_note, field, value)
            
    db.commit()
    db.refresh(db_note)

    return db_note