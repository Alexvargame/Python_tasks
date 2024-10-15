#https://pythonist.ru/polozhitelnye-i-otriczatelnye-chisla/
from functools import wraps
from time import time
from collections import Counter
from math import *



def alternative_pos_neg(alst):
    if (0 in alst) or (len(alst)%2==1 and alst[0]*alst[-1]<0):
       
        return False
    return all(alst[i]*alst[i-1]<0 for i in range(1,len(alst),2))# if alst[i]*alst[i-1]<0])


     
def main():
   
    print(alternative_pos_neg([3, -2, 5, -5, 2, -8]))
    print(alternative_pos_neg([-6, 1, -1, 4, -3]))
    print(alternative_pos_neg([4, 4, -2, 3, -6, 10]))
    print(alternative_pos_neg([3, -2, 5, -5, -2]))
    print(alternative_pos_neg([3, -2, 5, -5, 0, -8]))
    

    
    
    
    
        
if __name__ == "__main__":
    main()


