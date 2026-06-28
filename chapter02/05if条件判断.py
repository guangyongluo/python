# if条件判断：如果分数大于等于60分，输出“及格”，否则输出“不及格”

score = int(input("请输入分数："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")

# 输入三角形的三个边，判断三角的类型
a = int(input("请输入第一条边的边长："))
b = int(input("请输入第一条边的边长："))
c = int(input("请输入第一条边的边长："))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print(f"{a} {b} {c} 这三条边长构成等边三角形 ~")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c} 这三条边长构成等腰三角形 ~")
    else:
        print(f"{a} {b} {c} 这三条边长构成普通三角形 ~")
else:
    print(f"{a} {b} {c} 这三条边长不能构成三角形")

# 工作日程安排
day = input("请输入星期几(1-7):")
