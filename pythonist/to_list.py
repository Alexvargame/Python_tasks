#https://pythonist.ru/preobrazovat-slovar-v-spisok/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def to_list(adict):

    
  
    return [[item, adict[item]] for item in adict]
        

    
def main():
    print(to_list({ "a": 1, "b": 2 }))
   
    
 
if __name__ == "__main__":
    main()


