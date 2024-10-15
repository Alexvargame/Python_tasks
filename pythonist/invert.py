#https://pythonist.ru/invertiruem-klyuchi-i-znacheniya-v-slovare/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def invert(adict):
    adict1={}
    print(adict)
    for key, value in adict.items():
        key, value=value, key
        adict1[key]=value

    return   adict1



def invert(d):
    return {v: k for k, v in d.items()
def invert(dct):
    return dict(zip(dct.values(),dct.keys()))
    
def main():
    print(invert({ "z": "q", "w": "f" }))
    





if __name__ == "__main__":
    main()


