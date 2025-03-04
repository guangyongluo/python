from fastapi import APIRouter, HTTPException

from fastAPI.user_service.dto import UserInfoForm, RegisterForm, LoginForm
from fastAPI.user_service.models import UserModel

router = APIRouter()

@router.post("/register", response_model=UserInfoForm, summary="用户注册", description="用户注册接口")
async def register(param: RegisterForm):
    # 判断密码是否一致
    if param.password != param.password_confirm:
        raise HTTPException(status_code=400, detail="两次密码不一致")

    # 判断用户名是否已经存在
    if await UserModel.get_or_none(username=param.username):
        raise HTTPException(status_code=400, detail="用户名已经存在")

    # 进行注册
    user = await UserModel.create(**param.model_dump())
    return UserInfoForm(**user.__dict__)

@router.post("/login", response_model=UserInfoForm)
async def login(param: LoginForm):
    user = await UserModel.get_or_none(username=param.username, password=param.password)
    if user:
        return UserInfoForm(**user.__dict__)
    else:
        raise HTTPException(status_code=400, detail="用户名或密码错误")