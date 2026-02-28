# 全局变量：在函数之外定义的变量，在整个文件中（包括函数内）都可以使用（通常定义在文件的顶部）。
# 局部变量：在函数内部定义的变量，只能在该函数内使用，函数执行结束后局部变量会被销毁。
from traceback import print_tb

num = 10  # 全局变量

print("全局变量num的值是：", num)

def circle_area(radius):
    pi = 3.14  # 局部变量
    area = pi * radius ** 2  # 使用局部变量计算面积
    # 局部变量num = 100  # 在函数内部定义一个局部变量num，这个num与全局变量num是不同的变量，它们在内存中占用不同的位置，互不干扰。
    num = 10000
    print("在函数内部访问全局变量num的值是：", num)  # 在函数内部访问全局变量
    return area

c_area = circle_area(num)
print(c_area)

print("全局变量num的值是：", num)  # 在函数外部访问全局变量
