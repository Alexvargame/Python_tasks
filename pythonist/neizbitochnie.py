#https://pythonist.ru/zadacha-23-neizbytochnye-summy/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute(m):
        alst=listizb(m)
        print(alst)
        return sum(list(set([i for i in range(1,m)  for j in alst if i-j  not in alst])))
        

def izbyt(n):
        return n<sum([i for i in range(1,n) if n%i==0])
                        
def listizb(m):
        return [i for i in range(m) if izbyt(i)]
def compute1():
    LIMIT = 28124
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]
    
    expressible = [False] * LIMIT
    for i in abundantnums:
        for j in abundantnums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break
    
    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return str(ans)

def main():
        
        print(compute(28124))
        #print(compute1())
        
  




if __name__ == "__main__":
    main()


