from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from jwt.fastapi_jwt import fastapi_jwt_url


app = FastAPI(
    title="FastAPI",
    description='Fast API Demo',
    version="0.0.1beta"
)

app.mount("/static", StaticFiles(directory="./static"))

app.include_router(fastapi_jwt_url, prefix="/jwt", tags=['fast api demo'])

if __name__ == '__main__':
    uvicorn.run("application:app", port=8080, reload=True)