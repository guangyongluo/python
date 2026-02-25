i = 0
while i < 10:
    print("人生苦短，我用Python")
    i+= 1
else:
    print("循环结束了")

total = 0
n = 1
while n <= 100:
    if n % 2 == 0:
        total += n
    n += 1
print("1到100之间的偶数之和是：", total)