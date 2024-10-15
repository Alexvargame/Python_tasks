#https://pythonist.ru/goditsya-li-gora-dlya-voshozhdeniya/
from functools import wraps
from time import time
from collections import Counter
from math import *



def is_scalable(alst):
    if len([abs(alst[i+1]-alst[i]) for i in range(len(alst)-1) if abs(alst[i+1]-alst[i])<6])==len(alst)-1:
        return True
    return False
                
                   
  
           

    
def main():
 
    print(is_scalable([1,2,3,4,6,7,8]))
    print(is_scalable([40,45,50,47,52]))
    print(is_scalable([1,8,11,10,8,7,8]))
    print(is_scalable([11,2,3,4,6,7,8]))
                                         
    
    
if __name__ == "__main__":
    main()


