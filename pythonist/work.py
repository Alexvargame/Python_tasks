#https://pythonist.ru/transportirovka-materialov-iz-czeha-a-v-czeh-b/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re


def work(task):
    b=[]
    skd=[]
    if not task:
        return True
    for i  in range(len(task)):
        if task[i]==min(task[i:]):
            if task[i]<skd[-1]:
                b.append(task[i])
            else:
                b.append(skd[-1])
                skd.pop(-1)
                sld.append(task[i])
        else:
            skd.append(task[i])
    for i in range(len(skd)):
        if skd[i]==max(skd[i:]):
            b.append(skd[i])
        else:
            break
    return len(b)==len(task)
                    
def main():
    print(work([2.9, 2.1]))
    print(work([5.6, 9.0,2.0]))
    print(work([5.6, 5.5,1.0,2.0]))



if __name__ == "__main__":
    main()


