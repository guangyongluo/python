from tortoise import Tortoise, run_async

from tortoise_demo.model_define import UserModel

# 添加用户
async def create_user(username: str, password: str) -> UserModel:
    return await UserModel.create(username=username, password=password)

# 修改用户
async def update_user(user_id: int, username: str, password: str) -> UserModel:
    user = await UserModel.get(id=user_id)
    user.username = username
    user.password = password
    await user.save()
    return user

# 删除用户
async def delete_user(user_id: int) -> UserModel:
    user = await UserModel.get(id=user_id)
    await user.delete()
    return user

# 根据用户ID查找用户
async def find_user_by_id(user_id: int) -> UserModel:
    return await UserModel.get(id=user_id)

# 查找所有用户
async def find_all_users():
    return await UserModel.all()

async def init():
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:4406/orm_demo',
        modules={'models': ['__main__']},
    )

    # 在Tortoise初始化之后，生成表结构
    # user = await create_user("hei", "hei@123")
    # user = await update_user(1, "administator", "administator@123")
    # user = await delete_user(3)
    # user = await find_user_by_id(1)
    user_list = await find_all_users()
    print(user_list)

if __name__ == "__main__":
    run_async(init())