#https://pythonist.ru/obshhie-elementy/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def l1(alst):
    
    return [i for i in alst if i<5]
def l2(alst,blst):
    
    return [i for i in alst if i in blst]
def l10(astr):
    alst=[int(i) for i in astr.split(',')]
    at=tuple(alst)
    return alst, at
def l11(alst):
    
    return alst[0], alst[-1]
def l13(n):
    
    return n+int(str(n)+str(n))+int(str(n)+str(n)+str(n))

def l14(alst):

    for i in alst:
        if i==5:
            break
        elif i%2==0:
            print(i)
            
        
    return [i for i in alst if i%2==0]

def l15(alst,blst):
    
    return [i for i in alst if i not in blst]


def l17(n):
    
    return reduce(lambda x,y:int(x)+int(y), str(n))

def l18(astr,a):

    return list(astr).count(a)

def l20(alst,n):

    return [i for i in alst if i%15==0]

def l21(alst):

    return len(alst)==len(set(alst))

def l22(atxt):

    adict={}
    for word in atxt.split():
        key, value=len(word), word
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
    adict1={}
    for word in atxt.split():
        print(atxt.count(word), word)
        key, value=atxt.count(word), word
        l1=adict.get(key,[])
        l1.append(value)
        adict1[key]=l1
    return max(adict), adict[max(adict)], max([atxt.count(a) for a in atxt.split()]), adict1

        
def main():
    print(l1([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
    print(l2([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(l10('1,3,4,5,5,5,6'))
    print(l11([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
    print(l13(5))
    print(l14([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
    print(l15([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(l17(12344234))
    print(l18('dqqqgggq','d'))
    print(l20([12,34,30,45,325235,225],15))
    print(l21([12,34,30,30,325235,225]))
    print(l21([12,34,30,45,3,225]))
    print(l22('Напишите программу, которая которая принимает текст выводит два слова: наиболее часто встречающееся самое длинное.'))
    
if __name__ == "__main__":
    main()


