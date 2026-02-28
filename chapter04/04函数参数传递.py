# 函数的传参方式
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 传递方式一：位置参数
reg_stu("张三", 18, "男", "北京")

# 传递方式二：关键字参数
reg_stu(name="李四", age=20, gender="女", city="上海")
reg_stu(age=38, gender="男", city="北京", name="李四")  # 关键字参数的顺序可以任意

# 传递方式三：混合参数（位置参数和关键字参数混合使用）
reg_stu("王五", 28, gender="男", city="广州")  # 位置参数必须在关键字参数之前

# 传递方式四：默认参数
def reg_stu(name, age, gender, city="北京"):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

reg_stu("赵六", 18, "男")  # 使用默认参数，city默认为"北京"
reg_stu("赵六", 18, "男", "上海")  # 使用默认参数，但传递了city参数，覆盖了默认值

# 定义不定长参数的函数 --》 位置不定长参数，传递的所有匹配的位置参数都会被收集到一个元组中，args是一个元组，包含了所有传递的位置参数
def calc_data(*args, **kwargs):
    """
    计算传递的所有数字的最小值、最大值和平均值，并返回一个包含这三个值的元组
    :param args: 位置不定长参数，传递的所有匹配的位置参数都会被收集到一个元组中，args是一个元组，包含了所有传递的位置参数
    :param kwargs: 关键字不定长参数，传递的所有匹配的关键字参数都会被收集到一个字典中，kwargs是一个字典，包含了所有传递的关键字参数
        round: 保留小数的位数
        print: 是否打印结果
    :return: 包含最小值、最大值和平均值的元组
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值：{min_data}，最大值：{max_data}，平均值：{avg_data}")

    return min_data, max_data, avg_data

print(calc_data(2,7,9,10,45))

print(calc_data(2,7,9,10,45, round=2))

print(calc_data(2,7,9,10, round=2, print=True))


