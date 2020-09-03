def square(x) :
    return x**2

def main() :
    print("Function call : square(10)")
    a = square(10)
    print(a)

    print("Function Assign : f = square, f(10)")
    f =square
    b = f(10)
    print(b)

    print(a==b)

if __name__ == '__main__' :
    main()
