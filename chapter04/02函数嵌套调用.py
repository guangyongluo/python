# 函数的嵌套调用，就是在一个函数的内部调用另一个函数，甚至在一个函数内部调用自己，这种情况叫做递归调用。
def func1():
    print("这是函数1")
    func2()
    print("函数1结束了")

def func2():
    print("这是函数2")
    func3()
    print("函数2结束了")

def func3():
    print("这是函数3")

func1()