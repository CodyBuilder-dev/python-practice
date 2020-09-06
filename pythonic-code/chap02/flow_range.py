import sys

def get_type_and_size(data) :
    print("type : %s" % type(data))
    print("size : %s" % sys.getsizeof(data))

def main() :
    print("=== Range 10===")
    get_type_and_size(range(10))

    print("=== Range 100===")
    get_type_and_size(range(100))

    print("=== Range 1000===")
    get_type_and_size(range(1000))

    print(dir(range(10)))

if __name__ == "__main__" :
    main()