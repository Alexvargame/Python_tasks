from time import time
from random import *


def f1(lIn):
    
    l1=sorted(lIn)
    l2=[i for i in l1 if i<500]
    return [i*i for i in l2]

def f2(lIn):
    l1=[i for i in lIn if i<500]
    l2=sorted(l1)
    return [i*i for i in l2]
def f3(lIn):
    l1=[i*i for i in lIn]
    l2=sorted(l1)
    return[i for i in l1 if i<(500*500)]

def timing(lIn,l_f):
    l=[]
    for i in l_f:
        t0=time()
        i(lIn)
        t1=time()
        l.append(t1-t0)
    return l

def main():

    lIn = sample(range(0, 100000000), 10000000)
    print(timing(lIn,[f1,f2,f3]))
    
    #print(f1(lIn))
    # print(f2(lIn))
    # print(f3(lIn))



if __name__ == "__main__":
    main()

