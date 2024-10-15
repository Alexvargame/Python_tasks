#https://pythonist.ru/tip-posledovatelnosti/
from functools import wraps
from time import time
from collections import Counter
from math import *



def seq_level(alst, adict,j):
    if len(set([alst[i+1]-alst[i] for i in range(len(alst)-1)]))==1:
        print("5")
        return adict[str(j)]
    else :
        j=j+1
        alst=[alst[i+1]-alst[i] for i in range(len(alst)-1)]
        return seq_level(alst, adict,j)
        

    
def main():
    adict={'1':'Linear', '2':'Quadratic','3':'Cubic'}
    
    print(seq_level([1,2,3,4,5], adict,1))
    print(seq_level([3,6,10,15,21], adict,1))
    print(seq_level([4, 14, 40, 88, 164],adict,1))
        

if __name__ == "__main__":
    main()


