from functools import wraps
from time import time
from collections import Counter
from math import *



def sum_n(l_1,n):
    summ=0
    for i in range(n-1,len(l_1)//n*n,n):
        summ=summ+l_1[i]
    return summ
def sum_every_nth(alst,n):
    return sum(alst[n-1::n])
def main():
    #l_1=[1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7]
    #n=3
    print("sum:",sum_n([1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7],3))
    print("sum:",sum_n([1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7],6))
    print("sum:",sum_n([1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7],10))
    

    print("Тестовые")
    print("sum:", sum_n([4,8,6,6,7,9,3],1))
    print("sum:",sum_n([7,3,10,4,5,8,4,9,6,9,10,1],4))
    print("sum:",sum_n([10,6,5,4,5,2,3,3,8,10,7,2],8))
    
    print(sum_every_nth([1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7],6))
    

    
 

if __name__ == "__main__":
    main()


