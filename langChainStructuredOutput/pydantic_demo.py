from pydantic import BaseModel,EmailStr,Field
from typing  import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,lt= 10,default=5,description="a decimal value representing cgpa of a student")
    
new_student = {"name":"anya","age":'29',"email":"abc@gmail.com"}
student = Student(**new_student)
print(student)
