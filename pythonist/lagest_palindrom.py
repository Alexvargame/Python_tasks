#https://pythonist.ru/proekt-ejlera-zadacha-4-naibolshee-proizvedenie-palindrom/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


##def compute1(n,m):
##        
##        return sum([i for i in range(1,n+1)]))**2-sum([i**2 for i in range(1,n+1)])



def compute(n,m):
        
        l=[]
        for i in range(n,m):
                for j in range(i, m):
                        #print("*",i,j)
                        p=(i*j, i, j)
                        #print(str(p),str(p)[::-1])
                        if str(p[0])==str(p[0])[::-1]:
                                l.append(p)
        return max(l)
        #return max([[i*j for j in range(i,m) if str(i*j)==str(i*j)[::-1]] for i in range(n,m)])
              

def main():
        print(compute(1,10))
        print(compute(10,100))
  



if __name__ == "__main__":
    main()


