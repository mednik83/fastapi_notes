from sqlalchemy import Column, Integer, String, Table, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database import Base
from sqlalchemy.orm import relationship

note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    slug = Column(String, unique=True, index=True)
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    tags = relationship("Tag", secondary=note_tags, back_populates='notes')

    @property
    def tags_list(self):
        return [tag.title for tag in self.tags]


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)

    notes = relationship("Note", secondary=note_tags, back_populates="tags")