import streamlit as st #Streamlit
import pandas as pd #데이터 분석 및 DataFrame 생성
import numpy as np #배열 및 수치 계산


# ==========================================
# 1. DataFrame 생성 및 출력
# ==========================================

# Pandas를 이용하여 DataFrame 생성
df = pd.DataFrame({
    'first colum': [1,2,3,4], 'second colum': [10,20,30,40]
})
df # Streamlit에서는 DataFrame을 변수명만 작성해도 화면에 출력 가능

st.write("안녕") # st.write()를 이용하여 텍스트 출력


# ==========================================
# 2. DataFrame 표시
# ==========================================

# dataframe = np.random.randn(10,20)
# st.dataframe(dataframe)

# NumPy의 random.randn()을 이용하여 10행 20열의 랜덤 데이터 생성
dataframe = pd.DataFrame(
    np.random.randn(10,20), columns=('col %d' %i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0)) # DataFrame에서 각 열(column)의 최댓값을 강조하여 표시
st.table(dataframe) # DataFrame을 표(table) 형태로 표시

# ==========================================
# 3. 선 그래프
# ==========================================

# 20행 3열의 랜덤 데이터를 DataFrame으로 생성
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data) # DataFrame의 데이터를 선 그래프로 표시

# ==========================================
# 4. 지도
# ==========================================

# 위도(lat), 경도(lon) 데이터를 생성
# 지도에 표시할 위치 정보를 DataFrame으로 저장
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']
)

st.map(map_data) # 위도와 경도 데이터를 지도에 표시

# ==========================================
# 5. 텍스트 입력 위젯
# ==========================================

x = st.slider('x') # 사용자가 값을 직접 선택할 수 있는 슬라이더 생성
st.write(x, 'squared is', x * x) # 선택한 값과 제곱한 결과를 화면에 출력

st.text_input("Your name", key="name") # 사용자가 이름을 입력할 수 있는 입력창 생성
st.session_state.name # session_state를 이용하여 입력된 이름 확인


# ==========================================
# 6. 체크박스
# ==========================================

# 체크박스를 생성하고 체크된 경우에만 아래 코드를 실행
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 4), # 20행 4열의 랜덤 데이터 생성
        columns=['a','b','c','d']
    )
    chart_data # 체크박스가 선택되었을 때 DataFrame 표시
    

# ==========================================
# 7. 옵션 선택 상자 (Selectbox)
# ==========================================

# 선택 상자에 사용할 DataFrame 생성
df2 = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

# selectbox를 이용하여 목록에서 하나의 값을 선택
option = st.selectbox(
    '어떤 것을 가장 좋아하시나요?',
    df2['first column']
)
"당신의 선택: ", option # 사용자가 선택한 값 출력

# ==========================================
# 8. 진행 상황 표시
# ==========================================

import time # 시간 지연을 위해 time 모듈 사용

"진행 상황"
latest_iteration = st.empty() # 진행 상황을 표시할 빈 공간 생성
bar = st.progress(0) # 0부터 100까지 진행되는 Progress Bar 생성

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') # 현재 반복 횟수를 화면에 표시
    bar.progress(i+1) # Progress Bar를 현재 진행률로 업데이트
    time.sleep(0.1)  # 0.1초 동안 대기

"...끝!"
