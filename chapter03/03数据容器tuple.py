# 元组的组包与解包
t1 = (1, 2, 3) # 推荐这种方式定义元组
t2 = 4, 5, 6

print(t1)
print(t2)

# 解包操作
a, b, c = t1
print(f"a={a}, b={b}, c={c}")

# 扩展解包*
*i, j = t1
k, *m = t2

print(f"i={i}, j={j}")
print(f"k={k}, m={m}")

students = (
    ("s001", "王林", 85, 92, 78),
    ("s002", "李华", 90, 88, 95),
    ("s003", "张伟", 78, 80, 82),
    ("s004", "赵强", 92, 95, 90),
    ("s005", "刘洋", 88, 85, 91),
    ("s006", "陈静", 80, 82, 88),
    ("s007", "孙丽", 95, 90, 93),
    ("s008", "周杰", 82, 78, 85),
    ("s009", "吴敏", 90, 92, 88),
)

# 1. 计算每个学生的总分和平均成绩，并输出学生的姓名和平均成绩
for student in students:
    id, name, score1, score2, score3 = student
    total = score1 + score2 + score3
    average_score = (score1 + score2 + score3) / 3
    print(f"{name}的平均成绩是：{total}, 平均成绩是：{average_score:.2f}")

# 2. 统计各科的成绩的最高分、最低分和平均分，并输出结果
score1_list = [s[2] for s in students]
score2_list = [s[3] for s in students]
score3_list = [s[4] for s in students]

print(f"语文成绩：最高分={max(score1_list)}, 最低分={min(score1_list)}, 平均分={sum(score1_list)/len(score1_list):.2f}")
print(f"数学成绩：最高分={max(score2_list)}, 最低分={min(score2_list)}, 平均分={sum(score2_list)/len(score2_list):.2f}")
print(f"英语成绩：最高分={max(score3_list)}, 最低分={min(score3_list)}, 平均分={sum(score3_list)/len(score3_list):.2f}")

# 3. 找出平均成绩在90分以上的学生，并输出他们的姓名和平均成绩
for student in students:
    id, name, score1, score2, score3 = student
    average_score = (score1 + score2 + score3) / 3
    if average_score > 90:
        print(f"{name}的平均成绩是：{average_score:.2f}")