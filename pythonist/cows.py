#https://pythonist.ru/stado-korov/
from functools import wraps
from time import time
from collections import Counter
from math import *
import numpy as np


def cows():
    milk_m=np.arange(1,101).reshape(10,10)
    print(sum(milk_m))
    milk=sum([i for i in range(21,31)])
    print(milk)
   

    
def main():
    cows()
        
    
if __name__ == "__main__":
    main()


