import streamlit as st #웹 어플리케이션 라이브러리
import pandas as pd #데이터를 표 형태로 다루는 라이브러리
import numpy as np #배열 및 수치 계산 라이브러리

st.title("한화 내일배움 교육 :eagle:")
st.subheader("교육생 관리 시스템")
st.write("")

#현재 상태를 저장한 공간, 현재 로그인 되지 않은 상태
if "login" not in st.session_state: 
    st.session_state.login = False

# 로그인 전
if not st.session_state.login:

    if st.button("Login"):
        st.session_state.login = True #버튼을 눌러 로그인 됐기에 True(로그인 됨)
        st.rerun()

# 로그인 후
else:

    st.write("환영합니다! :clap:")

    st.divider() #구분선

    st.subheader(":calendar: 출결 현황")

    total_days  = 50 #총 일수
    attendance = [] #출석한 일수

    #50일의 출결 체크 박스
    for row in range(5): #행 5개
        col=st.columns(10) #10개의 열을 만들기 위해 화면을 10개의 열로 나눔

        for i in range(10): #10개로 나눈 각 칸을 하나씩 사용
            with col[i]:    #선택한 칸에 아래 내용 넣기
                day = row * 10 + i + 1          #각 칸에 일 수
                check = st.checkbox(f"{day}일") #체크박스 만듦
                attendance.append(check) #출석한 일 수를 참석에 추가

    #출석률 계산
    attendance_days = sum(attendance)
    attendance_rate = attendance_days/total_days

    st.progress(attendance_rate)
    st.write(f"출석률: {attendance_rate * 100: .0f}%")
