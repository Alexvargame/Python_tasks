li=[1,6,[4,3],3,5]
def sum_(l):
    summ=0
    for i in l:
        if type(i)==list:

            summ=summ+sum_(i)
        else:
            summ=i+summ
           
    return summ
print(sum_(li))

def sumDigits(n):
    l=[int(i) for i in str(n)]
    return sum(l)
print(sumDigits(34364572245))

def sum_series(n):
    if n<1:
        return 0
    else:
        
        return  n+sum_series(n-2)   
        
print(sum_series(6))
            
def sum_series_(n):
    if n<1:

        return 0
    else:
        return  1/(n**2)+sum_series_(n-1)   
        
print(sum_series_(5))

def power(a,b):
    if b<1:
        return 1
    else:
        return  a*power(a,b-1) 
        
print(power(2,4))


def fib(n):
    for i in range(n):
 
        if n in (1,2):
           return 1
        else:
           return fib(n-2)+fib(n-1)
               
print(fib(3))
