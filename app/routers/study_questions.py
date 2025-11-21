from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db import models, schemas

router = APIRouter(prefix="/study-questions", tags=["Study Questions"])


@router.post("/", response_model=schemas.StudyQuestion)
def create_study_question(question: schemas.StudyQuestionCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == question.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db_question = models.StudyQuestion(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


@router.get("/project/{project_id}", response_model=List[schemas.StudyQuestion])
def get_questions_by_project(project_id: str, db: Session = Depends(get_db)):
    return db.query(models.StudyQuestion).filter(models.StudyQuestion.project_id == project_id).all()


@router.delete("/{question_id}")
def delete_question(question_id: str, db: Session = Depends(get_db)):
    q = db.query(models.StudyQuestion).filter(models.StudyQuestion.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(q)
    db.commit()
    return {"detail": "Question deleted"}
