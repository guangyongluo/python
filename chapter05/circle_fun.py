# 导入整个模块
import math
import random
from random import randint as r_int

# 计算圆的面积
def circle_area(radius: float) -> float:
    """
    计算圆的面积
    :param radius: 圆的半径
    :return: 圆的面积
    """
    area = math.pi * radius ** 2
    return area

# 计算圆的周长
def circle_length(radius: float) -> float:
    """
    计算圆的周长
    :param radius: 圆的半径
    :return: 圆的周长
    """
    length = 2 * math.pi * radius
    return length

for i in range(100):
    print(random.randint(1, 100))

for i in range(100):
    print(r_int(1, 100))