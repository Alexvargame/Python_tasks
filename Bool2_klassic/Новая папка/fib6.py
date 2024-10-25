

def fib6(n: int):
    yield 0 # специальный случай
    if n > 0:
        yield 1 # специальный случай
    last= 0 #начальное значение fib(0)
    next= 1 #начальное значение fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # главный этап 


if __name__=="__main__":
    for i in fib6(50):
        print(i)
