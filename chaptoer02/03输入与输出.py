name = input("请输入你的名字：")
print("你好，" + name + "！")

age = input("请输入你的年龄：")
print("你的年龄是：" + age)

num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

print("两个数字的和是：" + str(float(num1) + float(num2))) # input函数获取的输入都是字符串类型，需要转换为数值类型才能进行数学运算