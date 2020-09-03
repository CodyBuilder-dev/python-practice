def square(x) :
    return x**2

def bind(func,data) :
    result_data = []
    for i in data :
        result_data.append(func(i))
    return result_data

def main() :
    data = [10,100]
    print("data = ",data)
    print("Function as Parameter : bind(square,data)")
    print("result = ",bind(square,data))

if __name__ == '__main__' :
    main()
