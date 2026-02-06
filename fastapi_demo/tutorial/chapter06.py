from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError

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

### jwt token 示例

# 1. 生成加密jwt token的secret key 使用命令 openssl rand -hex 32
SECRET_KEY = "1bba03cbdaf5f53071a19731e4acfe237f637f0967ba22b6702e0bc7c55b17c0"
# 2. jwt的加密算法
ALGORITHM = "HS256"
# 3. token过期时间 30分钟
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 4. 修改数据库中的密码
fake_users_db.update(
     {
        "alice": {
            "username": "alice",
            "full_name": "Alice Wonderland",
            "email": "alice@example.com",
            "hashed_password": "$2b$12$I.0Kx4360uTYDuDBPFKcs.qdMRFod.sA4sjHCiFqHhHzVWJR.v7Km",
            "disabled": False,
        },
        "bob": {
            "username": "bob",
            "full_name": "Bob Builder",
            "email": "bob@example.com",
            "hashed_password": "$2b$12$I.0Kx4360uTYDuDBPFKcs.qdMRFod.sA4sjHCiFqHhHzVWJR.v7Km",
            "disabled": True,
        }
    }
)

class Token(BaseModel):
    """返回给用户的token"""
    access_token: str
    token_type: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# print(pwd_context.hash("hello"))


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/chapter06/jwt/token")

def verify_password(plain_password, hashed_password):
    """对密码进行校验"""
    return pwd_context.verify(plain_password, hashed_password)

def jwt_get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def jwt_authenticate_user(db, username: str, password: str):
    user = jwt_get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(plain_password=password, hashed_password=user.hashed_password):
        return False
    return user

def created_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app06.post("/jwt/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = jwt_authenticate_user(db=fake_users_db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = created_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def jwt_get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = jwt_get_user(db=fake_users_db, username=username)
    if not user:
        raise credentials_exception
    return user

def jwt_get_current_active_user(current_user: User = Depends(jwt_get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
    return current_user

@app06.post("/jwt/user/me")
def jwt_current_user_me(current_user: User = Depends(jwt_get_current_active_user)):
    return current_user

