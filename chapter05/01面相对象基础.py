# 定义类
class Car:
    pass

# 创建对象
car = Car()
# 给对象添加属性 -- 不推荐动态添加属性，应该在类中定义属性

car.color = 'red'
car.brand = 'BMW'
car.name = 'X5'
car.price = 800000

print(car)
# 会将对象的属性以字典的形式输出
print(car.__dict__)
# 通过对象访问属性
print(car.brand)

class Car:

    # 定义类属性，所有对象共享的属性
    wheels = 4

    # 定义实例属性，只有当前对象拥有的属性
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price

    def __str__(self):
        return f"Car(color={self.color}, brand={self.brand}, name={self.name}, price={self.price})"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.price < other.price
        return False

    def running(self):
        print(f"{self.name} is running...")

    def total_price(self, discount=0.0, rate=0.1):
        return self.price * discount + rate * self.price


car1 = Car("red", "BMW", "X5", 800000)
print(car1.__dict__)

print(car1)

car2 = Car("red", "BMW", "X5", 800001)

print(car1 == car2) # True
print(car1 > car2)