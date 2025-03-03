from tortoise import Tortoise, run_async

from tortoise_demo.model_define import UserModel, PostModel, CommunityModel


# 一对一查询
async def one_to_one_query():
    user = await UserModel.get_or_none(id=1).select_related('info')
    print(user.info.nickname)
    print(user.info.phone)
    print(user.info.email)
    print(user.info.address)

# 一对多查询
async def one_to_many_query():
    user = await UserModel.get_or_none(id=1).prefetch_related('posts')
    # for post in user.posts:
    #     print(post.title)
    #     print(post.content)
    posts = await user.posts.all().values('title', 'content')
    result = {
        'id': user.id,
        'username': user.username,
        "posts": posts
    }
    print(result)

async def many_to_one_query():
    post = await PostModel.get_or_none(id=1).prefetch_related('user')
    print(post.user.username)
    print(post.user.password)

async def many_to_many_query():
    user = await UserModel.get_or_none(id=1).prefetch_related('communities')
    # for community in user.communities:
    #     print(community.name)
    communities = await user.communities.all().values('name')
    result = {
        'id': user.id,
        'username': user.username,
        "communities": communities
    }
    print(result)

async def many_to_many_query2():
    community = await CommunityModel.get_or_none(id=1).prefetch_related('members')
    # for user in community.members:
    #     print(user.username)
    #     print(user.password)

    members = await community.members.all().values('username', 'password')
    result = {
        'id': community.id,
        'name': community.name,
        "members": members
    }
    print(result)


async def init():
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:4406/orm_demo',
        modules={'models': ['tortoise_demo.model_define']},
    )
    # await one_to_many_query()
    # await one_to_one_query()
    # await many_to_one_query()
    # await many_to_many_query()
    await many_to_many_query2()


if __name__ == "__main__":
    run_async(init())