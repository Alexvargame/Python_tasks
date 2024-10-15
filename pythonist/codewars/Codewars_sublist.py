def sublist(lst,b,e):
    count=0
    for i in range(len(lst)):
        if lst[i]==b:
            count+=lst[i:].count(e)
    return count
        


def main():

    
    print(sublist([1,4,3,5,6,6,5],1,5))
    print(sublist([1,1,1,1],1,1))
   
    
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
