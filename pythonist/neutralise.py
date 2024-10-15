#https://pythonist.ru/nejtralizacziya/
from functools import wraps
from time import time
from collections import Counter
from math import *


def add(t):
    if t[0]==t[1]:
        return t[0]
    return '0'

def neutralise(astr, bstr):

    return ('').join([add(i) for i in list(zip(astr,bstr))])
        



def main():
   
     print(neutralise('+-+', '+--'))   
     print(neutralise("-+-+-+", "-+-+-+"))
     print(neutralise("-++-", "-+-+"))   
    
    
        
if __name__ == "__main__":
    main()


##def neutralise(s1, s2):
##    return ''.join(a if a == b else '0' for a, b in zip(s1, s2)
##
##neutralise=lambda a,b:"".join(["0",x][x==y]for x,y in zip(a,b))
##
