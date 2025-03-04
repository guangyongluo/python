from typing import Union

from fastAPI import FastAPI, Path
import uvicorn

app = FastAPI()

# 路径参数定义: {project_id} 是路径参数, name 是查询参数
@app.get("/project/{project_id}")
def get_project(project_id: Union[int, None] = 1, name: str = None):
    return {"project_id": project_id}

# 校验路径参数
@app.get("/env/{env_id}")
def get_env(env_id = Path(..., title="环境名称", description="环境名称", gt=1, lt=10)):
    return {"env_id": env_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)