#https://pythonist.ru/dva-unikalnyh-elementa/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def return_unique(alst):
    adict={}

    for a in alst:
        key, value=a, alst.count(a)
        adict[key]=value
    
    
    
  
    return   [key for key in adict if adict[key]<2]   
def return_unique1(lst):
  return [i for i in lst if lst.count(i)==1]
    
def main():
    print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
    print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
    print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
    
 
if __name__ == "__main__":
    main()


