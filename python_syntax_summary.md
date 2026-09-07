# 파이썬 문법 정리

---

## 1. 변수, 출력, 주석, 데이터 형식

### 1-1. 변수, 출력

변수에 값을 저장하고 `print()`를 이용하여 결과를 출력할 수 있다.

- **변수**: 데이터를 저장하는 공간
- `print()`: 변수나 값을 출력하는 함수

**💡 `print()`에서 `sep`을 사용하면 여러 값 사이에 원하는 문자를 넣을 수 있다.**

```python
print("파이썬 기본 문법", 8, sep=", 시간:")

출력: 파이썬 기본 문법, 시간:8
```

### 1-2. 주석

- **주석**은 `#`을 이용해서 사용
- 전체 주석을 하고 싶은 경우 `Ctrl + /`를 통해 가능

### 1-3. 데이터 형식

변수에 저장된 **데이터의 자료형**을 확인할 수 있다.

| 자료형 | 의미 | 예시 |
|---|---|---|
| `str` | 문자열 | `"Python"` |
| `int` | 정수 | `10` |
| `float` | 실수 | `3.14` |
| `bool` | 참/거짓 | `True`, `False` |
| `list` | 여러 데이터를 순서대로 저장 | `[1, 2, 3]` |
| `dict` | Key와 Value를 저장 | `{"name": "Yujin"}` |

📌 `type()`을 사용하면 변수에 저장된 데이터의 **자료형(Type)**을 확인할 수 있다.

```python
print(type(x))

출력 예시)
<class 'str'>
<class 'int'>
```

---

## 2. 문자열 (String)

- 문자열: `" "` 또는 `' '`를 사용하여 표현
- 문자열의 길이를 구하기 위해서는 `len()` 사용

```python
a = "Hello, World!"

print(a[1])
print(len(a))

출력:
e
13
```

### 2-1. 문자열 인덱싱

문자열의 각 문자에 번호를 부여하여 특정 문자에 접근할 수 있다.

> 📌 인덱스는 0부터 시작  
> 📌 `문자열[시작:끝]`에서 끝 인덱스는 포함하지 않는다.

```python
a = "Python"

print(a[1])      # y
print(a[-1])     # n

print(a[0:3])    # Pyt
print(a[:3])     # Pyt
print(a[3:])     # hon
print(a[::-1])   # nohtyP
```

### 2-2. 문자열 메서드

| 메서드 | 설명 | 예시 |
|---|---|---|
| `.upper()` | 대문자로 변환 | `"python".upper()` → `PYTHON` |
| `.lower()` | 소문자로 변환 | `"PYTHON".lower()` → `python` |
| `.replace()` | 문자열 변경 | `"I like Python".replace("Python", "Java")` |
| `.split()` | 문자열을 나눠 리스트로 변환 | `"A B C".split()` → `['A', 'B', 'C']` |
| `.strip()` | 앞뒤 공백 제거 | `" Python ".strip()` → `Python` |

### 2-3. 문자열 포함 여부

> **`in`을 사용하면 특정 문자열이 포함되어 있는지 확인할 수 있다.**

```python
text = "I love Python"

print("Python" in text)  # True
print("Java" in text)    # False
```

### 2-4. f-string

> **문자열 안에 변수나 값을 쉽게 넣을 수 있는 방법**
>
> 문자열 앞에 `f`를 붙이고 `{}` 안에 변수를 넣는다.

```python
name = "홍길동"
age = 25

print(f"이름: {name}, 나이: {age}")

출력:
이름: 홍길동, 나이: 25
```

📌 `f"문자열 {변수}"` 형태로 사용한다.

---

## 3. 리스트 (List)

> 리스트는 여러 개의 데이터를 하나의 변수에 순서대로 저장할 수 있는 자료형

```python
numbers = [1, 2, 3, 4, 5]
```

- `[]`를 사용하여 표현
- 데이터의 순서가 존재
- 인덱스는 0부터 시작
- 여러 종류의 데이터를 함께 저장할 수 있음
- 리스트의 값은 수정 가능함

### 3-1. 리스트 값 수정

> 리스트는 인덱스를 이용하여 값을 수정할 수 있다.

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "grape"

print(fruits)

