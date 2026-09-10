# 3. API 요청 -> 검증 -> 데이터 변환

from pydantic import BaseModel, Field

#SignupRequest는 pydantic 모델 데이터 클래스를 만듬
class SignupRequest(BaseModel): 
    username: str = Field(min_length=3, max_length=20) 
    password: str = Field(min_length=8)
    age: int = Field(ge=14)

#signup함수의 data에는 SignupRequest 형태의 데이터를 받겠다.
#data: SignupRequest는 타입 힌트
#검증된 데이터를 받아서 사용
def signup(data: SignupRequest):
    print("회원가입 처리")
    print(f"username: {data.username}")
    print(f"age: {data.age}")

#실제 데이터를 넣는곳
#SignupRequest라는 pydatic 모델에 실체 데이터를 넣으면서 검증
#정상이며 객체 생성, 오류면 오류 발생
#검증이 끝난 request를 함수 signup에 전달
request = SignupRequest( 
    username="alice",
    password="12345678",
    age=25,
)

signup(request)

# -----
# 회원가입 처리
# username: alice
# age: 25
# # -----