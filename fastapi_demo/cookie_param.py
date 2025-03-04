from fastAPI import FastAPI
import uvicorn
from fastAPI.params import Cookie

app = FastAPI()

@app.get("/token")
def get_token(token: str = Cookie(None, max_length=10)):
    return {"token": token}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)