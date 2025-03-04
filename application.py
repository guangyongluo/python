from fastAPI import FastAPI
import uvicorn
from fastAPI.staticfiles import StaticFiles
from tutorial import app03


app = FastAPI(
    title="FastAPI",
    description='Fast API Demo',
    version="0.0.1beta"
)

app.mount("/static", StaticFiles(directory="./static"))

app.include_router(app03, prefix="/chapter03", tags=['第三章 请求参数和验证'])


if __name__ == '__main__':
    uvicorn.run("application:app", host="0.0.0.0", port=8080, reload=True, workers=5)