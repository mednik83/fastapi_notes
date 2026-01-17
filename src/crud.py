from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from src.models import Note, Tag, note_tags
from src.schemas import NoteCreate, NotePatch
from src.utils import create_unique_slug

def get_or_create_tag(db: Session, tag_title: str) -> Tag:
    tag = db.query(Tag).filter(Tag.title == tag_title).first()
    if not tag:
        tag = Tag(title=tag_title)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag

def get_note_by_slug(db: Session, slug: str):
    return db.query(Note).filter(Note.slug == slug).first()

def get_notes_by_tag(db: Session, tag_title: str):
    return db.query(Note).join(note_tags).join(Tag).filter(Tag.title == tag_title).all()

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        title=note.title,
        content=note.content,
        slug=create_unique_slug(db, note.title),
        created_at=func.now(),
        updated_at=func.now()
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    for tag_title in note.tags:
        tag = get_or_create_tag(db, tag_title)
        db_note.tags.append(tag)

    db.commit()

    return db_note

def update_note(db: Session, note_id: int, note_data: NotePatch):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        return None
    
    update_dict = note_data.model_dump(exclude_unset=True)
    update_dict['updated_at'] = func.now()

    for field, value in update_dict.items():
        setattr(db_note, field, value)

    db.commit()
    db.refresh(db_note)

    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    return False
