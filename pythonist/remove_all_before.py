#https://pythonist.ru/udalit-vse-elemety-spiska-do-opredelennogo/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def remove_all_before(alst,n):

    if n in alst:
        return alst[alst.index(n):]
    return alst
  
  
    
def main():
    print(remove_all_before([1, 2, 3,4,5],3))
    print(remove_all_before([1, 2, 3,4,5],6))
    print(remove_all_before([1, 2, 2,4,5],2))
    





if __name__ == "__main__":
    main()


