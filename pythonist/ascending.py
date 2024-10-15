#https://pythonist.ru/vozrastayushhie-i-posledovatelnye-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *



def ascending1(astr):
    l=len(astr)
    for i in range(2,l+1):
        if l%i==0:
            for j in range(i-1):
                alst=[]
                if int(astr[l//i*(j+1):l//i*(j+2)])-int(astr[j*l//i:l//i*(j+1)])!=1:
                    break
                else:
                    alst.append(int(astr[l//i*(j+1):l//i*(j+2)])-int(astr[j*l//i:l//i*(j+1)]))
            if set(alst)=={1}:
                return True
        
    return False       
                   
  
           
def ascending(astr):
    l=len(astr)
    for i in range(2,len(astr)+1):
        if l%i==0:
            if set([int(astr[l//i*(j+1):l//i*(j+2)])-int(astr[j*l//i:l//i*(j+1)]) for j in range(i-1)])=={1}:
                return True
        
    return False       
                   
    
def main():
 
    print(ascending('232425'))
    print(ascending('444445'))
    print(ascending('23242527'))
    print(ascending('12345'))
    
if __name__ == "__main__":
    main()


