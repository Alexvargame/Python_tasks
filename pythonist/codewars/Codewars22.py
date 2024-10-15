from math import sqrt




def dbl_linear(a):
    u=[]

    for i in range (20):
        u.append(2*i+1)

    return u
  
        


def main():

    
    print(dbl_linear(10))
   
    
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
