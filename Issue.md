# Issue
인터넷 검색으로 안 나오는 경우의 이슈를 내가 스스로 정리

## 폐쇄망에서 pip 설치시 _vendor/urllib 관련 에러
|관련원리|pip 설치 과정에서 indexing 수행|
|원인|indexing시 pypi 서버에 접근하여 인덱싱 수행<br>해당과정에서 인터넷 연결이 필요|
|해결|--no-index 옵션으로 설치|

## pip 설치시 typing_extension에서 진행 멈춤
|관련원리|pip 설치 과정에서 dependency 검색을 수행하는 듯|
|원인|현재 python 환경에 맞는 dependency 찾아보는데 없는 경우|
|해결|현재 환경에 맞는 whl파일이 준비되어 있다면, --no-deps 옵션으로 설치|
