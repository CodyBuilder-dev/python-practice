EXIST_FILE = "sample_file"
NON_EXIST_FILE = "non_exist_sample_file"

def read_file(file_name) :
    try :
        f = open(file_name,"r")
    except :
        print("File open error")
    else :  # 반드시 try: except: 뒤에 else:가 와야 함
        print(f.read())
        f.close()
    finally :
        print("End file read\n\n")

if __name__ == "__main__" :
    print("== Exist File open ==")
    read_file(EXIST_FILE)

    print("== Non Exist File open ==")
    read_file(NON_EXIST_FILE)
