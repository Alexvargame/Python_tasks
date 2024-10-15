#https://pythonist.ru/vse-vhozhdeniya-elementa-v-spisok/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def check_perfect(n):

   return sum([i for i in range(1,n//2+1) if n%i==0])==n
    

        

    
def main():
    print(check_perfect(7))
    print(check_perfect(6))
    print(check_perfect(28))
    print(check_perfect(97))
    print(check_perfect(9))
    
    
 
if __name__ == "__main__":
    main()


