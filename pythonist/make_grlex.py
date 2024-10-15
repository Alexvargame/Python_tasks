#https://pythonist.ru/slozhnoe-uporyadochivanie/
from functools import wraps
from time import time
from collections import Counter
from math import *



def make_grlex(alst):
    blst=alst.copy()
    return blst
    
def main():
   
    print(make_grlex(["small", "big"]))
    print(make_grlex(["cat", "ran", "for", "the", "rat"]))
    print(make_grlex(["this", "is", "a", "small", "test"]))


if __name__ == "__main__":
    main()


