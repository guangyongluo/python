from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    age: int
    sex: str

def work(stu: Student):
    print(stu.name)
    print(stu.age)
    print(stu.sex)

if __name__ == '__main__':
    try:
        s = Student(name="Tom", age=23, sex=[])
    except ValidationError as e:
        print(e.json())