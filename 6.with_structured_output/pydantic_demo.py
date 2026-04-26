from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str


new_student = {'name' : 'Anupam'}  # the moment i will use any other data type except string (defined above) it will throw an error.   Input should be a valid string [type=string_type, input_value=32, input_type=int]

student = Student(**new_student)

print(student)

# Set default Value
class Dog(BaseModel):
    name: str = "Kafka"  # set default values

new_dog = {}

dog = Dog(**new_dog)

print(dog.name)

#Set optional value
class Cat(BaseModel):
    name: str
    age: Optional[int] = None

new_cat = {'name' : 'Billa'}

cat = Cat(**new_cat)

print(cat)

#Coerce - Smart data type conversion - Here we used age as string in the new_cat variable but it converts string into integer
class MyCat(BaseModel):
    name: str = "Billa"
    age: Optional[int] = None

new_cat = {'age' : '32'}

mycat = MyCat(**new_cat)

print(mycat)

#Email Validation - In case email structure is not correct it will raise it.
class MyCat1(BaseModel):
    name: str = "Billa"
    age: Optional[int] = None
    email:EmailStr

new_cat = {'age' : '32', 'email' : 'abc@gmail.com'}

mycat1 = MyCat1(**new_cat)

print(mycat1)

#Constraints - in case cgpa will be outside of defined range then it will raise an error we can also use default values, description, regex or expressions etc.
class MyStudent(BaseModel):
    name: str
    cgpa: float = Field(gt = 0, lt = 10)


new_student = {'name' : 'Anupam', 'cgpa' : 5}  # the moment i will use any other data type except string (defined above) it will throw an error.   Input should be a valid string [type=string_type, input_value=32, input_type=int]

student = MyStudent(**new_student)

student_dict = dict(student) #Explicit conversion from pydantic object to python dict
student_json =student.model_dump_json() #Can convert into json

print(student)
print(student_dict['cgpa'])
print(student_json)

