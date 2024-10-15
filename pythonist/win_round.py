#https://pythonist.ru/pronumerovannye-karty/
from functools import wraps
from time import time
from collections import Counter
from math import *



def win_round(alst, blst):

    if int(str(max(alst))+ str(max(alst[:alst.index(max(alst))]+alst[alst.index(max(alst))+1:])))>int(str(max(blst))+ str(max(blst[:blst.index(max(blst))]+alst[blst.index(max(blst))+1:]))):
            return True
    
    return False

def main():
   
    print(win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))
    print(win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
    print(win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]))
   
        
if __name__ == "__main__":
    main()


