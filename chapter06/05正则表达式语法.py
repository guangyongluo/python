import re

s = "18809090000是我的手机号，188开头的，以00结尾的。我的另一个手机号是15500008888，两个QQ号分别是1259908903和138090912938383，邮箱为python666@163.com，请给我发邮件。"

# 正则表达式
print(re.findall(r"188.*", s))
print(re.findall(r"188.?", s))
print(re.findall(r"188.+", s))

print(re.findall(r"188\d{8}", s))
print(re.findall(r"188\d{6,10}", s))
print(re.findall(r"188\d{6,}", s))

print(re.findall(r"1[38]\d{8}", s))
print(re.findall(r"1[^38]\d{8}", s))
print(re.findall(r"1[3-9]\d{9}", s))
print(re.findall(r"^1[3-9]\d{9}", s))
print(re.findall(r"^1[3-9]\d{9}$", s))

print(re.findall(r"\w+@\w+.\w+", s))
print(re.findall(r"\w+@\w+.\w+", s, re.ASCII))

s = "现在时间是2026-02-06 10:05:25，今天天气还可以，气温是28度"
print(re.findall(r"\d{4}-\d{2}-\d{2}", s))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s))