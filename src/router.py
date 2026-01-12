from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException

from src.schemas import NoteCreate, NotePatch, NotePut, NoteResponse
from src.utils import read_json_data, save_to_json_data


router = APIRouter()

@router.get('/notes', response_model=List[NoteResponse])
def get_notes():
    notes = read_json_data()
    return notes

@router.get('/notes/{note_id}', response_model=NoteResponse)
def get_note(note_id: int):
    notes = read_json_data()
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post('/notes', response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate):
    notes = read_json_data()

    new_id = notes[-1]['id'] + 1 if notes else 1
    now = datetime.now().isoformat()
    new_note = {
        'id': new_id,
        **note.model_dump(),
        'created_at': now,
        'updated_at': now
    }
    notes.append(new_note)
    save_to_json_data(notes)
    return new_note

@router.delete('/notes/{note_id}')
def delete_note(note_id: int):
    notes = read_json_data()
    init_len = len(notes)

    notes = [n for n in notes if n['id'] != note_id]

    if len(notes) == init_len:
        raise HTTPException(status_code=404, detail="Note not found")

    save_to_json_data(notes)

    return {"message": "Note deleted"}

@router.put('/notes/{note_id}', response_model=NoteResponse)
def put_note(note_data: NotePut, note_id: int):

    notes = read_json_data()

    for n in notes:
        if n['id'] == note_id:
            n['title'] = note_data.title
            n['content'] = note_data.content
            n['updated_at'] = datetime.now().isoformat()
            save_to_json_data(notes)
            return n

    raise HTTPException(status_code=404, detail="Note not found")

@router.patch('/notes/{note_id}', response_model=NoteResponse)
def update_note(note_id: int, note_data: NotePatch):
    notes = read_json_data()
    
    for n in notes:
        if n["id"] == note_id:
            update_data = note_data.model_dump(exclude_unset=True)
            if not update_data:
                 return n
            n.update(update_data)
            n['updated_at'] = datetime.now().isoformat()
            save_to_json_data(notes)
            return n
            
    raise HTTPException(status_code=404, detail="Note not found")
