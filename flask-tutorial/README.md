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






