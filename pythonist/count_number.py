#https://pythonist.ru/czifrovoe-rasstoyanie/
from functools import wraps
from time import time
from collections import Counter
from math import *


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def count_number(alst):
   
    for i in alst:
        if isfloat(i):
            print(i)
    return len([item for item in alst if isfloat(item)])

    
def main():
    print(count_number([" ", 17.2, 5, "edabit"]))
    #print(count_number([["", 17.2, 5, "edabit"]]))
    #print(count_number([[[[[2, 14]]], 2, 3, 4]]))
    #print(count_number([["number"]]))
        

if __name__ == "__main__":
    main()


