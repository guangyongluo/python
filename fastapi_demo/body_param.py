from datetime import date

from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn
from pydantic.fields import Field

app = FastAPI()


@app.post("/user/login")
async def login(username: str = Body(None, min_length=5, max_length=50),
                password: str = Body(..., min_length=5, max_length=20)):
    return {"username": username, "password": password}


class RegisterAddress(BaseModel):
    country: str = Field(default=None, title="country", description="country for registry", min_length=5, max_length=50)
    province: str = Field(default=None, title="province", description="province for registry", min_length=5, max_length=50)
    city: str = Field(default=None, title="city", description="city for registry", min_length=5, max_length=50)
    street: str = Field(default=None, title="street", description="street for registry", min_length=5, max_length=50)


class RegisterInfo(BaseModel):
    username: str = Field(title="user name", description="user name for registry", min_length=5, max_length=50)
    password: str = Field(title="password", description="password for registry", min_length=5, max_length=20)
    email: str = Field(default=None, title="email", description="email for registry", min_length=5, max_length=50)
    phone: str = Field(title="phone", description="phone for registry", min_length=5, max_length=50)
    birthday: date = Field(default=None, title="birthday", description="birthday for registry", le=date.today(), ge=date(1900, 1, 1))
    address: RegisterAddress

@app.post("/user/register")
async def register(info: RegisterInfo = Body(..., embed=True)):
    return info.model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
