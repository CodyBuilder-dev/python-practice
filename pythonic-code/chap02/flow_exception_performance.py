import os
import time

EXIST_FILE = "sample_file"
NON_EXIST_FILE = "non_exist_sample_file"

def write_file_try(file_name) :
    try :
        f = open(file_name,"w")

        for i in range(10000000) :
            f.write(str(i))
        
        f.close()
    except :
        print("File open error")
    finally :
        os.remove(file_name)
        print("End file read\n\n")

def write_file_else(file_name) :
    try :
        f = open(file_name,"w")
    except :
        print("File open error")
    else :
        for i in range(10000000) :
            f.write(str(i))
        
        f.close()
    finally :
        os.remove(file_name)
        print("End file read\n\n")

def check_runtime(func,file_name) :
    accumulate_time = 0
    for i in range(10) :
        start = time.time()
        func(file_name)
        accumulate_time += (time.time()-start)
    
    print("Run time summary : %s" % str(accumulate_time/10))
if __name__ == "__main__" :
    print("== Try Performance ==")
    check_runtime(write_file_try,EXIST_FILE)

    print("== Else Performance ==")
    check_runtime(write_file_else,EXIST_FILE)
