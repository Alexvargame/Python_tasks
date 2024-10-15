#https://pythonist.ru/skladyvaem-konczy/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def ends_add_to_10(alst):


    return len([i for i in alst if int(str(abs(i))[0])+int(str(abs(i))[-1])==10])
      
                
 


def main():
    print("res",ends_add_to_10([19,46,2098]))
    print("res",ends_add_to_10([33,44,-55]))
    print("res",ends_add_to_10([10]))
    
    
  

if __name__ == "__main__":
    main()

