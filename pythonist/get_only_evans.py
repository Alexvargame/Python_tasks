#https://pythonist.ru/chisla-chetnye-so-vseh-storon/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def get_only_evens(alst):


    return [i[1] for i in enumerate(alst) if i[0]%2==0 and i[1]%2==0]
      
                
 


def main():
    print("res",get_only_evens([1,3,6,6,4,8]))
    print("res",get_only_evens([0,1,2,3,4]))
    print("res",get_only_evens([1,2,3,4,5,6]))
    
  

if __name__ == "__main__":
    main()

