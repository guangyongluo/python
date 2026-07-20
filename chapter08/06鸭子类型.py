class Duck:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.name} 正在游泳...")

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.name} 正在游泳...")

class Pig:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.name} 正在游泳...")

def go_swimming(duck: Duck):
    duck.swimming()

if __name__ == '__main__':
    go_swimming(Duck("小鸭子", 1))
    go_swimming(Dog("小狗", 2))
    go_swimming(Pig("小猪", 3))