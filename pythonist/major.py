#https://pythonist.ru/slovar-iz-simvolov-i-ih-ascii-kodov/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def to_dict(alst):
    adict={}
    for a in alst:
        key,value=a, ord(a)
        adict[key]=value

    return adict

def main():
    print(to_dict(['a','b','c']))
    print(to_dict(['@']))  



if __name__ == "__main__":
    main()


