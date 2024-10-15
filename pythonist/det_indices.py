#https://pythonist.ru/vse-vhozhdeniya-elementa-v-spisok/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def get_indices(alst,s):

    adict={}
    for i in range(len(alst)):
        key, value=alst[i], alst[i:].index(alst[i])+i
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
    
    if adict[s]:
       return adict[s]
    else:
       return "no"
    

        

    
def main():
    print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
    print(get_indices([1, 5, 5, 2, 7], 7))
    print(get_indices([1, 5, 5, 2, 7], 5))
    print(get_indices([1, 5, 5, 2, 7], 8))
    
 
if __name__ == "__main__":
    main()


