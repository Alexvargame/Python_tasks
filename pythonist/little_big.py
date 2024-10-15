#https://pythonist.ru/malenkaya-bolshaya-posledovatelnost/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def little_big(n):

    if n%2==0:
        return int(100*(2**(n/2-1)))
    else:
        return int(5+n//2)
    
            
      

def main():
   
    print(little_big(4))
    print(little_big(5))
    print(little_big(9))
    print(little_big(28))
    


if __name__ == "__main__":
    main()


