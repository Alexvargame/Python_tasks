#https://pythonist.ru/czvetnye-karandashi/
from functools import wraps
from time import time
from collections import Counter
from math import *


def color_pattern_time1(cols):
    t1=time()
    ccl=0
    ctime=0
    for i in range(len(cols)-1):
        if cols[i+1]!=cols[i]:
            ccl+=1
    ctime=len(cols)*2+ccl
    return ctime

def color_pattern_time(cols):
    adict={}
    ch=0
    for i in range(len(cols)):
        key, value=cols[i], i
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
    for ad in adict:
        ch+=len(adict[ad])-(adict[ad][-1]-adict[ad][0])
    return ch+len(cols)*2-1
    
def main():

    print(color_pattern_time1(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))
    print(color_pattern_time1(["Blue", "Blue", "Red", "Blue", "Red", "Red"]))
    print(color_pattern_time1(["Blue"]))
    print(color_pattern_time1(["Red", "Yellow", "Green", "Blue"]))
    print("*"*10)
    
    print(color_pattern_time(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))
    print(color_pattern_time(["Blue", "Blue", "Red", "Blue", "Red", "Red"]))
    print(color_pattern_time(["Blue"]))
    print(color_pattern_time(["Red", "Yellow", "Green", "Blue"]))

if __name__ == "__main__":
    main()


