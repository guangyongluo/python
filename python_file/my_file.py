# 打开文件
# f = open("data.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容：{f.read(10)}")

print("--------------------------------------")

# 读取文件 - readLines()
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# print(f"第一行：{line1}")
# print(f"第一行：{line2}")

# for line in f:
#     print(line)
#
# f.close()

# with open("data.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(line)


def print_file_info(file_name):
    """
    input file print out to console.
    :param file_name: file path parameter.
    :return: file content.
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("file content : ")
        print(content)
    except Exception as e:
        print(f"programme go crush, cause is {e}")
    finally:
        if f:
           f.close()