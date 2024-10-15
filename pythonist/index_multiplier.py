#https://pythonist.ru/yavlyaetsya-li-chislo-repdigit/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def index_multiplier(alst):
    l=[]

    return sum( a*d for a,d in enumerate(alst))
    

        

    
def main():
    print(index_multiplier([1,2,3,4,5]))
    
    
 
if __name__ == "__main__":
    main()


