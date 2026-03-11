# 捕获异常

try:
    print("=====================")
    print(name)
    print("=====================")
except NameError:
    print("发生了NameError异常，变量name未定义")

try:
    print("=====================")
    print(1 / 0)
    print("=====================")
except NameError:
    print("发生了NameError异常，变量name未定义")
except ZeroDivisionError:
    print("发生了ZeroDivisionError异常，除数不能为零")