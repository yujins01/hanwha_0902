import streamlit as st
import requests


# FastAPI 주소
FASTAPI_URL = "http://127.0.0.1:8000"


st.title("🤖 랜덤 응원 챗봇")
st.write("힘이 필요할 때 메시지를 보내보세요! 💪")


# 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []


# 기존 대화 출력
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# 사용자 입력
user_message = st.chat_input("메시지를 입력하세요...")


if user_message:

    # 사용자 메시지 화면에 출력
    with st.chat_message("user"):
        st.write(user_message)

    # 대화 기록에 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })


    # FastAPI로 보낼 데이터
    payload = {
        "message": user_message
    }


    try:

        # FastAPI에 POST 요청
        response = requests.post(
            f"{FASTAPI_URL}/cheer",
            json=payload
        )


        # 응답 성공
        if response.status_code == 200:

            result = response.json()

            answer = result["answer"]


            # 챗봇 답변 출력
            with st.chat_message("assistant"):
                st.write(answer)


            # 대화 기록 저장
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })


        else:

            st.error(
                f"오류 발생! 상태 코드: {response.status_code}"
            )


    except requests.exceptions.RequestException as e:

        st.error(f"FastAPI 요청 오류: {e}")