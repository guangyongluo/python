from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException

app05 = APIRouter()

# 函数依赖

def common_parameters(q: Optional[str] = None, page: int = 0, limit: int = 100):
    return {"q": q, "page": page, "limit": limit}

@app05.get("/dependency01")
async def dependency01(commons: dict = Depends(common_parameters)):
    return commons

@app05.get("/dependency02")
def dependency02(commons: dict = Depends(common_parameters)):
    return commons

# 类依赖

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, page: int = 0, limit: int = 100):
        self.q = q
        self.page = page
        self.limit = limit

@app05.get("/dependency03")
def dependency03(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.page : commons.page + commons.limit]
    response.update({"items": items})
    return response

# 子依赖

def query(q: Optional[str] = None):
    return q

def sub_query(q: str = Depends(query), last_query: Optional[str] = None):
    if q:
        return last_query
    return q

@app05.get("/dependency04")
def dependency04(final_query: str = Depends(sub_query, use_cache=True)):
    return {"final_query": final_query}

# 路劲操作中添加依赖

def verify_token(x_token: str = Header(...)):
    if x_token == "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token

def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

@app05.get("/dependency05", dependencies=[Depends(verify_token), Depends(verify_key)])
def dependency05():
    return [{"user": "user01"}, {"user": "user02"}]