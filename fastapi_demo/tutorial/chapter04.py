from typing import Optional, List, Union
from fastapi import APIRouter, status, Form, File, UploadFile, HTTPException
from pydantic import BaseModel, EmailStr

app04 = APIRouter()


# response Model 响应类型
class UserRequestModel(BaseModel):
    username: str
    password: str
    email: EmailStr
    mobile: str = '10086'
    address: str = None
    full_name: Optional[str] = None


class UserResponseModel(BaseModel):
    username: str
    email: EmailStr
    mobile: str = '10086'
    address: str = None
    full_name: Optional[str] = None


users = {
    "user01": {"username": "user01", "password": "123123", "email": "user01@example.com"},
    "user02": {"username": "user02", "password": "123456", "email": "user02@example.com", "mobile": "13888888888"}
}


@app04.post("/user", response_model=UserResponseModel, response_model_exclude_unset=True)
def user(user: UserRequestModel):
    print(user.password)
    return users["user01"]


@app04.get("/userlist", response_model=Union[UserRequestModel, UserResponseModel], response_model_exclude_none=True)
def user_list_response(user: UserRequestModel):
    del user.password
    return user


@app04.post("/status_code", status_code=200)
def status_code():
    return {"status_code": 200}


@app04.post("/status_attribute", status_code=status.HTTP_200_OK)
def status_attribute():
    print(status.HTTP_200_OK)
    return {"status_code": status.HTTP_200_OK}


### Form data 表单数据处理
@app04.post("/login")
def login(user: str = Form(examples=['leo', 'admin'], max_length=100, min_length=3),
          password: str = Form(min_length=6, max_length=18)):
    return {"user": user, "password": password}


### 单文件、多文件上传

# 使用File类， 文件内容会以bytes类型的形式读入内存，适合小文件上传
@app04.post("/upload_file")
def upload_file(file: bytes = File(..., description="文件的二进制数据")):
    return {"file_size": len(file)}

@app04.post("/upload_files")
def upload_files(files: List[bytes] = File(..., description="多个文件的二进制数据")):
    return {"file_sizes": [len(file) for file in files]}

# 使用UploadFile类， 适合大文件上传，UploadFile是一个“类文件”对象
@app04.post("/upload_upload_file")
async def upload_upload_file(files: List[UploadFile] = File(..., description="文件的二进制数据")):
    """
    使用UploadFile类的又是：
    1. 文件储存在内存中，使用的内存达到阈值后，将被保存在磁盘中
    2. 适合于图片、视频大文件
    3. 可以获取上传的文件的元数据，比如文件名、创建时间、文件类型等
    4. 有文件对象的异步接口
    5. 可以像操作普通文件那样操作它，比如读取、写入、关闭文件等
    """
    for file in files:
        contents = await file.read()  # 读取文件内容
        print(f"filename: {file.filename}, content_type: {file.content_type}, size: {len(contents)}")
        await file.seek(0)


# 处理Exception
@app04.get("/http_exception")
def http_exception(q: str):
    if q != 'fastapi':
        raise HTTPException(status_code=404, detail="没有找到相关资源", headers={"X-Error": "There goes my error"})
    return {"q": q}
