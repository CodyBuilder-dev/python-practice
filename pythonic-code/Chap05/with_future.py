import time
import concurrent.futures

def worker(index) :
    print ("Worker Index : %s" % index)
    time.sleep(index) # Worker가 호출된 후 일정 기간동안 작업 수행
    return ("Completed %s worker job" % index)

def main() :
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor :
        # Executor에 worker 할당
        future_list = []
        for i in range(5) :
            future = executor.submit(worker,i)
            future_list.append(future)

        # wait 메소드를 통해 일정기간동안 대기
        finished, pending = concurrent.futures.wait(future_list, timeout = 2)

        for w in finished :
            print ("Finished Worker : %s" % w.result())
        for w in pending :
            print ("Not finished worker : %s" % w.result())
    
    
if __name__ == '__main__' :
    main()