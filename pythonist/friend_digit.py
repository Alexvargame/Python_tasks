#https://pythonist.ru/zadacha-21-druzhestvennye-chisla/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute(n):
        l=[]
        for i in range(1,n):
                for j in range(i,n):
                        #print([k for k in range(1,i) if i%k==0],j,[k for k in range(1,j) if j%k==0],i)
                       
                        if sum([k for k in range(1,i) if i%k==0])==j and sum([k for k in range(1,j) if j%k==0])==i:
                                p=(i,j)
                                l.append(p)
        
        return l
def divis():
        l1=[]
        for k in range(1,i):
                if i%k==0:
                        l1.append(k)
        return sum(li)
                        

def compute1():
    # Compute sum of proper divisors for each number
    divisorsum = [0] * 10
    
    for i in range(1, len(divisorsum)):
        for j in range(i * 2, len(divisorsum), i):

            divisorsum[j] += i
            print(i,j,divisorsum[j])
            print(divisorsum)
            input()
    print(divisorsum)
    # Find all amicable pairs within range
    ans = 0
    for i in range(1, len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] == i:
            ans += i
    return str(ans)        

def main():
        
        print(compute(100))
        
  



if __name__ == "__main__":
    main()


