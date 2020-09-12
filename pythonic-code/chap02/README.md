# Chap 02
## 흐름제어문
### 삼항 연산자
파이썬에도 삼항연산자가 있다. 다만 타 언어의 삼항연산자와 상당히 형식이 다르다  

문법 : `a if 조건문 else b`

- 장점 : 말 그대로 '영어문장으로 읽을 수 있을 정도'의 가독성
- 단점 : 타 언어와 전혀 호환되지 않는 문법에 혼란

### 예외처리
파이썬에는 try에도 else를 쓸 수 있다. try가 정상적으로 수행되면 else가 수행된다.  
else문에서는 try문의 변수가 그대로 사용된다.

문법 : `try : else : except : finally : `  
- 장점 : try에서 수행되는 내부 검사를 거치지 않아도 되어 수행속도가 빠르다

### 반복문
1. 파이썬의 range 구문은, generator이다
2. 파이썬의 enumerate 구문은, 인덱스를 쓸 수 없는 자료형(dict)에 인덱스를 만들어 준다.

## Decorator 
### Decorator의 목적
기존의 클래스나 함수를 수정하지 않고 기능을 덧붙이는 클로저
-> 나중에 Spring에서 이어지는 IoC를 위한 핵심적인 요소
### Decorator의 사용법
1. 함수를 인자로 받는 closure를 만든다
2. closure 내부에 wrapper 함수를 만들고, 인자로 받은 함수를 wrapper 내부에서 잘 요리한 후 wrapper를 반환한다.
3. Decorator를 적용시키고 싶은 함수의 윗줄에 `@클로저명` 을 추가한다.
### 다중 Decorator
실행 순서 : 함수의 바로 위에 있는 것 부터, 아래에서 위로 실행된다.

## iterable, iterator
### iterable
정의 : 한번에 하나 혹은 그 이상씩 값을 반환할 수 있는 객체  
예시 : 
1. container(리스트,튜플,dict등의 자료형)
2. open 함수로 불러진 파일, 소켓
3. __iter__ 혹은 __getitem__ 메서드가 구현된 Class

### iterator
정의 : 한번에 하나씩만 값을 반환하는 객체  
특성 : 
1. 현재 어디까지 반복되었는지 정보를 포함함
2. next를 통해 하나씩 반환
3. 더이상 반환할 값이 없을 경우 StopIteration Exception 발생  
사용법 : StopIteration 에 대한 예외처리가 필요함

### 파이썬의 iterator 구현 : iter 키워드
용도 : 해당되는 객체를 iterator로 만들어줌
동작방식 : 해당 객체의 __iter__ 메소드를 호출하는 듯?

### 파이썬의 iterator 구현 : next 키워드
용도 : 해당 iterator의 다음 값을 반환해줌
동작방식 : 해당 iterator의 __next__메소드를 호출하는 듯?

### 파이썬의 iterator 구현 : for문
for문에서 대상이 되는 객체는, iterable이라도 자동으로 iterator로 변환된다

## Generator
### 파이썬의 Generator 정의(python 3)
제네레이터 이터레이터를 반환하는 함수다

### Generator의 특성
1. 함수이다
2. yield 구문을 포함한다.

### Generator iterator vs Iterator
차이점 1 : next 메서드의 동작  
|Generator Iterator|Iterator|
|--|--|
|1. 처음일 경우, 처음 만나는 yield문까지 실행한다.<br>2.그 다음 yield문까지 실행한다.|컨테이너의 다음 값을 반환한다.|

차이점 2 : 메모리
|Generator Iterator|Iterator|
|--|--|
|next가 수행되는 시점에 값이 계산되고 반환됨|미리 계산된 값들을 next 시점에 반환만 함|

### 파이썬의 Generator 구현 : yield 키워드