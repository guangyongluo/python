# 常见数据类型
print("Hello")
print(type("Hello"))

print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num = -100
print(type(num))

print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, complex))

s1 = "Hello World"
s2 = 'Hello World'
s3 = """
尊敬的客户：
    感谢您选择我们公司的产品。
    我们将会为您服务。
"""

s4 = 'It\'s very interesting'
s5 = "It's very interesting"

s6 = "欢迎大家进入到python课堂学习！\n大家记得一键三连哦~"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# 字符串拼接
s1 = "人生苦短" "我用Python"
print(s1)

s2 = "人生苦短" + "我用Python"
print(s2)

msg1 = "人生苦短"
msg2 = "我用Python"
print("龟叔说：" + msg1 + "," + msg2) # print函数默认使用空格分隔多个参数

# 字符串格式化方式一
name = "龟叔"
age = 18
print("我的名字是%s, 我的年龄是%d" % (name, age))

# 字符串格式化方式二
print("我的名字是{}, 我的年龄是{}".format(name, age))

# 字符串格式化方式三 (Python 3.6+)
print(f"我的名字是{name}, 我的年龄是{age}")
