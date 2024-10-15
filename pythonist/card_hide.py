#https://pythonist.ru/skryvaem-nomer-kreditnoj-karty/
from functools import wraps
from time import time
from collections import Counter
from math import *



def card_hide(astr):
   

    
    return ('').join(['*' for i in astr[:12]])+astr[12:]

     
def main():
   
    print(card_hide('1234123456785678'))

    
    
    
    
        
if __name__ == "__main__":
    main()


