
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def major(alst):
    adict=Counter(alst)
    
    
    return list(set([a for a in alst if Counter(alst)[a]>len(alst)/2]))

def main():
    print(major([4,2,2]))
    print(major([4,5,6,7,8,8,8,8,8]))  



if __name__ == "__main__":
    main()


