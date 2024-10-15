#https://pythonist.ru/koridor/
from functools import wraps
from time import time
from collections import Counter
from math import *



def possible_path(alst):
    adict={1:['H'], 2:['H'], 3:['H'], 4:['H'], 'H':[1,2,3,4]}
    for i in range(len(alst)-1):
        if alst[i] in adict[alst[i+1]]:
           pass

    return len(['*' for i in range(len(alst)-1) if alst[i] in adict[alst[i+1]]])==len(alst)-1


def main():
   
    print(possible_path([1, "H", 2, "H", 3, "H", 4]))
    print(possible_path([2, "H", 3]))
    print(possible_path([1, 2, "H", 3, "H", 4]))
   
        
if __name__ == "__main__":
    main()


