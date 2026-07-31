def ask(name = "bobby"):
    print(name)

class Person:
    def __init__(self):
        print("bobby1")

my_func = ask
my_func("bobby")

my_class = Person
my_class()

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for obj in obj_list:
    print(obj())

def decorator_func():
    print("dec start")
    return ask

my_ask = decorator_func()
my_ask("Tom")