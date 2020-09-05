def calculator(x) : # calculator는 고차함수
    def sub(y) :
        return x - y
    
    return sub # sub 함수 반환

if __name__ == '__main__' :
    # print(sub(10)) # Error! 내장함수는 외부에서 접근할 수 없다.
    print(calculator(10)(20)) # 내장함수를 접근하려면 외장함수를 거쳐서 호출해야 한다
    f = calculator(10) # f는 외장함수를 한번 거쳐서 내장함수를 전달받는다
    print(f(20)) # outer()()의 효과를 지님