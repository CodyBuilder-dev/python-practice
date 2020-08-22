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

## 플라스크 extenstion 종류
(Pypi 사이트에서 'flask' 검색)  
대표적으로 자주 사용되는 것들을 정리해 보자
### flask-mail
플라스크 메일 
### flask-wtf

### flask-SQLite

### flask-SQLAlchemy

### flask-Sijax
플라스크용 jQueyr/Ajax 모듈

### flask - mod_wsgi / FastCGI
mod_wsgi : Apache-WSGI 서버
FastCGI : WSGI서버(굳이 쓸 필요 없음)