출력:
['apple', 'grape', 'orange']
```

📌 문자열은 인덱스로 개별 문자를 수정할 수 없지만, 리스트는 수정 가능하다.

### 3-2. 리스트 주요 메서드

| 메서드 | 설명 |
|---|---|
| `.append()` | 마지막에 데이터 추가 |
| `.insert()` | 원하는 위치에 데이터 추가 |
| `.extend()` | 여러 데이터 추가 |
| `.remove()` | 특정 값 삭제 |
| `.pop()` | 특정 위치의 값 삭제 |
| `.sort()` | 오름차순 정렬 |
| `.reverse()` | 순서 뒤집기 |
| `.count()` | 특정 값의 개수 확인 |
| `.index()` | 특정 값의 위치 확인 |

**💡 문자열과 리스트의 공통점**

> **문자열과 리스트는 둘 다 인덱싱과 슬라이싱이 가능하다.**

**💡 문자열과 리스트의 차이점**

> **문자열 → 수정 불가능**  
> **리스트 → 수정 가능**

---

## 4. 조건문

> **조건문은 조건에 따라 다른 코드를 실행할 때 사용**

- **`if`**: 조건이 **참(True)**이면 코드를 실행한다.

```python
age = 20

if age >= 20:
    print("성인입니다.")
```

📌 조건 뒤에 `:`을 작성하고, 실행할 코드는 들여쓰기한다.

### 4-1. if / elif / else

- `if` → 첫 번째 조건
- `elif` → 추가 조건
- `else` → 모든 조건이 거짓일 때

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

### 4-2. 비교 연산자

> **조건을 비교할 때 사용**

| 연산자 | 의미 |
|---|---|
| `==` | 같다 |
| `!=` | 같지 않다 |
| `>` | 크다 |
| `<` | 작다 |
| `>=` | 크거나 같다 |
| `<=` | 작거나 같다 |

### 4-3. 논리 연산자

> 여러 조건을 함께 사용할 때 사용

| 연산자 | 의미 |
|---|---|
| `and` | 모두 참이어야 `True` |
| `or` | 하나라도 참이면 `True` |
| `not` | `True` ↔ `False` 반전 |

### ⭐ 조건문 핵심

```text
if       → 조건이 참일 때
elif     → 추가 조건
else     → 모든 조건이 거짓일 때

==       → 같다
!=       → 같지 않다
> / <    → 크다 / 작다
>= / <=  → 크거나 같다 / 작거나 같다

and      → 모두 참
or       → 하나라도 참
not      → 조건 반전
```

📌 **조건문 = "조건이 맞으면 이걸 실행하고, 아니면 저걸 실행"**

---

## 5. 반복문 (for / while)

> 반복문은 **같은 코드를 여러 번 실행**할 때 사용

### 5-1. `for`

`for`문은 여러 데이터를 **하나씩 꺼내 반복적으로 처리**할 때 사용한다.

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

출력:
apple
banana
orange
```

문자열도 반복할 수 있다.

```python
for char in "Python":
    print(char)
```

### `range()`

`range()`는 정해진 횟수만큼 반복할 때 사용한다.

```python
for i in range(5):
    print(i)

출력:
0
1
2
3
4
```

📌 `range(5)`는 **0부터 4까지** 반복한다.

```python
for i in range(1, 6):
    print(i)

출력:
1
2
3
4
5
```

### 5-2. `while`

> 조건이 **참인 동안 계속 반복**

```python
count = 0

while count < 3:
    print(count)
    count += 1

출력:
0
1
2
```

📌 `while`문에서는 조건이 언젠가 거짓이 되도록 값을 변경해야 한다.  
그렇지 않으면 무한 반복이 발생할 수 있다.

### 5-3. `break / continue`

- `break`: 반복문을 즉시 종료

```python
for i in range(5):
    if i == 3:
        break
    print(i)

출력:
0
1
2
```

- `continue`: 현재 반복만 건너뛰고 다음 반복을 실행

```python
for i in range(5):
    if i == 2:
        continue
    print(i)

출력:
0
1
3
4
```

---

## 6. 함수 (Function)

> 반복해서 사용하거나 하나의 기능으로 묶고 싶은 코드를 **함수로 정의하여 재사용**할 수 있다.

- `def`를 사용하여 함수를 정의
- 함수 이름을 호출하여 실행

```python
x = "awesome"

def myfunc():
    x = "111"
    print("Python is " + x)

myfunc()

print("music is " + x)

출력:
Python is 111
music is awesome
```

