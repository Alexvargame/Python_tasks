from functools import wraps
from time import time
from collections import Counter
from math import *



def fuct_zeroes(n):

    return sum([n//(5**i) for i  in range(1,round(log(n,5))+1)])
def fuct(n):
    if n==1:
        return 1
    else:
        return n*fuct(n-1)
def revision(m):
     for i in range(len(str(m))):
        if i!=str(m)[::-1].find('0',i):
           return i
def main():
    print(fuct_zeroes(1000))
    #Проверка
    print(revision(fuct(1000)))
    print("*"*20)
    print(fuct_zeroes(20))
    #Проверка
    print(revision(fuct(20)))
    print("*"*20)
    print(fuct_zeroes(6))
    #Проверка
    print(revision(fuct(6)))
    print("*"*20)
        
if __name__ == "__main__":
    main()


