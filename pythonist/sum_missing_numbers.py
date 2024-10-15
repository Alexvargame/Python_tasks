#https://pythonist.ru/komplementarnaya-rnk/
from functools import wraps
from time import time
from collections import Counter
from math import *


def sum_missing_numbers(alst):
    return sum([i for i in range(min(alst),max(alst)+1) if i not in alst])

    
def main():
    print(sum_missing_numbers([4,3,8,1,2]))
    print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
    print(sum_missing_numbers([1, 2, 3, 4, 5]))
    print(sum_missing_numbers([-2, 0, 2]))
    

if __name__ == "__main__":
    main()


