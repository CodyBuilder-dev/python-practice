def greeting(name) :
    greeting_msg = "Hello "

    def add_name() :
        global greeting_msg # greeting_msg는 분명히 외부 변수이긴 하지만, global scope는 아니기에 error 발생
        greeting_msg += "Not "
        return "%s%s" % (greeting_msg,name)

    msg = add_name()
    print(msg)

if __name__ == '__main__' :
    greeting("codybuilder")