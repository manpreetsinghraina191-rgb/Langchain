from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    age:Optional[int]=Field(None,description="The age of the student, which is optional and can be None if not provided")
    name: str=Field(...,description="The full name of the student")
    email: EmailStr=Field(...,description="The email address of the student")
    cgpa: float=Field(...,ge=0.0,le=4.0,description="The CGPA of the student on a scale of 0.0 to 4.0")


new_student={'name':'Nitish Singh','email':'manpreer@gmail.com','cgpa':3.8}
student=Student(**new_student)
print(student)