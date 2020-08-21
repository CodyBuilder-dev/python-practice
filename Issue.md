# Issue
인터넷 검색으로 안 나오는 경우의 이슈를 내가 스스로 정리
|분류|내용|
|---|---|
|관련원리||
|발생원인||
|해결||

## 폐쇄망에서 pip 설치시 _vendor/urllib 관련 에러
|분류|내용|
|---|---|
|관련원리|pip 설치 과정에서 indexing 수행|
|발생원인|indexing시 pypi 서버에 접근하여 인덱싱 수행<br>해당과정에서 인터넷 연결이 필요|
|해결|--no-index 옵션으로 설치|

## python <3.7 에서 jpype 설치시 typing-extension에서 진행 멈춤
|분류|내용|
|---|---|
|관련원리|pip통한 jpype 설치 과정에서 dependency 검색을 수행 진행|
|발생원인|현재 python 환경에 맞는 dependency 찾아보는 과정 수행<br>typing-extension이 설치되어 있지 않아 진행 멈춤|
|해결|typing-extension 패키지는 추후 jpype 실행에서 필요하므로 whl 준비해서 설치|

## python venv 가상환경에서 sudo pip3.6 install 을 쓰면 root경로에 설치됨
|분류|내용|
|---|---|
|관련원리|sudo 명령어를 쓸 경우, sudo 이후의 모든 명령어&환경변수&옵션은 root 기준으로 해석된다|
|발생원인|현재 venv 내에서 pip link 존재/pip3.6 link 존재 & root 내에 pip link 미존재/pip3.6 link 존재 <br> sudo pip install 시 root 기준으로 생각하므로 command not found <br> sudo pip3.6 install시 root 기준으로 생각하므로 root 라이브러리 링크(/usr/lib/python3.6/site-packages)아래에 설치|
|해결|[sudo -E로 venv환경 물려받기](https://stackoverflow.com/questions/41429988/inside-virtual-env-sudo-pip-links-to-the-global-python-pip)<br>sudo 대신 root로 접속해서 pip install|

## python jaydebeapi 사용방법
|분류|내용|
|---|---|
|관련원리|jaydebeapi와 oracle 연결방법|
|해결|jaydebeapi.connect(드라이버 종류, 드라이버 접속정보, [유저,비밀번호 등 옵션], 드라이버 경로)<br>예시 : jaydebeapi.connect("oracle.jdbc.driver.OracleDriver","jdbc:oracle:thin:@주소:포트번호:SID",["user","pw"],"파일/경로")|
