from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db.database import engine
from app.db.models import Base

from app.routers.notes import router as notes_router
from app.routers.posts import router as posts_router
from app.routers.projects import router as projects_router
from app.routers.study_questions import router as study_questions_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

#seed_pomodoros()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="", title="My API")

# 허용할 origin 목록
origins = [
    "https://localhost:3000",  # 개발용
    "https://scriptly3.vercel.app/",  # 배포용 메인 도메인
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # 정확히 허용할 도메인만 넣음
    allow_credentials=True,         # 쿠키/토큰 인증용
    allow_methods=["*"],            # 모든 메서드 허용
    allow_headers=["*"],            # 모든 헤더 허용
)

app.include_router(notes_router)
app.include_router(posts_router)
app.include_router(projects_router)
app.include_router(study_questions_router)
