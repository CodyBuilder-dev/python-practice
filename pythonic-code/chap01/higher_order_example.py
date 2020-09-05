LOWER_LIST = ["python","python2","python3"]
UPPER_LIST = []

# 일반적인 for문을 사용한 패턴
# 문제 1: input이 list가 아니면 문제를 일으킬 수 있음
# 문제 2: 전역변수를 사용하므로 함수의 행동 파악하기 힘듬
def convert() :
    for data in LOWER_LIST :
        UPPER_LIST.append(data.upper())

# 고차함수 이용 패턴
def convert_upper(data:str) :
    return data.upper()

def main() :
    UPPER_LIST = map(convert_upper,LOWER_LIST) 
    print(type(UPPER_LIST)) # map 객체 반환
    print(list(UPPER_LIST))

if __name__ == '__main__' :
    main()