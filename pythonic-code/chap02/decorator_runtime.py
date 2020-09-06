import time

def measure_runtime(func) :
    def wrapper(args) : # *arg와 arg의 차이는?
        start = time.time()
        func(args)
        end = time.time()
        
        print("%s function run time : %s" % (func.__name__,end-start))

    return wrapper

@measure_runtime # 데코레이터 적용
def worker(delay) :
    time.sleep(delay)

if __name__ == "__main__" :
    worker(5)