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

"""
    案例：
    开发一个购物车，实现商品信息的添加、修改、产出和查询功能。系统使用嵌套字典结构存储商品信息，通过控制台与用户交互
    具体功能如下；
    1. 添加购物车：用户输入商品名称、价格和数量，系统将商品信息添加到购物车中。
    2. 修改购物车：用户输入要修改的商品名称，如果商品存在，用户可以修改该商品的价格和数量。
    3. 删除购物车：用户输入要删除的商品名称，如果商品存在，系统将其从购物车中删除。
    4. 查询购物车：用户输入要查询的商品名称，如果商品存在，系统将显示该商品的价格和数量。
    5. 退出购物车
    
    结构：shopping_cart = {"mate80":{"price": 5999, "quantity": 1}, "iPhone14": {"price": 7999, "quantity": 2}}
"""
shopping_cart = {}

# 1. 制作菜单
print("欢迎使用购物车管理系统！")

menu = """
################# 购物车管理系统菜单 ###################
#                 1. 添加购物车                       #
#                 2. 修改购物车                       #
#                 3. 删除购物车                       #
#                 4. 查询购物车                       #
#                 5. 退出购物车                       #
#####################################################

"""

print("欢迎使用购物车管理系统~")

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行具体操作
    choice = input("请输入一个功能编号（1-5）：")


    match choice:
        case "1":  # 添加购物车
            good_name = input("请输入商品名称：")
            good_price = float(input("请输入商品价格："))
            good_quantity = int(input("请输入商品数量："))

            if good_name in shopping_cart:
                print(f"{good_name}已经在购物车中了，请重新选择~")
            else:
                shopping_cart[good_name] = {"price": good_price, "quantity": good_quantity}
                print(f"{good_name}已经成功添加到购物车中了~")
        case "2":  # 修改购物车
            good_name = input("请输入商品名称：")
            good_price = float(input("请输入商品价格："))
            good_quantity = int(input("请输入商品数量："))

            if good_name in shopping_cart:
                shopping_cart[good_name] = {"price": good_price, "quantity": good_quantity}
                print(f"{good_name}已经成功修改了~")
            else:
                print(f"{good_name}不在购物车中，请重新选择~")
        case "3":  # 删除购物车
            good_name = input("请输入商品名称：")

            if good_name in shopping_cart:
                shopping_cart.pop(good_name)
                print(f"{good_name}已经成功删除了~")
            else:
                print(f"{good_name}不在购物车中，请重新选择~")
        case "4":  # 查询购物车
            good_name = input("请输入商品名称：")

            if good_name in shopping_cart:
                good_info = shopping_cart[good_name]
                print(f"{good_name}的价格是{good_info['price']}，数量是{good_info['quantity']}~")
            else:
                print(f"{good_name}不在购物车中，请重新选择~")
        case "5":  # 退出购物车
            print("感谢使用购物车管理系统，再见！")
            break
        case "_": # 匹配其他所有的情况
            print("输入的功能编号不合法，请输入1-5之间的数字")
