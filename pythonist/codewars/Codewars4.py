from math import sqrt
mem={0:0,1:1}
def fibonacci(n):
    if n not in mem:
        mem[n]=fibonacci(n - 1) + fibonacci(n - 2)
    return mem[n]



def productFib(prod):
    if prod<1000000:
        n=int(sqrt(prod))
    else:
        print(len(str(prod)))
        n=int(prod**(1./len(str(prod))/2.))
    print(n)
    fibonacci(n)
    print(mem)
    for key in mem.keys():
        if mem[key]*mem[key+1]==prod:
            return [mem[key],mem[key+1],True]
        elif mem[key]*mem[key+1]>prod:
            return [mem[key],mem[key+1],False]
    

        


def main():

    
    print(productFib(4895))
    print(productFib(74049690))
   
    
if __name__ == "__main__":
    main()



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
