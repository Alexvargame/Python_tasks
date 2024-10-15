import math


def represent(n):
    n_sqrt = math.isqrt(n)

##    if n_sqrt * n_sqrt == n:
##        return n_sqrt,

    set1 = set(i * i for i in range(1, n_sqrt+1))
    print('set1',set1)
    for i in set1:
        if n - i in set1:
            return math.isqrt(i), math.isqrt(n - i)

    def gen2():
        for i in set1:
            for j in set1:                
                s = i + j
                if s <= n:
                    yield s

    set2 = set(gen2())
    print('set2',set2)
    for i in set2:
        if n - i in set2:
            return *represent(i), *represent(n - i)
    for i in set1:
        if n - i in set2:
            return math.isqrt(i), *represent(n - i)

    

    assert False


def main():
##    n = int(input())
    n=121
    print('R',represent(n))
    print(n, '=', ' + '.join(f'{i}^2' for i in represent(n)))




if __name__ == "__main__":
    main()




#
