# 函数的参数类型

# 普通参数： 数字、字符串、列表、元组、字典等
# 特殊参数： 函数也是一种对象，可以作为参数传递给另一个函数

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "除数不能为零"
    return x / y

def calculate(x, y, operation):
    return operation(x, y)

result = calculate(10, 5, add)
print("10 + 5 =", result)

result = calculate(10, 5, subtract)
print("10 - 5 =", result)

result = calculate(10, 5, multiply)
print("10 * 5 =", result)

result = calculate(10, 5, divide)
print("10 / 5 =", result)