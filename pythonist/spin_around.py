#https://pythonist.ru/skolko-polnyh-oborotov/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def spin_around(alst):
 i=0
 count=0
 if len(alst)<4:
     return 0
 while i<len(alst)-3:
    if len(set(alst[i:i+4]))==1:
        print(alst[i:i+4])
        i=i+4
        count=count+1
    else:
        i=i+1
 return count
            
   
       


    



def main():
   
    print(spin_around(["left", "right", "left", "right"]))
    print(spin_around(["left", "left", "left", "left"]))
    print(spin_around(["right","left", "left", "left", "left"]))
    print(spin_around(["right","right","right","right","right","left", "left", "left", "left"]))
      
 


if __name__ == "__main__":
    main()


