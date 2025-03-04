from fastAPI import FastAPI, Header
import uvicorn
from setuptools.command.alias import alias

app = FastAPI()

@app.get("/header/token")
def get_token(token: str = Header(None, max_length=10, alias="JWT-Token")):
    return {"token": token}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)