from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model for a student
class Student(BaseModel):
    id: int
    name: str
    last_name: str
    age: int
    major: str

# Sample data store
students_db = {}

# Create a new student
@app.post("/students/")
async def create_student(student: Student):
    students_db[student.id] = student
    return student

# Get a student by ID
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return students_db.get(student_id)

# Update a student by ID
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    if student_id in students_db:
        students_db[student_id] = student
        return student
    else:
        return {"error": "Student not found"}

# Delete a student by ID
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id in students_db:
        del students_db[student_id]
        return {"message": "Student deleted successfully"}
    else:
        return {"error": "Student not found"}

# Get all students
@app.get("/students/")
async def get_all_students():
    return students_db
