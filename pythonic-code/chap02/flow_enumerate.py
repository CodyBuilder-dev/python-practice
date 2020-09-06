ALPHABET_LIST = {"A":"a","B":"b","C":"c","D":"d"}

def get_index_basic() :
    # 직접 index 변수를 만들어서 호출해야 함
    i = 0 
    for ch in ALPHABET_LIST :
        print("[%d] %s : %s" % (i,ch,ALPHABET_LIST[ch]) )
        i += 1

def get_index_enumerate() :
    for i, ch in enumerate(ALPHABET_LIST)     :
        print("[%d] %s : %s" % (i,ch,ALPHABET_LIST[ch]) )

    for i, (key ,value) in enumerate(ALPHABET_LIST.items()) :
        print("[%d] %s : %s" % (i,key,value) )
if __name__ == "__main__" :
    print("==basic==")
    get_index_basic()
    print("==enumerate==")
    get_index_enumerate()