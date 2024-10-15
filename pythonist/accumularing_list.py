#https://pythonist.ru/nakaplivayushhayasya-summa/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def accumulating_list(alst):

    return [reduce(lambda x,y:x+y, alst[:i+1]) for i in range(len(alst))]


def main():
    print(accumulating_list([1,2,3,4]))
    print(accumulating_list([1, 0, 1, 0, 1]))
    print(accumulating_list([]))
    

    
if __name__ == "__main__":
    main()


