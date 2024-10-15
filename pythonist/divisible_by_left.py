#https://pythonist.ru/kratna-li-czifra-czifre-sleva/
from functools import wraps
from time import time
from collections import Counter
from math import *



def divisible_by_left(n):
        return [False]+[int(str(n)[i])%int(str(n)[i-1])==0 for i in range(1,len(str(n)))]


def main():
   
    print(divisible_by_left(73312))
    print(divisible_by_left(222))
    print(divisible_by_left(1))
            
if __name__ == "__main__":
    main()


