from functools import wraps
from time import time
from collections import Counter
from math import *



def difference(l_1):
    
    l=[b-a for a,b in zip(sorted(l_1), sorted(l_1[1:]))]
    
    return max(l)

def main():
    l_1=[1,2,7,3,56,6,37,8,68,62,5,3,68,8,7,3,4,4,6,7]
    print(difference(l_1))
    print("Тестовые")
   
    

    
 

if __name__ == "__main__":
    main()


