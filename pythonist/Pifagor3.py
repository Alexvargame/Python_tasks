#https://pythonist.ru/proekt-ejlera-zadacha-9-osobaya-trojka-pifagora/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def compute(n):
    l=[]

    for i in range(1,n):
        for j in range(i,n):
          
            
            if sqrt(i**2+j**2)+i+j==n:
                t=(i,j,sqrt(i**2+j**2))
                l.append(t)

    return l
            




                    
def main():
   print(compute(1000))



if __name__ == "__main__":
    main()


