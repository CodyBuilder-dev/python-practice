msg = "Hello" # global scope

def read_work() :
    print(msg)
    print("World")

def read_exception() :
    print(msg) # Interpreter는 Local Scope의 msg라고 생각함. Error발생
    msg = "World" 
    print(msg)

print("=== first read ===")
read_work()
print("=== second read ===")
read_exception()