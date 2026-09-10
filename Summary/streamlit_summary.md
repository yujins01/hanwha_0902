# Streamlit 정리

---

### Streamlit 이란?

> Python을 이용하여 웹 애플리케이션을 쉽게 만들 수 있도록 도와주는 프레임워크, 웹페이지의 UI를 구성할 수 있음

#### Streamlit 설치

```python
pip install streamlit
```

#### Streamlit 실행 방법

```python
streamlit run [파일명].py
```

#### Streamlit 기본 구조

```python
import streamlit as st
```

#### Streamlit 기본 출력 문법

#### 1. 제목 및 텍스트

| 문법 | 설명 |
|---|---|
| `st.title()` | 가장 큰 제목 |
| `st.header()` | 헤더 |
| `st.subheader()` | 하위 헤더 |
| `st.write()` | 텍스트, 변수, 데이터 등 출력 |
| `st.markdown()` | Markdown 형식으로 출력 |
| `st.text()` | 일반 텍스트 출력 |
| `st.caption()` | 작은 보조 문구 출력 |

#### 2. 사용자 입력

| 문법 | 설명 |
|---|---|
| `st.text_input()` | 텍스트 입력 |
| `st.number_input()` | 숫자 입력 |
| `st.text_area()` | 여러 줄의 텍스트 입력 |
| `st.button()` | 버튼 |
| `st.checkbox()` | 체크박스 |
| `st.radio()` | 여러 항목 중 하나 선택 |
| `st.selectbox()` | 드롭다운 메뉴에서 하나 선택 |
| `st.multiselect()` | 여러 항목 선택 |
| `st.slider()` | 슬라이더를 이용한 값 선택 |
| `st.date_input()` | 날짜 입력 |
| `st.time_input()` | 시간 입력 |
| `st.file_uploader()` | 파일 업로드 |

#### 3. 화면 구성

### Columns

```python
st.columns()
```

→ 화면을 여러 개의 열로 나눌 때 사용

### Container

```python
st.container()
```

→ 여러 요소를 하나의 영역으로 묶을 때 사용

### Sidebar

```python
st.sidebar
```

→ 화면 왼쪽의 사이드바 영역 사용

### Expander

```python
st.expander()
```

→ 내용을 접었다 펼칠 수 있는 영역 생성

### `with`

```python
with 영역:
```

→ 특정 영역 안에서 코드를 실행할 때 사용

#### 4. 데이터 출력

> pandas DataFrame과 함께 사용
>
> 데이터 분석 결과를 웹 화면에 쉽게 출력

| 문법 | 설명 |
|---|---|
| `st.dataframe()` | DataFrame을 표 형태로 출력 |
| `st.table()` | 데이터를 정적인 표로 출력 |
| `st.metric()` | 주요 수치나 지표를 표시 |
| `st.json()` | JSON 데이터를 출력 |

#### 5. 그래프 및 시각화

| 문법 | 설명 |
|---|---|
| `st.line_chart()` | 선 그래프 |
| `st.bar_chart()` | 막대 그래프 |
| `st.area_chart()` | 영역 그래프 |
| `st.pyplot()` | Matplotlib 그래프 출력 |
| `st.plotly_chart()` | Plotly 그래프 출력 |

#### 6. 이미지 및 미디어

| 문법 | 설명 |
|---|---|
| `st.image()` | 이미지 출력 |
| `st.audio()` | 오디오 출력 |
| `st.video()` | 동영상 출력 |

#### 7. 상태 관리

```python
st.session_state
```

→ 사용자의 입력이나 특정 데이터를 페이지가 다시 실행돼도 유지하기 위해 사용

→ 값을 지속적으로 유지하기 위해 사용
