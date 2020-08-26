# python-practice
언젠가는 짚고 가야 할 파이썬 &amp; 장고 백엔드 동작원리  
**나는 지금 파이썬을 '파이썬스럽게' 잘 쓰고 있는가? 에 대한 답변**

## 목표 공부기간
2020년 ~ 2021년

## 레퍼런스 정리
### 교재 추천 리스트
#### 파이토닉 코드
|제목|설명|
|---|---|
|[파이썬 클린 코드](http://www.yes24.com/Product/Goods/69064790)|교재, e북 없음|
|[파이썬 클린 코드](https://dailyheumsi.tistory.com/221)|파이썬 클린코드 예시|
|[파이썬답게 코딩하기](https://ridibooks.com/books/3780000029?_s=search&_q=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%8B%B5%EA%B2%8C+%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0)|파이토닉 코드 교재|

#### 플라스크
|제목|설명|
|---|---|
|[깔끔한 파이썬,탄탄한 백엔드](https://ridibooks.com/books/3780000004?_s=search&_q=%EA%B9%94%EB%81%94%ED%95%9C+%ED%8C%8C%EC%9D%B4%EC%8D%AC)|플라스크 이용한 몇 안되는 책|
|[플라스크 튜토리얼](https://www.tutorialspoint.com/flask/index.htm)|플라스크 기본 문법 튜토리얼, 분량이 적어 따라하기 쉽다|
|[플라스크 기본 문법](https://www.slideshare.net/dahlmoon/20170331)|SildeShare 설명 내용|
|[플라스크 공식 문서](https://flask-docs-kr.readthedocs.io/ko/latest/)|한글화된 공식 문서. 플라스크의 내부 구조 API 포함|

#### 장고
|제목|설명|
|---|---|
|파이썬 웹 프로그래밍 (입문편/실전편) | 평가 제일 무난 |
|Django(장고)로 쉽게 배우는 배프의 오지랖 파이썬 웹 프로그래밍 | 완전 기초보다는 예제 프로젝트 위주  |
|Django 한 그릇 뚝딱 | 3가지 실전 프로젝트 위주  |
|[Django 자습](https://wikidocs.net/book/837) | 위키독스 자습 파일. 코드가 나와 있어 따라치기 좋음|

+[프로그래머를 위한 베이지안 with python](https://ridibooks.com/books/754022885?_s=search&_q=%ED%8C%8C%EC%9D%B4%EC%8D%AC)(재밌어보여서 ㅎ)

### 링크 정리
#### 파이썬
|내용|링크|
|---|---|
|Python 3.x 버전별 차이|[3.6/3.7](https://docs.python.org/ko/3/whatsnew/3.7.html)<br>[3.7/3.8](https://python.flowdas.com/whatsnew/3.8.html)|
|Python GC(가비지 컬렉터) 동작원리|[링크](https://winterj.me/python-gc/)|
|Python 기술면접 질문들|[리드미](https://post.naver.com/viewer/postView.nhn?volumeNo=21620976&memberNo=28685456)|
|JIT 컴파일의 이해|[위키백과](https://ko.wikipedia.org/wiki/JIT_%EC%BB%B4%ED%8C%8C%EC%9D%BC)<br>[꺼무위키](https://namu.wiki/w/JIT)|
|Python 런타임 이해|[컴파일러/인터프리터 구조](https://aliwo.github.io/swblog/python/python-runtime/#)|
|PyPy의 구현 원리|[나무위키](https://namu.wiki/w/PyPy)<br>[Youtube](https://www.youtube.com/watch?v=Wgw5ers5jA4)|
|Python generator||
|Python과 객체지향||
|Python GIL||
|Python과 메모리||
|Python에서 운영체제 확인하기|[링크](https://pinkwink.kr/1002)|
|Python pyinstaller로 Executable 만들기|[Windows](https://hongku.tistory.com/338)<br>[GUI설정 포함](https://blog.naver.com/PostView.nhn?blogId=qbxlvnf11&logNo=221791248065)|
|파이썬 실행 옵션 정리|[Doc](https://docs.python.org/ko/3.6/using/cmdline.html)|

#### pip
|내용|링크|
|---|---|
|pip 폐쇄망에서 사용하기|[링크](https://yujuwon.tistory.com/entry/%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%97%90%EC%84%9C-pip-%ED%8C%A8%ED%82%A4%EC%A7%80-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)|
|pip 원하는 플랫폼/원하는 파이썬 버전으로 깔기|[플랫폼](https://stackoverflow.com/questions/59083607/how-to-download-pip-module-for-linux-using-windows)|
|pip 폐쇄망 설치시 이슈|[링크](Issue.md)|
|pip 설치과정에서 외부 의존성에 대한 pip팀의 입장|[공식Doc](https://pip.pypa.io/en/stable/development/vendoring-policy/)|

#### WEBWAS(flask/django)
|내용|링크|
|---|---|
|동적 웹서비스를 위한 CGI,WAS,WSGI 이해|[링크](https://brownbears.tistory.com/350)<br>[링크](https://www.slideshare.net/SELOLEE/ss-126936404)|
|포워드 프록시 vs 리버스 프록시|[링크](https://www.lesstif.com/system-admin/forward-proxy-reverse-proxy-21430345.html) <br> [링크](https://firework-ham.tistory.com/23)|
|flask의 WSGI 구현 이해|[링크](https://spoqa.github.io/2012/01/16/wsgi-and-flask.html)|
|werkzeug(flask WSGI 유틸리티) http 처리방식 심도 이해|[링크](https://spoqa.github.io/2012/05/07/about-flask-request.html)|
|gunicorn 이해|[링크](https://vsupalov.com/what-is-gunicorn/)<br> [링크](https://jaas.ai/gunicorn/trusty/1)|
|flask SSL 적용|[링크](http://mcchae.egloos.com/11143246)|
|flask (+ werkzeug) + Nginx |[Windows](https://chanhy63.tistory.com/19?category=731625)|
|flask + gunicorn + Nginx |[링크](https://velog.io/@yvvyoon/flask-nginx-gunicorn-1)<br>[링크](https://yumere.tistory.com/59)<br>[링크](https://blog.iolate.kr/259)<br>[링크](https://blog.naver.com/PostView.nhn?blogId=na_qa&logNo=221912986971)|
|flask + uWSGI + Nginx |[링크](https://medium.com/sunhyoups-story/flask-nginx-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-258b979d2de3) <br> [링크](https://taetaetae.github.io/2018/07/01/simple-web-server-flask-nginx/)<br>[링크](https://cjh5414.github.io/flask-uwsgi-nginx/)<br>[링크](https://sodocumentation.net/ko/flask/topic/4637/nginx%EC%99%80-%ED%95%A8%EA%BB%98-uwsgi-%EC%9B%B9-%EC%84%9C%EB%B2%84%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-flask-%EC%9D%91%EC%9A%A9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%B0%B0%ED%8F%AC)|
|flask + fabric + Apache |[링크](https://beomi.github.io/2017/10/17/Deploy-Flask-with-Fabric/)|
|flask + gunicorn (+supervisor) |[링크](http://egloos.zum.com/mcchae/v/11149241) |
|django ORM||
|django + gunicorn + Nginx | [링크](https://wikidocs.net/6601)|
|django + gunicorn + Nginx (+supervisor)|[링크](https://yujuwon.tistory.com/entry/%EC%9A%B0%EB%B6%84%ED%88%AC%EC%97%90%EC%84%9C-Django%EC%99%80-gunicorn-supervisor-nginx-%EC%97%B0%EB%8F%99-%ED%95%98%EA%B8%B0)|
|python에서 JDBC thin driver 통해 DB 접근|[Jpype & JayDeBeApi](https://bongury.tistory.com/89)<br>|
|Jython 스타일로 JDBC 드라이버 DB접근|[링크](https://jythonbook-ko.readthedocs.io/en/latest/DatabasesAndJython.html)|
|Flask의 Secret Key에 대해서 내용 싹다 정리|[플라스크 Secret Key 사용 이유](https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key)<br>[플라스크 임의 Secret Key 만들기](https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask)<br>[Secret Key를 하드코딩하는 이유](https://stackoverflow.com/questions/27287391/why-not-generate-the-secret-key-every-time-flask-starts)<br>[Secret Key 보관법](https://stackoverflow.com/questions/30873189/where-should-i-place-the-secret-key-in-flask)|
|flask에 https 적용하기|[링크](https://www.hanbit.co.kr/media/channel/view.html?cms_code=CMS6163871474)|
|flask Login|[링크](https://niceman.tistory.com/191)<br>[링크](https://flask-login.readthedocs.io/en/latest/#flask_login.login_required)<br>[링크](https://github.com/mcchae/Flask-Login)|
|gunicorn 백그라운드에서 돌리기|[링크](https://www.it-swarm.dev/ko/python/gunicorn%EC%9D%84-%EA%B3%84%EC%86%8D-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EC%98%AC%EB%B0%94%EB%A5%B8-%EB%B0%A9%EB%B2%95%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C/1070401484/)|
|gunicorn 명령어 설정하기||
