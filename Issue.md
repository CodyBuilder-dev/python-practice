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
|발생원인|현재 python 환경에 맞는 dependency 찾아보는 과정 수행<br>typing-dependency가 설치되어 있지 않아 진행 멈춤|
|해결|현재 환경에 맞는 jpype whl파일이 준비되어 있다면, --no-deps 옵션으로 설치|
