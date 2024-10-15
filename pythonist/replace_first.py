#https://pythonist.ru/pomenyat-mestami-pervyj-i-poslednij-element-spiska/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def replace_first(alst):

    if len(alst)<2:
        return alst
    a=alst[1:].append(alst[0])
    return a
  
  
    
def main():
    print(replace_first([1, 2, 3,4]))
    





if __name__ == "__main__":
    main()


