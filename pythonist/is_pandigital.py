#https://pythonist.ru/panczifrovye-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *
import numpy as np



    
def is_pandigital(n):
    sm={0,1,2,3,4,5,6,7,8,9}
    if len(sm&set([int(i) for i in str(n)]))==10:
        return True
    return False
  
    
def main():
 
    print(is_pandigital(98140723568910))
    print(is_pandigital(90864523148909))
    print(is_pandigital(112233445566778899))
    
if __name__ == "__main__":
    main()

