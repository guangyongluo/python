import bisect, array

# 用来处理已排序序列，其中的方法可以维持一个已排序序列。

inter_list = []

bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 0)

print(inter_list)

my_array = array.array('i')
bisect.insort(my_array, 3)
bisect.insort(my_array, 2)
bisect.insort(my_array, 5)
bisect.insort(my_array, 1)
bisect.insort(my_array, 6)
bisect.insort(my_array, 0)

print(my_array)

# 列表推导式
my_list = [i for i in range(21) if i % 2 == 1]
print(my_list)

# 生成器表达式
my_gen = (i for i in range(21) if i % 2 == 1)
print(type(my_gen))
print(my_gen)

print(list(my_gen))

# 字典推导式
my_dict = {"alice" : 21, "bob" : 33, "charlie" : 45}
reversed_dict = {value : key for key, value in my_dict.items()}
print(reversed_dict)