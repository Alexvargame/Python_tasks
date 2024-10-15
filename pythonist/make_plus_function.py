#https://pythonist.ru/pribavlenie-konstanty/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def plus_five(n):
    return n+5
def make_plus_function(num):
    return plus_five(num)

    
def main():
    print(make_plus_function(6))
    
    

    
if __name__ == "__main__":
    main()


