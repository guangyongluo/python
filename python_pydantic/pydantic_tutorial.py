from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, ValidationError, constr
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel):
    id: int # 必填字段
    name: str = "John Snow" # 有默认值，选填字段
    signup_ts: Optional[datetime] = None
    friends: List[int] = [] # 列表中元素是int类型或者可以直接转换成int类型

# external_data = {"id": "123", "signup_ts": "2019-06-01 12:22", "friends": [1, "2", b"3"]}
# user = User(**external_data)
# print(user.id, user.friends)
# print(user.model_dump())

try:
    user = User(id=123, signup_ts=datetime.today(), friends=[1, "2", b"3"])
    print(user.model_copy())
    print(User.model_validate_json('{"id": 123, "signup_ts": "2019-06-01 12:22", "friends": [1, "2", "3"]}'))
    print(User.model_validate(user))
    print(User.model_json_schema())
    print(User.model_fields)
except ValidationError as e:
    print(e.json())

class Sound(BaseModel):
    sound: str

class Dog(BaseModel):
    birthday: date
    weight: float = Optional[None]
    sound: List[Sound]

dogs = Dog(birthday=date.today(), weight=10.5, sound=[{"sound": "wangwang"}, {"sound": "guaigua"}])
print(dogs.model_dump())

Base = declarative_base()

class CompanyOrm(Base):
    __tablename__ = 'company'
    id: int = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(255), index=True, nullable=False, unique=True)
    name: str = Column(String(255), unique=True)
    domains: List[str] = Column(ARRAY(String(255)))
    created_at: datetime = Column(DateTime, default=datetime.now)
    updated_at: datetime = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class CompanyMode(BaseModel):
    id: int
    public_key: str = constr(max_length=255)
    name: str = constr(max_length=255)
    domains: List[str] = List[constr(max_length=255)]
    created_at: datetime = constr()
    updated_at: datetime



