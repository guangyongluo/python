from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app06 = APIRouter()

"""
OAuth2PasswordBearer 是接收URL作为参数的类：客户端会向这个URL发送用户名和密码以获取令牌
OAuth2PasswordBearer 并不会创建相应的端点，它只是一个类，告诉FastAPI如何从请求中获取令牌，以及在哪里可以获取令牌
当请求到来时，FastAPI会检查请求的Authorization头，提取令牌，并将其作为字符串传递给依赖项
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/chapter06/token")

@app06.post("/oauth2_password")
def oauth2_password_bearer(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# 基于 password 和 bearer token 的 OAuth2 认证

fake_users_db = {
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderland",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "bob": {
        "username": "bob",
        "full_name": "Bob Builder",
        "email": "bob@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    }
}

def fake_hash_password(password: str):
    return "fakehashed" + password

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def fake_decode_token(token: str):
    user = get_user(fake_users_db, token)
    return user

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"} # OAuth2的规范，如果认证失败，请求头中返回”WWW-Authenticate“
        )
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user

@app06.post("/token")
def login(form_data = Depends(OAuth2PasswordRequestForm)):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}

@app06.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


