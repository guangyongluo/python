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