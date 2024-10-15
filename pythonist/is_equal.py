#https://pythonist.ru/ravny-li-summy-czifr-v-chislah/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def is_equal(alst):

    return sum([int(i) for i in str(alst[0])])==sum([int(i) for i in str(alst[1])])
 
            
   
       


    



def main():
   
    print(is_equal([105,42]))
    print(is_equal([145,42]))


if __name__ == "__main__":
    main()


