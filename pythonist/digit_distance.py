#https://pythonist.ru/czifrovoe-rasstoyanie/
from functools import wraps
from time import time
from collections import Counter
from math import *


def digit_distance(num1,num2):
    
    return sum([abs(int(str(num1)[i:i+1])-int(str(num2)[i:i+1])) for i in range(len(str(num1)))])

    
def main():
    print(digit_distance(234,489))
    print(digit_distance(111,400))
    print(digit_distance(210,409))
        

if __name__ == "__main__":
    main()


