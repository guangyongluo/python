# 定义字典dict
dict1 = {"王林": 675, "李华": 680, "张伟": 690, "王林": 700}
print(dict1)
print(type(dict1))

# key是唯一的，value可以重复，后面定义的key会覆盖前面定义的key
# key是不可变类型，可以是字符串、数字、元组等，value可以是任意类型，可以是字符串、数字、列表、字典等
dict2 = {0: 670, 1.5: 680, (1, 2): 690}
print(dict2)
print(type(dict2))

# 字典的访问和修改
dict3 = {"name": "Alice", "age": 30, "city": "New York"}
print(dict3["name"])  # 访问字典中的值
dict3["age"] = 31  # 修改字典中的值
print(dict3)

dict1["赵强"] = 710  # 添加新的键值对
print(dict1)

dict1["王林"] = 888  # 修改已有的键值对
print(dict1)

e = dict1.pop("王林")  # 删除键值对
print(e)
print(type(e))
print(dict1)

del dict1["李华"]  # 删除键值对
print(dict1)

items = dict1.items()
print(items)
print(type(items))
print(dict1.keys())
print(dict1.values())