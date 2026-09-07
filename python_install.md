# Python Install

---

## 1. Python & VS Code 설치

### 1-1. Python 설치

본 과정에서는 **Python 3.12.10** 버전을 설치한다.

- 개발 환경의 안정성, 라이브러리 호환성, 다양한 레퍼런스를 고려하여 `Python 3.12.10` 버전을 선택한다.

### ✅ 설치 확인

1. **시스템 환경 변수 편집 → 환경 변수 → Path**에 Python 경로가 등록되어 있는지 확인한다.
2. CMD 창을 실행한다.
3. 다음 명령어를 입력한다.

```cmd
python --version
```

4. 다음과 같이 Python 버전이 출력되면 정상적으로 설치된 것이다.

```text
Python 3.12.10
```

---

## 2. VS Code 설치

VS Code 설치 후, 한국어 환경과 Python 개발을 위해 **확장 프로그램(Extension)**을 설치한다.

### 주요 Extension

1. **Korean Language Pack**
   - VS Code를 한국어 환경으로 설정

2. **Python**
   - VS Code에서 Python 개발 지원

---

## 3. Python 버전 확인

VS Code에서 Python 개발 환경을 설정하기 전에 **CMD에서 설치한 Python 버전과 동일한 버전이 선택되어 있는지 확인**한다.

```cmd
python --version
```

```text
Python 3.12.10
```

📌 CMD에서 확인한 Python 버전과 VS Code에서 사용하는 Python 버전이 동일한지 확인한다.

---

## 4. 프로젝트 폴더 생성

Python 프로젝트를 관리하기 위한 **프로젝트 폴더**를 생성한다.

```text
📁 프로젝트 폴더
├─ 📁 py
└─ 📁 .venv
```

- `py` → Python 파일을 저장하는 폴더
- `.venv` → Python 가상환경 폴더

---

## 5. 가상환경 생성

### 💡 가상환경을 사용하는 이유

**프로젝트별로 독립된 Python 개발 환경을 만들어 라이브러리 간 충돌을 방지하기 위해 사용한다.**

### 5-1. 가상환경 생성

프로젝트 폴더에서 다음 명령어를 입력한다.

```cmd
python -m venv .venv
```

실행하면 `.venv`라는 가상환경이 생성된다.

---

## 6. 가상환경 활성화

가상환경을 사용하기 위해서는 먼저 **가상환경을 활성화**해야 한다.

Windows CMD에서는 다음과 같이 입력한다.

```cmd
.venv\Scripts\activate.bat
```

활성화되면 터미널 앞에 가상환경 이름이 표시된다.

```text
(.venv) D:\프로젝트폴더>
```

📌 `(.venv)`가 표시되면 현재 가상환경이 활성화된 상태이다.

> 가상환경 이름은 생성할 때 지정한 이름에 따라 달라질 수 있다.

### 가상환경 비활성화

가상환경 사용을 종료하려면 다음 명령어를 입력한다.

```cmd
deactivate
```

---

## ⭐ Python 개발환경 핵심

```text
Python 설치
    ↓
VS Code 설치
    ↓
Python Extension 설치
    ↓
프로젝트 폴더 생성
    ↓
가상환경 생성
    ↓
가상환경 활성화
    ↓
Python 개발 시작
```

📌 **가상환경 = 프로젝트별로 독립적인 Python 개발 환경을 만들어 라이브러리 충돌을 방지하는 것**
