def deco(func) :
    def wrapper() :
        print("==Before==")
        func()
        print("==After==")

    return wrapper

@deco # 데코레이터 적용
def base() :
    print("Base")

if __name__ == "__main__" :
    base()