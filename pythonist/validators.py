from functools import wraps
from time import time
from collections import Counter
from math import *



def is_shifted(alst, blst):
    dif=alst[0]-blst[0]
    for a,b in zip(alst,blst):
        if (a-b)!=dif:
            return False
    return "Разница между элементами массивов"'{}'.format(dif)

def is_multipled(alst, blst):
    try:
        dif=alst[0]/blst[0]
        for a,b in zip(alst,blst):
            if (a/b)!=dif:
                return False
        return "Множитель между элементами массивов"'{}'.format(dif)
    except:
        return False
    
    


def main():
    print(is_shifted([1,2,3,4],[5,6,7,8]))
    print(is_shifted([1,2,3,4],[5,6,7,9]))
    print(is_multipled([1,2,3,4],[5,6,7,8]))
    print(is_multipled([1,2,3,4],[10,20,30,40]))
    print(is_multipled([0,0,0,0],[5,6,7,8]))
    print(is_multipled([0,2,3,4],[5,6,7,8]))
    print(is_multipled([1,2,3,4],[0,6,7,8]))
    
        
if __name__ == "__main__":
    main()


