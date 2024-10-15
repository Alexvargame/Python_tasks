#https://pythonist.ru/ravny-li-poslednie-czifry/
from functools import wraps
from time import time
from collections import Counter
from math import *



def last_dig(a,b,c):
   
    if str(a*b)[-1]==str(c)[-1]:
        return True
    
    return False

     
def main():
   
    print(last_dig(25,21,125))
    print(last_dig(55,226,5190))
    print(last_dig(12,215,0))

    
    
    
    
        
if __name__ == "__main__":
    main()


