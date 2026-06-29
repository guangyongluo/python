# 遍历字符串中的每个元素
msg = input("请输入一个字符串：")

for char in msg:
    print(f"元素：{char}")
else:
    print("循环结束了")

# 计算1到100之间的奇数之和
total = 0
for n in range(1, 101):
    if n % 2 != 0:
        total += n
print("1到100之间的奇数之和是：", total)

m = int(input("请输长方形的长度："))
n = int(input("请输入长方形的宽度："))

for j in range(n):
    for i in range(m):
        print("*", end="  ")
    print()  # 换行

# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {j * i}", end="\t")
    print()

while True:
    name = input("请输入用户名")
    password = input("请输入密码")
    if name == "" or password == "":
        print("用户名和密码不能为空！")
        continue
    if (name == "admin" and password == "666888") or (name == "zhangsan" and password == "123456") or (
            name == "lwei" and password == "888666"):
        print("登入成功，进入B站首页")
        break
    else:
        print("用户名密码错误，请重新输入")
