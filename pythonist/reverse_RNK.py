#https://pythonist.ru/komplementarnaya-rnk/
from functools import wraps
from time import time
from collections import Counter
from math import *


def reverse_rnk(astr):
    adict={'A':'U','C':'G','G':'C','U':'A'}
    return ('').join([adict[item] for item in astr ])[::-1]

    
def main():
    print(reverse_rnk('GUGU'))
    print(reverse_rnk('UCUCG'))
    print(reverse_rnk('CAGGU'))


if __name__ == "__main__":
    main()


