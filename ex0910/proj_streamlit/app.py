import streamlit as st
import requests #요청 보낼 수 있는 라이브러리

#Fastapi 백엔드 URL
FASTAPI_URL = "http://127.0.0.1:8000"

st.title("Streamlit & FastAPI 연결 예제")

#입력 폼 구성
with st.form("user_form"):
    name = st.text_input("이름", value="홍길동")
    age = st.number_input("나이", min_value=1,max_value=120, value=20)
    submit_button = st.form_submit_button("백엔드로 전송")

if submit_button:
    #Fastapi로 보낸 데이터 페이로드
    payload = {
        "name": name,
        "age": age
    }

    try:
        #fastapi/predict 앤드포인트에 POST 요청
        response = requests.post(f"{FASTAPI_URL}/predict",json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("FASTAPI  응답 성공!")
            st.write(f"**결과:**{result['result_message']}")
        else:
            st.error(f"오류 발생 (상태 코드:{response.status_code})")

    except requests.exceptions.RequestException as e:
        st.error(f"FastAPI 요철 중 오류가 발생했습니다: {e}")





#http://localhost:8501/
with st.chat_message("user"):
    st.write("Hello 👋")

prompt = st.chat_input("무엇이든 물어보세요")
if prompt:
    st.write(f"사용자: {prompt}")