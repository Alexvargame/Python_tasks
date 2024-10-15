#https://pythonist.ru/sortirovka-chisel-po-ih-dline/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def number_len_sort(alst):
 
    return sorted([i for i in alst], key=lambda x: len(str(x)))
      
                
 


def main():
    print("res",number_len_sort([1,54,12,2,463,2]))
    print("res",number_len_sort([999, 421, 22, 990, 32]))
    print("res",number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]))
   
    
    
  

if __name__ == "__main__":
    main()