📌 함수 안에서 정의한 변수는 함수 밖의 변수와 별개로 사용할 수 있다.

### `return`

> `return`은 함수에서 계산한 **결과를 반환**할 때 사용한다.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

출력:
30
```

---

## 7. Class (객체 지향)

> 클래스는 **객체를 만들기 위한 설계도**이다.
>
> 예를 들어 `Person`이라는 클래스를 만들고, 이를 이용해 여러 객체를 만들 수 있다.

### 7-1. 객체 생성

클래스를 이용해 실제 객체를 만드는 것을 **객체 생성**이라고 한다.

```python
class Person:
    pass

person1 = Person()
person2 = Person()
```

`Person()`을 호출하면 `Person` 클래스를 기반으로 객체가 생성된다.

```text
Person 클래스
     ↓
  객체 생성
  ↙      ↘
person1  person2
```

### 7-2. 속성 (Attribute)

객체가 가지고 있는 **데이터**를 속성이라고 한다.

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

객체를 생성할 때 값을 전달한다.

```python
person = Person("Yujin", 25)

print(person.name)
print(person.age)

출력:
Yujin
25
```

여기서 `name`, `age`가 객체의 **속성**이다.

### 7-3. 메서드 (Method)

클래스 안에 정의된 **함수**를 메서드라고 한다.

```python
class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"저는 {self.name}입니다.")
```

객체를 통해 메서드를 호출할 수 있다.

```python
person = Person("Yujin")

person.introduce()

출력:
저는 Yujin입니다.
```

📌

```text
함수   → 클래스 밖에서 정의
메서드 → 클래스 안에서 정의
```

### 7-4. `self`

`self`는 **현재 객체 자신**을 의미한다.

```python
class Person:

    def __init__(self, name):
        self.name = name
```

```text
name       → 전달받은 값
self.name  → 현재 객체의 속성
```

```python
person = Person("Yujin")

print(person.name)

출력:
Yujin
```

📌 `self`를 통해 **현재 객체의 속성이나 메서드에 접근**할 수 있다.

### 7-5. 부모 클래스와 자식 클래스

클래스는 다른 클래스를 **상속(Inheritance)**받을 수 있다.

- **부모 클래스** → 기존 기능을 가지고 있는 클래스
- **자식 클래스** → 부모 클래스의 기능을 물려받는 클래스

```python
class Animal:

    def eat(self):
        print("먹습니다.")


class Dog(Animal):

    def bark(self):
        print("멍멍!")
```

`Dog`는 `Animal`을 상속받았기 때문에 `eat()`을 사용할 수 있다.

```python
dog = Dog()

dog.eat()
dog.bark()

출력:
먹습니다.
멍멍!
```

```text
Animal
  ↓ 상속
 Dog
```

### 7-6. `super()`

자식 클래스에서 **부모 클래스의 메서드나 생성자를 호출**할 때 사용한다.

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

```python
dog = Dog("초코", "푸들")

print(dog.name)
print(dog.breed)

출력:
초코
푸들
```

📌 `super()` → 부모 클래스의 기능을 사용

### ⭐ Class 핵심

```text
Class       → 객체를 만들기 위한 설계도

Object      → 클래스를 이용해 만든 실제 객체

객체 생성   → Person()

속성        → 객체가 가지고 있는 데이터
             self.name
             self.age

메서드      → 클래스 안에 정의된 함수

self        → 현재 객체 자신

부모 클래스 → 기능을 물려주는 클래스

자식 클래스 → 부모의 기능을 물려받는 클래스

상속        → 부모 클래스의 기능을 자식 클래스가 사용

super()     → 부모 클래스의 기능을 호출
```

### 💡 한 번에 이해하기

```text
             부모 클래스
               Animal
                  │
                상속
                  ↓
              자식 클래스
                 Dog
                  │
            ┌─────┴─────┐
            ↓           ↓
          속성         메서드
        self.name      bark()
```

**핵심은 `class → 객체 → 속성 → 메서드 → self → 상속` 순서로 이해하는 것.**

---

## 8. NumPy

**수치 계산과 배열 연산**을 쉽게 할 수 있도록 도와주는 라이브러리

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

출력:
[1 2 3 4 5]
```

📌 `np.array()`를 이용해 NumPy 배열을 생성할 수 있다.
