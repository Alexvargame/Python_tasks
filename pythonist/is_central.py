#https://pythonist.ru/v-czentre-ili-net/
from functools import wraps
from time import time
from collections import Counter
from math import *



def is_central(astr):
   
    if len(astr)%2==1 and astr.find(('').join([i for i in astr if i!=' ']))==len(astr)//2:
        return True

    return False

def is_central1(txt):
    return len(txt)%2 and txt[len(txt)//2] != ' '
    
def main():
   
    print(is_central(" # "))
    print(is_central(" 2   "))
    print(is_central("@"))
    
    
    
    
    
        
if __name__ == "__main__":
    main()


