# Chap01
## 파이썬스러움의 예시

## python namespace 
### Namespace와 Scope
Python에는 사전에 정의된 몇가지의 Namespace가 존재  
변수가 초기화되는 순간에 어디에 있느냐에 따라 해당 변수가 속하는 Namespace가 결정  
파이썬에서 Scope는 Namespace와 동일한 의미로 사용됨  
(예시 : 변수 x가 global namespace에 속해 있다 = global scope에서 변수 x를 찾을 수 있다)

### 파이썬 Namespace 규칙 : LEGB
Local -> Enclosed -> Global -> Built-in의 순서로 변수 네임스페이스 탐색  

|Namespace명|설명|
|--|--|
|built in|모든 파이썬 코드 범위에서 유효|
|global|해당 파일 내에서 유효|
|enclosed|Nested 함수에서 유효|
|local|클래스, 함수 내에서 유효|

### global 키워드
(코드 참조)

### nested function
(코드 참조)

### variable shadowing

## First-Class(일급)
### First-Class Citizen의 의미
1. 변수에 값으로 할당할 수 있거나
2. 함수에 매개변수로 전달할 수 있거나
3. 함수의 반환값으로 사용할 수 있는 객체

### PYthon First-Class Citizen 의 종류
1. 변수
2. 데이터구조(list,dict 등)
3. 클래스
4. **함수(First-Class Function)**

## Higher-Order Function(고차 함수)
### 고차함수의 의미
타 함수를 매개변수로 받거나, 타 함수를 반환하는 함수
### Python 고차함수의 예시
map

## Nested Function과 Scope Chain
### Nested 개념
함수의 내부에 다른 함수가 정의된 경우를 Nested 되었다고 표현하고,  
내부의 함수를 inner function, 외부의 함수를 outer function이라고 지칭한다.

### Closure
1. Nested Func을 지원하고
2. 함수가 일급 객체로 취급될 수 있는 언어에서
자신의 내부에 있는 inner func과 그 inner func이 사용되는 환경을 반환하는 함수  
=> 이를 통해, 외부에서 inner func에 접근할 수 있게 된다.

### 의문 : CLosure를 써야하는 이유?
JavaScript는 클래스가 익숙하지 않으니 클로저를 쓰는걸 이해할 수 있다  
Python은 클래스가 이미 존재하는데 클로저를 굳이 써야하는 이유가 있을까?
1. global 변수를 사용하고 싶지 않을 때 : outer func의 local variable을 마치 inner의 global variable처럼 사용할 수 있으므로!
2. class를 사용하고 싶지 않을 때 : 자주 반복되지는 않아서 class로 만들기보다는, 잠깐 closure로 만들어서 쓰는 것이 나을 수 있다.
3. decorator를 사용하기 위해서