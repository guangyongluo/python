#定义列表
l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# 切面操作
print(l[0:5:1]) # 从索引0开始，切到索引3（不包含3）
print(type(l[0:5:1])) # 切面操作的结果是一个新的列表

print(l[:5:1])
print(l[:5:])
print(l[:5])


print(l[0:5:2])
print(l[0:-2:1])

s = [56, 90, 88, 65, 90, 100, 209, 72, 145, 188]
s.append(145)
print(s)

s.insert(2, 80)
print(s)

s.pop(1)
print(s)

s.pop()
print(s)

s.sort()
print(s)

s.reverse()
print(s)

num_list1 = [32, 88, 56, 90, 88]
num_list2 = [65, 88, 100, 209, 32]

num_list = num_list1 + num_list2

new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)

new_list1 = [num ** 2 for num in range(1, 21)]
print(new_list1)

list_1 = [23, 45, 67, 89, 12]
new_list2 = [num ** 2 for num in list_1 if num % 2 == 0]
print(new_list2)
print(list_1[1])
list_1[1] = 88
print(list_1)

a1, a2, a3, a4, a5 = list_1
print(f"a1={a1}, a2={a2}, a3={a3}, a4={a4}, a5={a5}")

