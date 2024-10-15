#https://pythonist.ru/proekt-ejlera-zadacha-28-diagonali-chislovoj-spirali/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute(m):


       return 1+sum([(i-1)*10 + 4*((i-2)**2) for i in range(3,m+1,2)])


def main():
        
        print(compute(1001))
       
        
  




if __name__ == "__main__":
    main()


