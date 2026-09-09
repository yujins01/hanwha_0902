from fastapi import FastAPI,HTTPException
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello~~"}

@app.get("/user/")
async def ice_name():
    return {"message": "어서오십시오"}

class Color(str, Enum):
    R = 'Red'
    G = "Green"
    B = 'Blue'

@app.get("/name/")
async def get_color(color: Color):
    return{"color": color.value}


#요청 받을 데이터 구조 정의
class UserInfo(BaseModel):
    name: str
    email: str
    age: int

#경로 파라미터 + 쿼리 파라미터 + body 동시처리?
@app.post("/users/{user_id}")
async def user_profile(
    user_id: int, #경로 파라미터
    user_info: UserInfo, #body(Json)
    send: bool = True # 쿼리 파라미터
):

    return{
        "msg": "어서오십시오",
        "ststus": "success",
        "assigned_id": user_id,
        "profile": user_info,
        "sent": send
    }

#===========================#
# 물품 등록, 조회, 변환, 삭제
#===========================#

#메모리용 가상 데이터베이스 (물품 저장소)
item_db = {}

#1. 물품 데이터 구조 정의 (Pydantic Model)
class ItemInfo(BaseModel):
    name: str
    price: int
    stock: int

#2. 물품 등록(post)
@app.post("/items/{item_id}")
async def create_item(
        item_id: int,
        item_info: ItemInfo,
        is_discount: bool = False
):
    #할인 적용 요청시 10% 할인가 계산
    final_price = item_info.price
    if is_discount:
        final_price = int(item_info.price * 0.9)

    #가상 DB에 저장
    item_db[item_id] = {
        "info": item_info,
        "final_price": final_price,
        "is_discount": is_discount
    }

    return {
        "msg": "물품이 등록되었습니다.",
        "item_id": item_id,
        "registered_data": item_db[item_id]
    }

#3. 물품 조회 get
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in item_db:
        #HTTPException -> fastapi가 제공하는 예외 클래스
        #fastapi가 자동으로 깔끔한 에러 응답 형태로 변환
        #에러가 실행되면 코드를 404로 성정하고 뒤에 말로 JSON 응답변화
        raise HTTPException(status_code=404, detail="물품을 찾을 수 없습니다.")

    return{
        "item_id": item_id,
        "item_details": item_db[item_id]
    }

#4.물품 수정(PUT)
@app.put("/items/{item_id}")
async def update_item(
    item_id:int,
    item_info: ItemInfo,
    is_discount: bool = False
):
    #수정하려는 물품이 존재하지 않을 경우
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="수정할 물품이 존재하지 않습니다.")

    #할인가 재계산 및 데이터 덮어쓰기(update)
    final_price = int(item_info.price*0.9) if is_discount else item_info.price

    item_db[item_id] = {
        "info": item_info,
        "final_price": final_price,
        "is_discount": is_discount
    }
    #수정 완료 결과 반환
    return{
        "mgs":"물품 정보가 수정되었습니다",
        "item_id":item_id,
        "update_data": item_db[item_id]
    }

#5.물품삭제(delete)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="물품을 찾을 수 없습니다.")

    delete_item = item_db.pop(item_id)
    return{
        "msg":f"{item_id} 물품이 삭제되었습니다.",
        "delete_item": delete_item
    }