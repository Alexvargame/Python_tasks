#https://pythonist.ru/schitaem-povtory/
from functools import wraps
from time import time
from collections import Counter
from math import *



def repeats(astr):
    acnt=Counter(astr)
    return sum([av for ak, av in acnt.items()])-len(acnt)
    
def main():
    print(repeats("ruti riw"))
    print(repeats("footbar"))
    print(repeats("helicopter"))
    print(repeats("birthday"))
if __name__ == "__main__":
    main()


