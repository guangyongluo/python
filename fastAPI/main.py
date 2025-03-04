from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from fastAPI.config.db_config import TORTOISE
from fastAPI.config.exception_handler import starlette_http_exception_handler, request_validation_exception_handler
from fastAPI.user_service.api import router as user_router
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI(
    title='fastapi集成tortoise orm框架项目',
    version='1.0.0',
    description='这是demo项目'
)

# 注册tortoise orm
register_tortoise(app, config=TORTOISE)

# 注册路由
app.include_router(user_router, prefix='/user/api/v1', tags=['用户服务接口'])

app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, starlette_http_exception_handler)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)