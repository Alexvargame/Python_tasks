#https://pythonist.ru/kirpich/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def does_brick_fit(a,b,c,w,h):
    if len([i for i in [a,b,c] if i>max([w,h])])>1:
        return False
    return True
                    
def main():
    print(does_brick_fit(1,1,1,1,1))
    print(does_brick_fit(1,2,1,1,1))
    print(does_brick_fit(1,2,2,1,1))



if __name__ == "__main__":
    main()


