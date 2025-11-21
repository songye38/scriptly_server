from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


# ====== Base ======
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class StudyQuestionBase(BaseModel):
    question: str
    answer_title: str
    answer_content: str


class NoteBase(BaseModel):
    title: str


class PostBase(BaseModel):
    title: str
    content: str


# ====== Create ======
class ProjectCreate(ProjectBase):
    pass


class StudyQuestionCreate(StudyQuestionBase):
    project_id: UUID


class NoteCreate(NoteBase):
    project_id: UUID


class PostCreate(PostBase):
    project_id: UUID


# ====== Response ======
class StudyQuestion(NoteBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class NoteQuestion(BaseModel):
    id: UUID
    note_id: UUID
    question_id: UUID

    class Config:
        orm_mode = True


class Note(NoteBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class Project(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    study_questions: List[StudyQuestion] = []
    notes: List[Note] = []
    posts: List[Post] = []

    class Config:
        orm_mode = True
