#https://pythonist.ru/verno-li-neravenstvo/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def correct_sign(astr):


    
    digit=[int(re.split('>|<', astr)[i])-int(re.split('>|<', astr)[i-1]) for i in range(1,len(re.split('>|<', astr)))]
    symb=[a for a in astr if a=='>' or a=='<']
    return all([(a[0]>0 and a[1]=='<') or (a[0]<0 and a[1]=='>') for a in list(zip(digit,symb))])
def correct_signs1(txt):
    return eval(txt)
def main():
   
    print(correct_sign("3<7<11"))
    print(correct_sign("13 > 44 > 33 > 1"))
    print(correct_sign("1 < 2 < 6 < 9 > 3"))
  
 


if __name__ == "__main__":
    main()


