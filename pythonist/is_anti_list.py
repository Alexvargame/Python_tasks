#https://pythonist.ru/antispiski/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def is_anti_list(alst, blst):
        return all([i[0]!=i[1] for i in list(zip(alst,blst))])

def main():
    print(is_anti_list(["1", "0", "0", "1"], ["0", "1", "1", "0"]))
    print(is_anti_list(["apples", "bananas", "bananas"], ["bananas", "apples", "apples"]))
    print(is_anti_list(["1", "1", "0", "1"], ["0", "1", "1", "0"]))
    print(is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]))


    
 
if __name__ == "__main__":
    main()


