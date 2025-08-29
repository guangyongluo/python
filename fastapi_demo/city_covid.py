from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None

@app.get('/')
def hello_world():
    return {'hello', 'world'}

@app.get('/city/{city}')
def path_variable(city: str):
    return {'city': city}

@app.get('/city')
def query_variable(query_string: Optional[str] = None):
    return {'query_string': query_string}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)