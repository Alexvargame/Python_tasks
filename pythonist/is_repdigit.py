#https://pythonist.ru/yavlyaetsya-li-chislo-repdigit/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def is_repdigit(n):

    if n>0 and len(set([i for i in str(n)]))==1:
        return True
    return False

    
def main():
    print(is_repdigit(66))
    print(is_repdigit(0))
    print(is_repdigit(-11))
    print(is_repdigit(63))
    
 
if __name__ == "__main__":
    main()


