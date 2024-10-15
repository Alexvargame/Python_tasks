#https://pythonist.ru/samyj-dlitelnyj-period-vremeni/
from functools import wraps
from time import time
from collections import Counter
from math import *



    
def longest_time(*args):
    #m=[args[i]/60**i for i in range(len(args))]
    return args[[args[i]/60**i for i in range(len(args))].index(max([args[i]/60**i for i in range(len(args))]))]
        
        
  
           

    
def main():
 
    print(longest_time(1,59,3598))
    print(longest_time(2,300,15000))
    print(longest_time(15,955,59400))
       
if __name__ == "__main__":
    main()

