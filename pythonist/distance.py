from functools import wraps
from time import time
from collections import Counter
from math import *



def distance(astr):
    alist=astr.split(',')
    return round(sqrt((int(alist[2])-int(alist[0]))**2+(int(alist[3])-int(alist[1]))**2),2)

def main():
    print(distance("1,1,4,5"))
    print(distance("1,1,2,1"))
    print(distance("1,1,3,1"))
    print(distance("-5,1,3,1"))
    print(distance("-5,2,3,1"))
        
if __name__ == "__main__":
    main()


