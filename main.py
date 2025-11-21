from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
# from app.db.database import engine
# from app.db.models import Base
# from app.routers.users import router as users_router
# from app.routers.pomodoros import router as pomodoros_router
# from app.routers.logs import router as logs_router
# from app.db.seed_pomodoros import seed_pomodoros


app = FastAPI()

# Base.metadata.create_all(bind=engine)

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

# app.include_router(users_router)
# app.include_router(pomodoros_router)
# app.include_router(logs_router)
