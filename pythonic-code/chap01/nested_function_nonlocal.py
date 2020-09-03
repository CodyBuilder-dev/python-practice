def greeting(name) :
    greeting_msg = "Hello "

    def add_name() :
        nonlocal greeting_msg # Local scope를 벗어나 Enclosed scope 부터 탐색 시작
        greeting_msg += "Not "
        return "%s%s" % (greeting_msg,name)

    msg = add_name()
    print(msg)

if __name__ == '__main__' :
    greeting("codybuilder")