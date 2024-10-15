#https://pythonist.ru/preimushhestvenno-polozhitelnyj-spisok/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def is_positive_dominant(alst):

   return len(set([i for i in alst if i>0]))>len(set([i for i in alst if i<0]))
    

        

    
def main():
    print(is_positive_dominant([1, 1, 1, 1, -3, -4]))
    print(is_positive_dominant([5, 99, 832, -3, -4]))
    print(is_positive_dominant([5,0]))
    print(is_positive_dominant([0,-4,-1]))
    
    
 
if __name__ == "__main__":
    main()


