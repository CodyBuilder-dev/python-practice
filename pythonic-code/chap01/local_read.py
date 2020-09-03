def hello() :
    msg = "Hello"
    print(msg)

if __name__ == "__main__" :
    print("=== msg in function ===")
    hello()
    print("=== msg in global ===")
    print(msg) # msg는 Local Scope에서 잠시 사용되다 사라지므로 Error 발생