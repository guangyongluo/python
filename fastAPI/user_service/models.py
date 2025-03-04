from tortoise import models, fields

class UserModel(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True, description="用户名")
    password = fields.CharField(max_length=20, description="密码")
    email = fields.CharField(max_length=50, description="邮箱")
    age = fields.IntField(description="年龄")
    sex = fields.CharField(max_length=10, description="性别")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_at = fields.DatetimeField(auto_now=True, description="更新时间")

    def __str__(self):
        return self.username

    class Meta:
        table = "user"
        table_description = "用户表"