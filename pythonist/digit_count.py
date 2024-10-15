#https://pythonist.ru/podschet-czifr/
from functools import wraps
from time import time
from collections import Counter
from math import *



def digit_count(n):
    
    adict=Counter(str(n))
##    for i in str(n):
##        key, value=i, count(i)
##        adict[key]=value

    return int(('').join([str(adict[i]) for i in str(n)]))

    
    
def main():
   
    print(digit_count(136116))
    print(digit_count(221333))
    print(digit_count(123344))
    print(digit_count(2))
    print(digit_count(1))
    
    
    
    
        
if __name__ == "__main__":
    main()


