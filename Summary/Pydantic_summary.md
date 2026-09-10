# Pydantic

---

💡**pydantic이란?**

> Python의 **타입 힌트(Type Hint)**를 기반으로 **데이터의 유효성을 검사**(Validation)하고, 데이터를 원하는 형태로 변환·**직렬화(Serialization)**할 수 있도록 도와주는 라이브러리

**사용 이유**

> 내가 정해놓은 데이터 형식에 맞게 값이 들어왔는지 확인하기 위해
>
> 주로 API, JSON, 데이터 처리에서 사용

**흐름**

> 외부 데이터
>
> ↓
>
> Pydantic Model
>
> ↓
>
> 데이터 검증 (Validation)
>
> ↓
>
> 정상 → 사용
>
> 오류 → ValidationError
>
> ↓
>
> 필요하면 직렬화
>
> ↓
>
> Dictionary / JSON

#### 1. 데이터 구조 정의 + 타입 지정

> **`BaseModel`**과 **Type Hint**를 이용해 내가 원하는 데이터의 구조와 타입을 정의

```python
from pydantic import BaseModel 

class User(BaseModel):
    name: str
    age: int
```

- `BaseModel` → Pydantic 모델을 만들기 위한 기본 클래스 (데이터 검증)
- `name: str`, `age: int` → 각 데이터의 타입 지정

#### 2. 데이터 검증 + 조건 설정

> 정의한 모델에서 데이터가 들어오면 Pydantic이 타입과 조건에 맞는지 검사

```python
from pydantic import Field

class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0)
```

- `Field` → 타입만으로 표현하기 어려운 추가 조건을 설정 가능
- name → 문자열 + 최소 2글자
- age → 정수 + 0보다 커야함

**⭐ Type Hint + Field → 데이터가 가져야 할 구체적인 조건 설정**

#### 3. 특수한 조건을 타입으로 지정

> 자주 사용하는 조건은 pydantic이나 Python의 타입을 이용해서 더 간단히 표현

```python
from pydantic import PositiveInt
from typing import Literal, Annotated
from annotated_types import Gt

class User(BaseModel):
    age: PositiveInt
    gender: Literal["male", "female"]
```

- `PositiveInt` → 0보다 큰 정수
- `Literal` → 지정한 값만 허용
- `Annotated` → 기존 타입에 추가 조건을 붙일 때 사용
- `Gt` → `>` 조건

#### 4. 데이터 검증 실패 처리

> 입력된 데이터가 우리가 정한 규칙에 맞지 않으면 `ValidationError` 발생

```python
from pydantic import ValidationError

try:
    user = User(
        name="길",
        age=-1
    )
except ValidationError as e:
    print(e)
```

- **`except ValidationError`** → 검증 오류가 발생하면 잡기
- `e` = 어떤 검증 오류가 발생했는지 담고 있는 변수
- `print(e)` → 문자열 형태의 전체적인 에러 메시지
- `print(e.errors())`
  - 리스트 + 딕셔너리 형태의 데이터로 오류를 보여줌
  - 어떤 필드에서 오류가 발생했는지 자세히 확인하거나 처리할 때 좋음

#### 5. 데이터 변환 + 직렬화

> 검증이 끝난 Pydantic의 모델을 필요에 따라 사용하기 좋은 데이터 형태로 변환

- `user.model_dump()` → 딕셔너리
- `user.model_dump_json()` → JSON

#### 6. 딕셔너리 데이터를 모델에 전달

> 클래스의 필드에 넣을 값을 원래 하나씩 지정해야 하지만,
>
> 딕셔너리에 `key: value` 형태로 값이 이미 들어 있다면 `**`를 사용해서 한 번에 전달 가능

```python
external_data = {
    "name": "길동",
    "age": 20
}

user = User(**external_data)
```

☑️ **딕셔너리를 클래스에 한 번에 넣어주는 것**
