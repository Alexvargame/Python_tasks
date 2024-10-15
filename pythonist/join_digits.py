#https://pythonist.ru/soedinite-chisla-defisami/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re




def join_digits(n):

    return '-'.join(['-'.join(str(i)[j] for j in range(len(str(i)))) for i in range(1, n+1)])
    
  
    return   set(adict[max(adict)])
    
def main():
    print(join_digits(4))
    print(join_digits(11))






if __name__ == "__main__":
    main()


