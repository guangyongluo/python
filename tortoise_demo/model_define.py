from tortoise.models import Model
from tortoise import fields, Tortoise, run_async


class UserModel(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=20)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        table = "user"

# 一对多关系
class PostModel(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    content = fields.TextField()
    user = fields.ForeignKeyField('models.UserModel', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        table = "post"

# 一对一关系
class UserInfoModel(Model):
    id = fields.IntField(pk=True)
    nickname = fields.CharField(max_length=50)
    phone = fields.CharField(max_length=11)
    email = fields.CharField(max_length=50)
    address = fields.CharField(max_length=100)
    user = fields.OneToOneField('models.UserModel', related_name='info')

    def __str__(self):
        return self.nickname

    class Meta:
        table = "user_info"

# 多对多关系
class CommunityModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    members = fields.ManyToManyField('models.UserModel', related_name='communities')

    def __str__(self):
        return self.name

    class Meta:
        table = "community"

#连接数据库初始化配置
async def init():
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:4406/orm_demo',
        modules={'models': ['__main__']},
    )

    # 在Tortoise初始化之后，生成表结构
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())