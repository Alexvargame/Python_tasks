#https://pythonist.ru/validacziya-pin-koda/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def is_valid(astr):
    
    if len(astr) not in [4,6]:# or len(astr)!=6:
        return False
    elif len([i for i in astr if i.isdigit()])==len(astr):
        return True
    return False
   
      
                
 


def main():
    print("res",is_valid('1234'))
    print("res",is_valid('12344'))
    print("res",is_valid('1ss23'))
    print("res",is_valid('120003'))
    print("res",is_valid('123f'))
   
    
  

if __name__ == "__main__":
    main()

