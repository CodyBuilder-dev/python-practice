import time
import concurrent.futures

def worker(index) :
    print ("Worker Index : %s" % index)
    time.sleep(index) # Worker가 호출된 후 일정 기간동안 작업 수행
    return ("Completed %s worker job" % index)

def main() :
    future_list = []
    # ProcessPoolExecutor 객체 선언
    # max workers 개수만큼만 동시에 실행됨
    executor =concurrent.futures.ProcessPoolExecutor(max_workers=3)

    for i in range(5) :
        # Worker 함수와 함수의 인자를 Executor에 전달
        # 전달 즉시 future를 반환해줌
        future = executor.submit(worker,i)
        future_list.append(future)

    time.sleep(1)

    # 1초 후 future의 상태 확인
    for idx, future in enumerate(future_list) :
        # future가 수행 완료되었을 경우 해당 결과 출력
        if future.done() : 
            print("Result : %s" % future.result())
            continue
        print("[%s worker] wait for 1 second because it has not finished yet" % idx)
        
        # future가 수행 완료되지 않았을 경우, 1초간 더 대기
        try :
            result = future.result(timeout=1)
        except concurrent.futures.TimeoutError :
            print("[%s worker] Timeout error" % idx)
        else :
            print("result : %s" % result)

        # 모든 future 될 경우 executor shutdown
        # 주의, 아직 수행중인 future들도 강제로 종료됨
        executor.shutdown(wait = False )
    
if __name__ == '__main__' :
    main()