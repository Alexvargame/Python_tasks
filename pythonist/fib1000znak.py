#https://pythonist.ru/zadacha-25-slovarnye-perestanovki/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute(m):
        i=3
        while len(str(fib(i)))<m:
                i=i+1
        return i

def fib(n):
        if n<3:
                return 1
        else:
                return fib(n-1)+fib(n-2)


                



def main():
        
        print(compute(100))
       
        
  




if __name__ == "__main__":
    main()


