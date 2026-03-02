import math
# 变量定义 - 指定类型注解

a : int = 10
b : float = 3.14
c : str = "Hello, Python!"
d : bool = True
e : None = None

l : list[int] = [1, 2, 3, 4, 5]
t : tuple[str, int] = ("Alice", 30)
s : set[float] = {1.1, 2.2, 3.3}
m : dict[str, int] = {"Alice": 30, "Bob": 25}

# 函数定义 - 指定参数和返回值类型注解
def add(x: int, y: int) -> int:
    return x + y

def calc(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def circle_area_len(radius: float) -> tuple[float, float]:
    return math.pi * radius ** 2, 2 * math.pi * radius