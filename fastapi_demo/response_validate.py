from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

app = FastAPI()

class UserNameFrom(BaseModel):
    username: str

class UserPasswordFrom(BaseModel):
    password: str

class UserInfoFrom(UserNameFrom):
    sex: str
    age: int
    job: str
    address: str

class UserLoginFrom(UserNameFrom, UserPasswordFrom):
    pass

class UserRegisterForm(UserInfoFrom, UserPasswordFrom):
    password_confirm: str

@app.post("/user/login", response_model=UserInfoFrom, status_code=201)
async def login(user: UserLoginFrom):
    return {"username": user.username, "sex": "male", "age": 18, "job": "engineer", "address": "beijing"}

@app.post("/user/register", response_model=UserInfoFrom, status_code=201)
async def register(user: UserRegisterForm):
    return {"username": user.username, "sex": "male", "age": 18, "job": "engineer", "address": "beijing"}

@app.get("/user/info", response_model=UserInfoFrom, status_code=200)
async def get_user_info(username: str):
    return {"username": "username", "sex": "male", "age": 18, "job": "engineer", "address": "beijing"}

@app.get("/response")
async def get_response(response: Response):
    response.set_cookie(key="fake-session", value="fake-cookie-session-value")
    response.set_cookie(key="fake-token", value="fake-cookie-token-value")
    return {"response": "set two cookies"}

@app.get("/response/cookie")
async def get_response_cookie():
    response = JSONResponse(content={"response": "get two cookies"})
    response.set_cookie(key="fake-session", value="fake-cookie-session-value")
    response.set_cookie(key="fake-token", value="fake-cookie-token-value")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)