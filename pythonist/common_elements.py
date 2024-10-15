#https://pythonist.ru/obshhie-elementy/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def common_elements(alst, blst):
    
    return list(set(alst)&set(blst))

    
def main():
    print(common_elements([-1, 3, 4, 6, 7, 9], [1, 3]))
    print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]))
    print(common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]))
    print(common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]))
    
    

    
if __name__ == "__main__":
    main()


