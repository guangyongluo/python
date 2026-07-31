a = 1
b = "abc"

print(type(1))
print(type(int))
print(type(b))
print(type(str))

class Student:
    pass

class MyStudent(Student):
    pass

stu = Student()
print(type(stu))
print(type(MyStudent))
print(int.__base__)
print(str.__base__)
print(Student.__base__)
print(MyStudent.__base__)
print(type.__base__)
print(object.__base__)
print(type(object))
