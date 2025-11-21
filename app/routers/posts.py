from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db import models, schemas

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == post.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.get("/project/{project_id}", response_model=List[schemas.Post])
def get_posts_by_project(project_id: str, db: Session = Depends(get_db)):
    return db.query(models.Post).filter(models.Post.project_id == project_id).all()


@router.delete("/{post_id}")
def delete_post(post_id: str, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted"}
