import sys
sys.set_int_max_str_digits(0)
mem={0:0,1:1,-1:1,-2:-1}

def fib1(n):

    
    if n not in mem:
        mem[n]=fib1(n - 1) + fib1(n - 2)
    return mem[n]

def fib(m):
    print('mmm',m)
    if abs(m)>1000:
        
        for n in range(1,abs(m)//900+1):
            fib1(n*900) 
        fib1(abs(m))
        if m>=0:
            print('m',mem[m])
            return fib1(abs(m))
        elif m<0 and m%2!=0:
            print('m1',mem[-m])
            print('m11',fib1(abs(m))*(-1))
            return mem[-m]#fib1(abs(m))*(-1)
        else:
            print('m2',mem[-m])
            return -mem[-m]#fib1(abs(m))
    else:
        if m>=0:
            return fib1(abs(m))
        elif m<0 and m%2==0:
            return fib1(abs(m))*(-1)
        else:
             return fib1(abs(m))
        
def main():

    print(fib(-64951))

    
if __name__ == "__main__":
    main()




#
