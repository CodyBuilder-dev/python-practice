def calculator(x) : # calculator는 고차함수
    def add(y) :
        return x + y
    def sub(y) :
        return x - y
    
    return add,sub # add,sub를 동시 반환


if __name__ == '__main__' :
    
    f = calculator(10)[0]
    g = calculator(10)[1]
    h = calculator(10) # add, sub를 tuple에 담아서 반환하는 듯
    print(f(20)) # 
    print(h[0](10))