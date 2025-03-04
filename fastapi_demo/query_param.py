from typing import Union

from fastAPI import FastAPI
import uvicorn
from fastAPI.params import Query

app = FastAPI()

# 第一个demo试例
@app.get("/")
async def read_root():
    return {"message": "Hello World", "code": 200, "data": None}

# 查询参数，只校验参数类型
@app.get("/demo")
async def read_demo(age: int, name: str | None = None):
    return {"name": name, "age": age}

# 查询参数，校验参数类型和长度
@app.get("/demo/page/check")
async def read_demo_page(token: Union[str, None] = Query(None, min_length=1, max_length=10, description="用户token")):
    return {"token": token}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
