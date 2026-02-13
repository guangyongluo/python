# 算术运算符
print("10 + 3 =", 10 + 3)  # 加法
print("10 - 3 =", 10 - 3)  # 减法
print("10 * 3 =", 10 * 3)  # 乘法
print("10 / 3 =", 10 / 3)  # 除法，
print("10 // 3 =", 10 // 3)  # 整除，结果向下取整
print("10 % 3 =", 10 % 3)  # 取模，
print("10 ** 3 =", 10 ** 3)  # 幂运算，10的3次方

# 算术运算符的优先级
print("0.1 + 10 / 3 ** 2 = ", 0.1 + 10 / 3 ** 2)  # 先计算幂运算，再计算除法，最后计算加法


# 赋值运算符
num = 88

print("num =", num)  # 输出num的值

num += 12  # 等价于 num = num + 12
print("num += 12, num =", num)  # 输出num的值

num -= 10  # 等价于 num = num - 10
print("num -= 10, num =", num)  # 输出num的值

num *= 2  # 等价于 num = num * 2
print("num *= 2, num =", num)  # 输出num的值

num /= 2  # 等价于 num = num / 2
print("num /= 2, num =", num)  # 输出num的值

num //= 3  # 等价于 num = num // 3
print("num //= 3, num =", num)  # 输出num的值

num %= 2  # 等价于 num = num % 2
print("num %= 2, num =", num)  # 输出num的值

num **= 2  # 等价于 num = num ** 2
print("num **= 2, num =", num)  # 输出num的值

n = int(input("请输入一个数字："))  # 获取用户输入的字符串，并将其转换为整数
print(f"{n}在10~20之间吗？{10 <= n <= 20}")  # 判断n是否在10到20之间，并输出结果

n = int(input("请输入一个数字："))  # 获取用户输入的字符串，并将其转换为整数
print(f"{n}不在10~20之间吗？{n <= 10 or n >=20}")  # 判断n是否在10到20之间，