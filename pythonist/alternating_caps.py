#https://pythonist.ru/spongecase/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def alternating_caps(astr):

    return ''.join([astr[i].upper() if i%2==0  else astr[i] for i in range(len(astr))])
##def alternating_caps(txt):
##    res = ''
##    cap = True
##    for ch in txt:
##        res += ch.upper() if cap else ch.lower()
##        if ch.isalpha():
##            cap = not cap
##    return res                  
def main():
    print(alternating_caps('Hello'))
    print(alternating_caps('How are you?'))
    print(alternating_caps('OMG this website is awesome!'))



if __name__ == "__main__":
    main()


