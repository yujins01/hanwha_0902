# 2. 실전: 기본값, Optional, 중첩모델

from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150) #0이상 150이하 정수
    email: str
    address: Address
    nickname: str|None = None #허용 되는 데이터 타입은 문자열이거나 None, 기본 값은 None

user = User(
    name="Alice",
    age=25,
    email="alice@example.com",
    address={
        "city": "Daejeon",
        "zip_code": "34100",
    },
)

print(user)
print(user.address.city)
print(user.nickname)

# ------
# name='Alice' age=25 email='alice@example.com' address=Address(city='Daejeon', zip_code='34100') nickname=None
# Daejeon
# None
# # -----