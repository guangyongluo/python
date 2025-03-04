from tortoise import Tortoise, run_async
from tortoise.functions import Count, Avg, Sum

from tortoise_demo.model_define import UserModel, PostModel, CommunityModel

# 排序查询
async def sort_user_all():
    """
    按照字段大小排序
    :return:
    """
    users = await UserModel.all().order_by('-id').values('id', 'username')
    print(users)

async def filter_user_all():
    """
    过滤查询
    gt 大于 lt 小于 gte 大于等于 lte 小于等于
    """
    # users = await UserModel.filter(id__gt=1).values('id', 'username')
    # 多条件过滤
    users = await UserModel.filter(id__gte=1, username__icontains='admin').values('id', 'username')
    print(users)


async def limit_page_user():
    """
    分页查询
    """
    users = await UserModel.all().limit(1).offset(1).values('id', 'username')
    print(users)

async def aggregate_user():
    """
    聚合查询
    """
    # user_count = await UserModel.all().annotate(count=Count('id')).values('count')
    # user_count = await UserModel.all().annotate(avg=Avg('id')).values('avg')
    user_count = await UserModel.all().annotate(sum=Sum('id')).values('sum')
    print(user_count)


async def init():
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:4406/orm_demo',
        modules={'models': ['tortoise_demo.model_define']},
    )
    # await sort_user_all()
    # await filter_user_all()
    # await limit_page_user()
    await aggregate_user()

if __name__ == "__main__":
    run_async(init())