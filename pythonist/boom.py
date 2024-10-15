#https://pythonist.ru/boom/
from functools import wraps
from time import time
from collections import Counter
from math import *



def boom1(alst):
    for i in alst:
        if '7' in str(i):
            
            return "Boom"
    return False
def boom(alst):
    if len([i for i in alst if '7' in str(i)])>0:
        return "Boom"
    return False
    
    
    
def main():
   
    print(boom([1,2,3,4,5,6,7]))
    print(boom([1,2,3,4,5,6,]))
    print(boom([1,2,3,4,5,6,97]))
    print(boom([]))
if __name__ == "__main__":
    main()


