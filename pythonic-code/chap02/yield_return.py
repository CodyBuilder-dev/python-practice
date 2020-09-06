def gen() :
    yield 1
    yield 2
    yield 3

def normal() :
    return 1
    return 2
    return 3

if __name__ == "__main__" :
    print("gen : ", gen)
    print("gen() :", gen())
    print("next(gen()) : ", next(gen()))
    print("normal() :",normal())

    print("type(gen) : ", type(gen))
    print("type(gen()) : ", type(gen()))

    for g in gen() : # for문 내부적으로 next가 돌아감
        print(g)

    for n in normal() :
        print(n)