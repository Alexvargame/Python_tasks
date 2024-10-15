#https://pythonist.ru/proekt-ejlera-zadacha-6-raznost-mezhdu-summoj-kvadratov-i-kvadratom-summy/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def compute(n):
        
        return (sum([i for i in range(1,n+1)]))**2-sum([i**2 for i in range(1,n+1)])

def compute1(n):
        
        return reduce(lambda a,b:a*b, range(1,n+1))

def main():
    
    print(compute(100))
    print(compute1(10))



if __name__ == "__main__":
    main()


