#https://pythonist.ru/goditsya-li-gora-dlya-voshozhdeniya/
from functools import wraps
from time import time
from collections import Counter
from math import *



def compaire(astr,bstr):
    w1=astr.split(' ')[-1].lower().strip('.')
    w2=bstr.split(' ')[-1].lower().strip('.')
    for i in range(min(len(w1),len(w2))):
        if ord(w1[i])<ord(w2[i]):
            return True
        elif ord(w1[i])>ord(w2[i]):
            return False
                   
  
    
def sort_authors(alst):
    if len(alst)<2:
        return alst
    else:
        pivot=alst[0]
        less=[i for i in alst[1:] if compaire(i, pivot)]
        greater=[i for i in alst[1:] if not compaire(i, pivot)]
        return sort_authors(less)+[pivot]+sort_authors(greater)
        
        
  
           

    
def main():
 
    print(sort_authors(["J. K. Rowling", "w. s.", "lewis carroll", "M. M."]))
    print(sort_authors(["J. L.", "J. B. priestley", "L. C.", "Suzanne Collins"]))
    print(sort_authors(["J. K. Rowling", "WW", "carroll", "M. M.","WW"]))
    
    
    
if __name__ == "__main__":
    main()


