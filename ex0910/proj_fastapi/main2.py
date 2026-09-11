from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Streamlit에서 받을 데이터
class ChatInput(BaseModel):
    message: str


# 응원 메시지
cheer_messages = [
    "오늘도 충분히 잘하고 있어요! 💪",
    "조금씩 해도 괜찮아요. 꾸준함이 가장 중요해요! 🌱",
    "지금까지 노력한 만큼 분명 좋은 결과가 있을 거예요! 😊",
    "포기하지 마세요! 끝까지 응원할게요! 🔥",
    "오늘도 한 걸음씩 나아가고 있어요! 🚶"
]


@app.get("/")
def read_root():
    return {"message": "응원 챗봇 서버가 정상 작동 중입니다."}


@app.post("/cheer")
def get_cheer(data: ChatInput):

    # 랜덤으로 응원 메시지 선택
    answer = random.choice(cheer_messages)

    return {
        "status": "success",
        "user_message": data.message,
        "answer": answer
    }