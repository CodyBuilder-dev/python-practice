# 주의! Closure 사용시, 시간에 관련된 변수를 쓰면 의도치 않은 결과가 나올 수 있다.

import datetime
import time

def logger() :
    now = datetime.datetime.now() # 시간 변수

    def print_log(msg) :
        return ("[%s] %s" % (now,msg))

    return print_log

def main() :

    print_log = logger() # 외부 함수의 호출과 동시에 시간변수가 세팅된다
    print(print_log("Start"))

    time.sleep(5)
    
    print(print_log("After 5 sec")) # 한번 저장된 시간변수는 변하지 않는다

if __name__ == '__main__' :
    main()