#https://pythonist.ru/zadacha-1-proekt-ejlera//
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute(n):
        
        return sum([i for i in range(1,n) if not all(kr(i))])
        

def kr(i):
        alst=[3,5,7,11,13,17]
        return [i%j for j in alst]

       
def main():
        alst=[3,5]
        print(compute(10))
        print(compute(100))
  



if __name__ == "__main__":
    main()


