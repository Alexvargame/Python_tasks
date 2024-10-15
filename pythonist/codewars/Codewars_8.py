from itertools import permutations
from math import sqrt
from functools import reduce
import re

                   

def sobes1(d):
    d1={}
    for k,v in d.items():
        k,v=v,k
        d1[k]=v

    return d1
def sobes2(l1,l2):
    d1={}
    for i in range(len(l1)):
        key,value=l1[i],l2[i]
        d1[key]=value

    return d1


def sobes3(l):
    
    return [item for sublist in l for item in sublist] 


def sobes4(l1,l2):
    
    return list(set([el for el in l1 if el in l2]))

def sobes8(d):
  
    
    return [k for k in d.keys() if d[k] in sorted(d.values())[-3:]]
                                                                    
def main():

   
    print(sobes1({1:'value1', 2: 'value2'}))
    print(sobes2([1,2,3],['q','w','e']))
    print(sobes3([[1,2,3],[4,5,6]]))
    print(sobes4([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(sobes8({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}))
    

   


if __name__ == "__main__":
    main()

