from enum import Enum
from datetime import date
from fastapi import APIRouter, Path, Query, Cookie, Header
from typing import List, Optional
from pydantic import BaseModel, Field

app03 = APIRouter()


### 路径参数的获取和校验

@app03.get("/path/parameters")
def path_parameter():
    return {"message", "this is a message"}


@app03.get("/path/{parameter}")
def path_param(parameter: str):
    return {"message": parameter}


class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"


@app03.get("/enum/{city}")
def latest(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": city, "confirmed": 1392, "death": 7}
    elif city == CityName.Beijing:
        return {"city_name": city, "confirmed": 963, "death": 7}


@app03.get("/file/file_path:path")
def file_path(file_path: str):
    return f"the file path is {file_path}"


@app03.get("/path/{num}")
def path_variable_validation(
        num: int = Path(title='路径参数中的数字', gt=0, lt=10, description='请求路径中的数字参数约束')):
    return num


### 查询参数的获取和校验

@app03.get("/query")
def page_limit(page: int = 1, limit: Optional[int] = None):
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}


@app03.get("/query/bool/conversion")
def type_conversion(param: bool = False):
    return param

@app03.get("/query/validation")
def query_params_validate(value: str = Query(..., min_length=8, max_length=16, regex='^a'),
                          values: List[str] = Query(default=['v1', 'v2'], alias="alias_name")):
    return value, values

### 定义嵌套的请求体
class CityInfo(BaseModel):
    name: str = Field(..., examples=["Beijing"])
    country: str
    country_code: str = None
    country_population: int = Field(default=800, title="人口数量", description="国家的人口")

    class Config:
        json_schema_extra = {
            "example" : {
                "name": "Shanghai",
                "country": "China",
                "country_code": "CN",
                "country_population": 1400000000,
            }
        }

@app03.post("/request/body/city")
def city_info(city: CityInfo):
    print(city.name, city.country)
    return city.model_dump()

### 前面梳理的所有传参形式
@app03.put("/request/city/{name}")
def mix_city_info(
        name: str,
        city01: CityInfo,
        city02: CityInfo,
        confirmed: int = Query(ge=0, description="新冠确诊数", default=0),
        death: int = Query(ge=0, description="新冠死亡数", default=0)
):
    if name == "Shanghai":
        return {"Shanghai", {"confirmed": confirmed, "death": death}}
    return city01.model_dump(), city02.model_dump()

### 数据嵌套请求体
class Data(BaseModel):
    city: List[CityInfo] = None
    date: date
    confirmed: int = Field(ge=0, description="新冠确诊数", default=0)
    death: int = Field(ge=0, description="新冠死亡数", default=0)
    recovered: int = Field(ge=0, description="新冠痊愈数", default=0)

@app03.put("/request_body/nested")
def nested_models(data: Data):
    return Data

### cookie和token传参
@app03.get("/cookie")
def cookie(cookie_id: Optional[str] = Cookie(None)):
    return {"cookie_id": cookie_id}

@app03.get("/header")
def header(user_agent: Optional[str] = Header(None, convert_underscores=True), x_token: List[str] = Header(None)):
    return {"User-Agent": user_agent, "x_token": x_token}