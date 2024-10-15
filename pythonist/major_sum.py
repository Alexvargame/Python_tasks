#https://pythonist.ru/naibolshee-absolyutnoe-znachenie/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def major_sum(alst):

    a=sum([a for a in alst if a>0])
    b=sum([b for b in alst if b<0])
    c=len([c for c in alst if c==0])

       

    return max(a,abs(b),c)


def main():
    print(major_sum([1, 2, 3, 4, 0, 0, -3, -2]))
    print(major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]))
    print(major_sum([0, 0, 0, 0, 0, 1, 2, -3]))

    
if __name__ == "__main__":
    main()


