#https://pythonist.ru/skolko-raz-pridetsya-umnozhit/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def multiplication(n,count):
        if len(str(n))==1:
                return count
        else:   
                count+=1 
                return multiplication(sum([reduce(lambda a,b:a*b, map(int,str(n)))]),count)
                
                    
def main():
    print(multiplication(999,0))



if __name__ == "__main__":
    main()


