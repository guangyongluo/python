# 递归调用：指的事在函数中自己调用自己的情况
# 递归调用的优点：代码简洁，容易理解
# 递归调用的缺点：效率较低，容易导致栈溢

# 计算阶乘的递归函数
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
"""
案例2：定义一个用于根据传入一批商品信息（商品名、价格、数量）、优惠（优惠劵、积分抵扣）、运费计算订单总金额函数
具体规则如下：
    1. 优惠券需要商品金额满5000才可以使用，且优惠券的金额不能超过商品总金额
    2. 积分抵扣需要商品金额满5000才可以使用，100积分抵扣1元，且积分抵扣的金额不能超过商品总金额，积分只能整百抵扣。
"""
def calculate_order_cost(*goods, coupon=0, points=0, express=0.0):
    """
    计算订单总金额的函数
    :param items: 商品信息列表，每个元素是一个包含商品名、价格、数量的字典
    :param coupon: 优惠券金额，默认为0
    :param points: 积分数量，默认为0
    :param express: 运费金额，默认为0.0
    :return: 订单总金额
    """

    # 订单总金额 = 商品总金额 - 优惠金额 - 积分抵扣金额 + 运费
    # 1. 计算商品总金额
    total_price = [goods[1] + goods[2] for goods in goods]
    total_cost = sum(total_price)

    # 2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3.扣减积分抵扣金额
    if total_cost >= 5000 and points // 100 <= total_cost:
        total_cost -= (points // 100)

    # 4.加上运费
    total_cost += express
    return total_cost


total_cost = calculate_order_cost(("手机", 3000, 2), ("电脑", 5000, 1), coupon=1000, points=500, express=50)
print(total_cost)