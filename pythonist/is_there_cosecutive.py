#https://pythonist.ru/czifry-idushhie-posledovatelno/
from functools import wraps
from time import time
from collections import Counter
from math import *




def is_there_consecutive(alst, n, times):
    print(''.join(str(i) for i in alst), str(n)*times)
    if ''.join(str(i) for i in alst).find(str(n)*times)==-1:
        return False
   
    return True        



def main():
   
     print(is_there_consecutive([1, 3, 5, 5, 3, 3, 1], 3, 2))
     print(is_there_consecutive([1, 2, 3, 4, 5], 1, 1))
     print(is_there_consecutive([3], 1, 0))
     print(is_there_consecutive([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2))
     print(is_there_consecutive([5, 5, 5, 5, 5], 5, 7))
  
      
    
        
if __name__ == "__main__":
    main()


