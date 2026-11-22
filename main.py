from fastapi import FastAPI , HTTPException, Depends,status,Query
from pydantic import BaseModel
from database import engine,Base,get_db
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse
from routers.students import router as student_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router)





