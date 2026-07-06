# 函数的定义
import math


def circle_area(radius):
    """
    计算圆的面积
    :param radius: 圆的半径
    :return: 圆的面积, 圆的周长
    """
    area = math.pi * radius ** 2, 2 * math.pi * radius
    return area


def rectangle_area(length, width):
    """
    计算长方形的面积
    :param length: 长方形的长度
    :param width: 长方形的宽度
    :return: 长方形的面积
    """
    area = length * width
    return area

def circle_area_length(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积，圆的周长
    """
    return math.pi * r**2, 2 * math.pi * r

print(type(circle_area_length(10)))

a = 1, 2, 3, 4, 5, 6

print(a)
print(type(a))