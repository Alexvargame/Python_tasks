#https://pythonist.ru/yavlyaetsya-li-input-faktorialom-chisla/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def is_factorial(n):
    i,f = 1,1
    while f < n:
        i+=1
        f*= i
    return n == f                
                    
def main():
    print(is_factorial(24))



if __name__ == "__main__":
    main()


