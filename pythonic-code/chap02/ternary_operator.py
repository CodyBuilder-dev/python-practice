def check_boolean(value) :
    return True if type(value) == bool else False

if __name__ == '__main__' :
    print(check_boolean(False))
    print(check_boolean("String"))
    