import datetime
import pytest
import json

from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Body, Header, Response
from pydantic import BaseModel

app = FastAPI()


@app.get("/hi")
def greet():
    return "Hello? World?"


# Query Parameters
@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"


# # Url path
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"


# # Body parameter
@app.post('/hi')
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}?"

# HTTP Header
@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

# Status code specification
@app.get("/happy")
def happy(sad:str = Header, status_code=201):
    return f"{status_code}? :)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"


@pytest.fixture
def data():
    return datetime.datetime.now()


def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)


def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out

# Model types and response_model



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("hello:app", reload=True)
