#https://pythonist.ru/vse-chetnye-chisla-do-opredelennogo-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def find_even_nums(n):


    return [i for i  in range(0,n+1,2)]
    

        

    
def main():
    print(find_even_nums(8))
    
    
 
if __name__ == "__main__":
    main()


