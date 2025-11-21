from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db import models, schemas

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == note.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("/project/{project_id}", response_model=List[schemas.Note])
def get_notes_by_project(project_id: str, db: Session = Depends(get_db)):
    return db.query(models.Note).filter(models.Note.project_id == project_id).all()


@router.delete("/{note_id}")
def delete_note(note_id: str, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"detail": "Note deleted"}
