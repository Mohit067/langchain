from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'mohit' # defaylt parameter
    age: Optional[int] = None #optinal
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'age': 23, 'email': 'xya@gmail.com', 'cgpa': 5.9}
student = Student(**new_student)

print(type(student)) # <class '__main__.Student'>

# student_dict = dict(studnet) #convert student into a dictnory

# print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)