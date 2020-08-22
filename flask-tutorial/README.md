# flask 
## 플라스크의 기본 환경
python 2.7(놀랍게도 2.7이 공식 지원 버전이다) + Werkzeug + Jinja2

## 플라스크 request 객체
사용법 : from flask import request로 import 해 와야 한다  
구성요소 :   
Form = 폼데이터. dict 타입  
args = 쿼리스트링. string타입  
Cookies = 쿠키. dict 타입 
files = 파일  
method = HTTP 메소드 종류

## 플라스크 정적 파일 폴더 static
### 정적파일 폴더를 따로 만들고 관리해야 하는 이유
html에서 불러와서 쓰고 싶은 파일이 있다 -> html 안에 파일의 경로를 적자 -> 에러 발생! 불러오기 실패!  
이유 : 웹 브라우저는 기본적으로 OS 파일시스템에 접근할 수 없다!  
해결법 : 
1. 해당 파일도 웹서버 URL에 라우팅시키고, 해당 URL을 참조하는 식으로 간접적으로 불러와야 한다.  
2. 라우팅 처리를 Flask WAS쪽에서 직접 할 수도 있지만, nginx와 같은 WEB서버쪽에서 수행해주면 더 빠른 처리가 가능하다


## 플라스크 session
구현방식 : 플라스크에서 Session은 사실은 Signed Cookie 방식으로 구현됨  
사용방법 : 구체적인 구현은 library 내에 감춰져 있음.  
우리는 그냥 서버의 private key(=secret key)만 발급해서 쓰면 됨

## 플라스크 message flashing
개념 : 자바스크립트의 alert과 같이 사용자에게 경고를 주는 창을 띄우는 것  
동작방식 : 



## 플라스크 extenstion 종류
(Pypi 사이트에서 'flask' 검색)  
대표적으로 자주 사용되는 것들을 정리해 보자
### flask-mail
플라스크 메일 
### flask-wtf

### flask-SQLite

### flask-SQLAlchemy
용도 :   
    (ORM을 쓰는 범용적인 이유와 동일)  
의존성 :  
    sqlalchemy
설치법 :  
    pip install flask-sqlalchemy

### flask-Sijax
플라스크용 jQueyr/Ajax 모듈
의존성 :  
    sijax  
    future
설치법 :  
    pip install flask-sijax
용도(jinja에서 jQuery를 쓸 수 있고, 보통 router로도 request처리가 가능하다. 왜 flask BE단에서 jQuery 라이브러리가 필요한가?) :  
    (적절한 대답 찾는 중)  
    일반적인 flask request와 jQuery request를 따로 분리하여 대응할 수 있다.  
    jQuery로 짜여진 레거시 코드에 대응할 때 쓸 수 있을 것 같다.

### flask - mod_wsgi / FastCGI
mod_wsgi : Apache-WSGI 서버
FastCGI : WSGI서버(굳이 쓸 필요 없음)






