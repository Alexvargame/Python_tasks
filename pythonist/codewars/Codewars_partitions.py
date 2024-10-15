from itertools import permutations,combinations,product,combinations_with_replacement
from math import sqrt
from functools import reduce


def is_prime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True


def partitions(n):
    mem={1:1,2:2,3:3,4:5,5:7}
    if n<6:
        return mem[n]
    #print([[b for b in range(1,n+1)][:n+1-rep] for rep in range(1,n-1)])
    
    print ([sorted(list(item),reverse=True) for sublist in [[item for item in combinations_with_replacement([b for b in range(1,n+1)][:n+1-rep],rep)
                                   if sum(item)==n] for rep in range(1,n+1)] for item in sublist])
    

    return len([sorted(list(item),reverse=True) for sublist in [[item for item in combinations_with_replacement([b for b in range(1,n+1) ][:n+1-rep],rep)
                                   if sum(item)==n] for rep in range(1,n-3)] for item in sublist])+7
    
            
            
                   
                                                    
def main():

   
    print(partitions(3))
    print(partitions(4))
    print(partitions(5))
    print(partitions(6))
    print(partitions(7))
    print(partitions(8))
    print(partitions(9))
    print(partitions(10))
    print(partitions(11))
    print(partitions(12))


    
    


   


if __name__ == "__main__":
    main()

