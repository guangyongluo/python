import re

s1 = "18809090000是我的手机号，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998993和18809091293833你记住了吗？"
s2 = "我的手机号是18809090000，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998993和18809091293833你记住了吗？"

# match - 从字符串的开头开始匹配(匹配第一个匹配项)
result = re.match(r"1[3-9]\d{9}", s1)
print(result.group()) # 获取到匹配结果
print(result.span()) # 获取匹配的索引
print(result.start()) # 获取匹配项的开始索引
print(result.end()) # 获取匹配项的结束索引

# search - 从任意位置开始，搜索第一个匹配项
result = re.search(r"1[3-9]\d{9}", s2)
print(result.group())
print(result.span())
print(result.start())
print(result.end())

# findall - 从任意位置开始，搜索所有匹配项
result = re.findall(r"1[3-9]\d{9}", s2)
print(result)