msg = "Hello" # global scope

def write() :
    # global msg = "Not Hello" # global 키워드에는 선언과 초기화를 동시에 할 수 없음
    global msg
    msg = "Not Hello"
    print(msg)

print("=== before msg===")
print(msg)
print("=== write msg===")
write()
print("=== after msg===")
print(msg)