from itertools import combinations_with_replacement
from math import sqrt


def exp_sum(n):
    mem={3:2,4:5}
    count=0
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        return exp_sum(n-1)

#
#     print(list([item for item in combinations_with_replacement(range(1,n),rep) if
#              sum(item)==n] for rep in range(2,n)))
#     print(list(len(list(item for item in combinations_with_replacement(range(1,n),rep) if
#              sum(item)==n)) for rep in range(2,n)))
#
#
# ##    while nn>2:
# ##        for item in combinations_with_replacement(range(1,n),rep):
# ##            if sum(item)==n:
# ##                count+=1
# ##                yield
# ##        print('d')
# ##        nn-=1
#
#     return sum(len(list(item for item in combinations_with_replacement(range(1,n),rep) if
#             sum(item)==n)) for rep in range(2,n))+2
   


def main():
    print(exp_sum(4))
    # print(exp_sum(5))
    # print(exp_sum(6))
    # print(exp_sum(7))
    # print(exp_sum(8))
    # print(exp_sum(9))
       
if __name__ == "__main__":
    main()
##
##if n==1:
##        return 1

####    print(list([item for item in combinations_with_replacement(range(1,n),rep) if
####             sum(item)==n] for rep in range(2,n)))
##    print(list(len(list(item for item in combinations_with_replacement(range(1,n),rep) if
##             sum(item)==n)) for rep in range(2,n)))
##    return sum(len(list(item for item in combinations_with_replacement(range(1,n),rep) if
##             sum(item)==n)) for rep in range(2,n))+2
##
##def memoized(f):
##    cache = {}
##    def wrapped(k):
##        v = cache.get(k)
##        if v is None:
##            v = cache[k] = f(k)
##        return v
##    return wrapped
##
##@memoized
##def fibonacci(n):
##    if n in [0, 1]:
##        return n
##    return fibonacci(n - 1) + fibonacci(n - 2)

##mem={0:0,1:1}
##def fibonacci(n):
##
##    if n not in mem:
##        mem[n]=fibonacci(n - 1) + fibonacci(n - 2)
##    return mem[n]
##
##def alphanumeric(password):
##    if password.isspace() or ' ' in password or len(password)<1:
##        return False
##    else:
##        for l in password:
##            if not l.isnumeric() and not l.isalpha():
##                return False
##        return True

##    if n not in mem:
##        print(mem)     
##        men[n]=[pow(-1,k+1)*exp_sum(n-k*(3*k-1)/2) for k in range(1,n)]
##        ptint(mem[n])
##    return mem[n]
##    if n not in mem:
##
##        mem[n]=[pow(-1,k+1)*exp_sum(n-k*(3*k-1)/2) for k in range(n)]
##    return mem[n]

