if __name__ == "__main__" :
    x = [1,2,3]
    print(type(x)) #  list

    y = {"red":1,"blue":2,"green":3}
    print(type(y)) # dict

    x_iterator = iter(x)
    print(type(x_iterator)) # list_iterator

    y_iterator = iter(y)
    print(type(y_iterator)) # dict_keyiterator

    # print(next(x)) # TypeError : object is not an iterator
    # print(next(y)) # TypeError : object is not an iterator
    print(next(x_iterator))
    print(next(y_iterator))
    