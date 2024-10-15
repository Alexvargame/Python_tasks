
mem={2:1,3:2,5:3}
primes=[2,3,5]
##def is_prime(a):
##    if a%2==0:
##        return False
##    for i in mem.keys():#range(2,a//2+1):
##        if a%i==0:
##            return False
##    return True

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d # чередование прироста 2 и 4: 5 + 2, 7 + 4, 11 + 2, и т.д.
    
    return prime
        
def count_primes_less_than(n):
##    for nn in range(3,n):
##        if is_prime(nn):
##            mem[nn]=mem[max(mem.keys())]+1
    return len(list(i for i in range(3,n) if is_prime(i)))+1
#mem[max(mem.keys())]



def main():

    print(count_primes_less_than(218680))
    
    
  
    
if __name__ == "__main__":
    main()
##
##def is_prime(a):
##    print(a)
##    if a%2==0:
##        return False
##    for i in mem.keys():#range(2,a//2+1):
##        if a%i==0:
##            return False
##    return True
##
##def count(nn):
##    if nn in mem.keys():
##        return mem[nn]
##    else:
##        if is_prime(nn):
##            mem[nn]=count(nn-1)+1       
##        else:
##            return count(nn-1)
##            #mem[nn]=count(nn-1)
##        print(mem.keys())
##        return mem[nn]   
##        
##def count_primes_less_than(n):
##    if n>1000:
##        for nn in range(1,n//1000+1,-1):
##            
##            count(nn*1000)
##         #   print(mem[nn*1000])
##        count(n)
##        return count(n)
##    else:
##        return count(n)
##
##print(100/log(100))
##    p=sqrt(log(n))/15
##    print(p)
##    print(exp(1)**p)
##    return n/log(n)*(pow(exp(1),sqrt(log(n))/15))
##    #print(n)
##    #input()
##    for i in range(n,-1,-1):
##        #print(i)
##        if is_prime(i):
##            if i in mem.keys():
##                #print('in')
##                #print(mem)
##                return mem[i]+1
##            else:
##                #print('out')
##                mem[i]=count_primes_less_than(i-1)+1
##                
##                
    
    #print('mem',mem, max(mem.keys()))
##mem={0:0,1:0,2:0,3:1,5:2}
##def is_prime(a):
##    for i in range(2,a//2+1):
##        if a%i==0:
##            return False
##    return True
##
##    
##        
##def count_primes_less_than(n):
##    #print(n)
##    #input()
##    for i in range(n,-1,-1):
##        #print(i)
##        if is_prime(i):
##            if i in mem.keys():
##                #print('in')
##                #print(mem)
##                return mem[i]+1
##            else:
##                #print('out')
##                mem[i]=count_primes_less_than(i-1)+1
##                
##                
##    
##    #print('mem',mem, max(mem.keys()))
##    return mem[max(mem.keys())]+1
##    
####    res=(i for i in range(2,n) if is_prime(i))
####    print(list(res))
####    return  len(list(i for i in range(2,n) if is_prime(i)))
