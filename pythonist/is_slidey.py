#https://pythonist.ru/skolzyashhie-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *



def is_slidey(anum):
    alst=list(str(anum))
    if len(str(anum))==1 or set([abs(int(alst[i+1])-int(alst[i])) for i in range(len(alst)-1)])=={1}:
        return True
    return False
           

    
def main():
 
    print(is_slidey(123454321))
    print(is_slidey(54345))
    print(is_slidey(987654321))
    print(is_slidey(1123))
    print(is_slidey(1247))
    print(is_slidey(1))
    print(is_slidey(135))
  
if __name__ == "__main__":
    main()


