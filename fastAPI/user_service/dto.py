from pydantic import BaseModel, Field


class RegisterForm(BaseModel):
    username: str = Field(description="用户名", min_length=6, max_length=50)
    password: str = Field(description="密码", min_length=6, max_length=50)
    password_confirm: str = Field(description="确认密码", min_length=6, max_length=50)

class LoginForm(BaseModel):
    username: str = Field(description="用户名", min_length=6, max_length=50)
    password: str = Field(description="密码", min_length=6, max_length=50)

class UserInfoForm(BaseModel):
    email: str = Field(..., description="邮箱", min_length=6, max_length=50)
    age: int = Field(..., description="年龄", ge=0, le=150)
    phone: str = Field(description="手机号", min_length=11, max_length=11)
    sex: str = Field(..., description="性别", min_length=1, max_length=2)
    address: str = Field(..., description="地址", min_length=6, max_length=100)