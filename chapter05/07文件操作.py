# 读文件

# 1. 打开文件
# f = open("resource/望庐山瀑布.txt", "r", encoding="utf-8")

# 2. 读取文件内容
# content = f.read() # 读取所有内容
# print(content)

# content_list = f.readlines()
# for line in content_list:
#    print(line.strip())

# f.close()

# 写文件

# 1. 打开文件
with open("resource/静夜思.txt", "w", encoding="utf-8") as f:
    # 2. 写入文件内容
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")






