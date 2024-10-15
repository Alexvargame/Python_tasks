from itertools import permutations
from math import sqrt
from functools import reduce


def is_prime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True

def permutational_primes(n_max, k_perms):
    lst1=[]
    lst2=[]
    n=1789
    print([int(''.join(list(item))) for item in permutations(list(str(n)),len(str(n))) if is_prime(int(''.join(list(item))))
             and len(str(int(''.join(list(item)))))==len(str(n))])
    lst=[[int(''.join(list(item))) for item in permutations(list(str(n)),len(str(n))) if is_prime(int(''.join(list(item))))
             and len(str(int(''.join(list(item)))))==len(str(n))]  
            for n in range(1001,n_max) if is_prime(n) and
           len(set([int(''.join(list(item))) for item in permutations(list(str(n)),len(str(n))) if is_prime(int(''.join(list(item))))
                    and len(str(int(''.join(list(item)))))==len(str(n))]))==k_perms+1]
##    lst=[list(set([int(''.join(list(item))) for item in permutations(list(str(n)),len(str(n))) if is_prime(int(''.join(list(item))))
##             and len(str(int(''.join(list(item)))))==len(str(n))]))  
##            for n in range(11,n_max) if is_prime(n) and
##           len(set([int(''.join(list(item))) for item in permutations(list(str(n)),len(str(n))) if is_prime(int(''.join(list(item))))
##                    and len(str(int(''.join(list(item)))))==len(str(n))]))==k_perms+1]
    print(lst)
    lsst=[[] for i in range(len(lst))]
    for i in range(len(lst)):
        for l in lst[i]:
            if l not in lsst[i]:
                lsst[i].append(l)
       
    print(lsst)

   
    for l in lsst:
        print('l',l[0],l[1:])

        lst2.extend(l[1:])
        print('lst2',lst2)
        if l[0] not in lst2:
            if l[0] not in lst1:
                lst1.append(l[0])
                print('lst1',lst1)
    if len(lst1)>1:
        return [len(lst1),min(lst1),max(lst1)]
    return [0,0,0]
    
            
            
                   
                                                    
def main():

   
    #print(permutational_primes(1000,3))
    #print(permutational_primes(1000,2))
    #print(permutational_primes(1000,1))
    print(permutational_primes(2000,9))


    
    


   


if __name__ == "__main__":
    main()

