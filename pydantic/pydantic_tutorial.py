from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int # 必填字段
    name: str = "John Snow" # 有默认值，选填字段
    signup_ts = Optional[datetime] = None
    friends = List[int] = [] # 列表中元素是int类型或者可以直接转换成int类型

