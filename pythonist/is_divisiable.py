#https://pythonist.ru/kratno-li-chislo-summe-czifr-etogo-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def is_divisiable(n):
  
    return n%sum([int(i) for i in str(n)])==0


  
                
 


def main():
    print("res",is_divisiable(75))
    print("res",is_divisiable(171))
    print("res",is_divisiable(481))
    print("res",is_divisiable(89))
    print("res",is_divisiable(516))
    print("res",is_divisiable(200))
    
    
  

if __name__ == "__main__":
    main()

