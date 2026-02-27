# 字符串是不可变的序列类型，字符串中的每个字符都有一个索引位置，可以通过索引来访问字符串中的字符。
s = "Hello Python"

print(s[4])
print(s[-8])

s = "    Hello-Python-Hello-World    "
# find() 查找指定字符串第一次出现的位置，如果找到返回索引位置，如果找不到返回-1
index = s.find("-")
print(index)

# count() 统计指定字符串在字符串中出现的次数
count = s.count("o")
print(count)

# upper() 将字符串中的所有字母转换为大写字母
s_upper = s.upper()
print(s_upper)

# lower() 将字符串中的所有字母转换为小写字母
s_lower = s.lower()
print(s_lower)

s1 = s.replace("-", "_")
print(s1)

print(s.startswith("Hello"))
print(s.endswith("Python"))

print("---------------------------")
print(s)

s2 = "黄山落叶松叶落山黄"
s3 = s2[::-1]
print(s2 == s3)

