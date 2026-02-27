# 定义集合set
s = {5,3,21,8,5,3}
print(s)
print(type(s))

# 定义一个空集合 s = set()，不能使用s = {}，因为s = {}定义的是一个空字典
s = {}
print(s)
print(type(s))

s = set()
print(s)
print(type(s))

s = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000}
print(s)
s.add(1200)
print(s)

s.remove(200)
print(s)

e = s.pop()
print(e)
print(s)

s.clear()
print(s)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

print(s2.difference(s3))
print(s3.difference(s2))

print(s2.union(s3))
print(s3.union(s2))

print(s2.intersection(s3))
print(s3.intersection(s2))


# 选修足球的学生名单
football_students = {"张三", "李四", "王五", "赵六", "钱七"}
# 选修篮球的学生名单
basketball_students = {"李四", "王五", "赵六", "孙八", "周九"}
# 选修法语的学生名单
french_students = {"王五", "赵六", "孙八", "周九", "吴十"}
# 选修艺术的学生名单
art_students = {"赵六", "孙八", "周九", "吴十", "郑十一"}

# 1. 找出同时选修法语和艺术的学生名单
# 方式一：使用intersection()方法
french_and_art_students = french_students.intersection(art_students)
print("同时选修法语和艺术的学生名单：", french_and_art_students)
# 方式二：使用&运算符
french_and_art_students2 = french_students & art_students
print("同时选修法语和艺术的学生名单：", french_and_art_students2)

# 2. 找出同时选修四门课程的学生名单
all_courses_students = football_students.intersection(basketball_students, french_students, art_students)
print("同时选修四门课程的学生名单：", all_courses_students)

all_courses_students2 = football_students & basketball_students & french_students & art_students
print("同时选修四门课程的学生名单：", all_courses_students2)

# 3. 找出选修了足球，但是没有选修蓝球的学生名单
football_not_basketball_students = football_students.difference(basketball_students)
print("选修了足球，但是没有选修蓝球的学生名单：", football_not_basketball_students)
football_not_basketball_students2 = football_students - basketball_students
print("选修了足球，但是没有选修蓝球的学生名单：", football_not_basketball_students2)
football_not_basketball_students3 = {s for s in football_students if s not in basketball_students}
print("选修了足球，但是没有选修蓝球的学生名单：", football_not_basketball_students3)

# 4. 统计每一个学生选修的课程数量
# all_students = football_students.union(basketball_students, french_students, art_students)
all_students = football_students | basketball_students | french_students | art_students
print("所有选修课程的学生名单：", all_students)

for student in all_students:
    count = 0
    if student in football_students:
        count += 1
    if student in basketball_students:
        count += 1
    if student in french_students:
        count += 1
    if student in art_students:
        count += 1
    print(f"{student}选修了{count}门课程")