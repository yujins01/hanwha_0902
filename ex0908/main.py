from fastapi import FastAPI
from enum import Enum
#http://localhost:8000/docs
#http://localhost:8000/redoc
#Enum class 선언
class ModelName(str, Enum):
    aaa = "aleznet"
    r = "resnet"
    l = "lenet"
    기타 = "기타"

app = FastAPI()

#http://localhost:8000/
@app.get("/") #웹 경로 요청
def read_root():
    return {"Hello": "world"} #이걸로 실행

#http://localhost:8000/items/{555}
@app.get("/items/{item_id}") #이 경로로 보내면
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q} #일로 실행

#http://localhost:8000/users/me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

#http://localhost:8000/users/사용자
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"사용자 user_id": user_id}


#http://localhost:8000/users 요청 url(경로)
@app.get("/users")
async def read_users():
    return [ 'Rick', "Morty"]

#http://localhost:8000/users 위에 꺼랑 경로가 같기때문에 무시됨.
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

#http://localhost:8000/models/{aaa}
#http://localhost:8000/models/{resnet}
#http://localhost:8000/models/{lenet}
#http://localhost:8000/models/{기타}
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    #키를 요청하면, 값을 return
    if model_name is ModelName.aaa:
        return {"model_name": model_name, "message":"키요청: Deep Learing FTW!"}
    
    #값을 요청하면, 키를 return
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "값요청: LeCNN all the images"}
    
    #그 외의 상황 
    return {"model_name": model_name, "message": "그외에: Have some residuals"}

#http://localhost:8000/items
fake_items_db = [{"item_name": "Foo"},{"item_name": "Bar"},{"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
    #범위연산자
    #return fake_items_db[0:1]

#http://localhost:8000/items2/test
#http://localhost:8000/items2/test?q=None
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str|None = None):
    if q:
        return {"item_id": item_id, "q":q}
    return {"item_id": item_id}

#