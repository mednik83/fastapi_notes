from slugify import slugify
from sqlalchemy.orm import Session

from src.models import Note

def create_unique_slug(db: Session, title: str, exclude_id: int = None) -> str:
    base_slug = slugify(title, separator="-")[:100]
    slug = base_slug
    
    counter = 1
    while True:
        existing = db.query(Note).filter(Note.slug == slug)
        if exclude_id:
            existing = existing.filter(Note.id != exclude_id)
        
        if not existing.first():
            return slug
        
        slug = f"{base_slug}-{counter}"
        counter += 1