#https://pythonist.ru/fruktovye-soki/
from functools import wraps
from time import time
from collections import Counter
from math import *



def get_drink(astr, bstr):


    return ''.join([a[:3].upper() for a in astr.split()])+''.join([b for b in bstr if b.isdigit()])

    
 
def main():
   
    print(get_drink("apple", "500ml"))
    print(get_drink("passion fruit", "750ml"))
    
        

 


if __name__ == "__main__":
    main()


