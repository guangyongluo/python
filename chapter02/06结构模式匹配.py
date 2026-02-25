# 结构匹配模式
day = int(input("请输入一个数字，代表星期几（1-7）："))

match day:
    case 1:
        print("今天是星期一")
    case 2:
        print("今天是星期二")
    case 3:
        print("今天是星期三")
    case 4:
        print("今天是星期四")
    case 5:
        print("今天是星期五")
    case 6:
        print("今天是星期六")
    case 7:
        print("今天是星期日")
    case _: # 匹配其他所有的情况
        print("输入的数字不合法，请输入1-7之间的数字")


# 带条件的结构匹配模式
num1 = float(input("请输入一个数字："))
num2 = float(input("请输入另一个数字："))
operator = input("请输入运算符（+、-、*、/）：")

match operator:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case "/" if num2 == 0:
        print("除数不能为零")
    case _:
        print("不支持的运算符")

