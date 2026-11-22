
from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# CREATE STUDENT
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# GET ALL STUDENTS
@router.get("/")
def get_students(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit

    students = db.query(Student).offset(offset).limit(limit).all()
    total = db.query(Student).count()
    total_pages = (total + limit - 1) // limit

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "students": students
    }


# SEARCH STUDENTS
@router.get("/search", response_model=list[StudentResponse])
def search_students(course: str, db: Session = Depends(get_db)):

    students = db.query(Student).filter(Student.course == course).all()

    return students


# GET STUDENT BY ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found!")

    return student


# UPDATE STUDENT
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    update_student: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found!")

    student.name = update_student.name
    student.age = update_student.age
    student.course = update_student.course

    db.commit()
    db.refresh(student)

    return student


# DELETE STUDENT
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found!")

    db.delete(student)
    db.commit()

    return {"message": "Student Deleted Successfully"}
