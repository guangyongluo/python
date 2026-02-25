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
