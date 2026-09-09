from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

#데이터용
class ItemSchema(BaseModel):
    name: str
    price: float
    description: str | None = None

item_db:dict[int, dict] = {}
id_counter = 1

#생성 Create
#http://127.0.0.1:8000/items/
@app.post("/items/", status_code=201) # 요청에 성공, 새로운 리소스 생성
async def create_item(item: ItemSchema):
    global id_counter
    new_item = item.model_dump()  # 입력한 데이터
    new_item["id"] = id_counter   # 

    item_db[id_counter] = new_item
    id_counter += 1

    #return item_db


#조회 (전체) Read
#http://127.0.0.1:8000/items/
@app.get("/items/")
async def get_all_items():
    return{"msg":"정체 목록 조회 완료","data":list(item_db.values())} #list를 소괄호로하면 새로운 list 생성?


#조회 (단일) Read
#http://127.0.0.1:8000/items/1
@app.get("/items/{item_id}")
async def get_item(item_id:int):
    if item_id not in item_db:
        raise HTTPException(status_code=404,detail="제품을 찾을 수 없습니다")

    return{"message":"단일 조회 완료","data":item_db[item_id]}

#수정 Update
#http://127.0.0.1:8000/items/1
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema):

    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="물건을 찾을 수 없습니다")

    update_data = item.model_dump()
    update_data["id"] = item_id #입력 받은 id를 넣어줌
    item_db[item_id] = update_data #수정한 것을 db에 넣어줌

    return{"msg":"수정 완료", "data":update_data}


#삭제 Delete
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):

    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="물건을 찾을 수 없습니다")

    delete_item = item_db.pop(item_id)
    return{"msg":"삭제 완료", "data":delete_item}

