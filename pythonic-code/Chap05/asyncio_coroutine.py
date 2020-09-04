import asyncio
import random
import datetime


@asyncio.coroutine  # yield from을 쓰기 위해서는 coroutine decorator가 필요하다
def print_time(idx): 
    sleep_time = random.randrange(1,10)
    # yield from는 원래 generator를 반환할 때 쓰지만, asyncio를 반환할 때도 쓴다
    # 하지만, generator의 일반적인 의미와는 다르므로 좀 비직관적
    yield from asyncio.sleep(sleep_time) 
    print("[%s] Sleep time : %s, Complete time : %s" % (idx,
                sleep_time,
                datetime.datetime.now()))
    
def main() :
    futures = [print_time(i) for i in range(10)]

    # Event Loop 객체 선언
    loop = asyncio.get_event_loop()

    # Event 
    # loop.run_until_complete(futures) # 에러 발생
    loop.run_until_complete(asyncio.wait(futures))
    
    # Event Loop 종료
    loop.close()

if __name__ == '__main__' :
    main()