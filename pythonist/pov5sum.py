#https://pythonist.ru/proekt-ejlera-zadacha-30-pyatye-stepeni-czifr/
from functools import wraps, reduce
from time import time
from collections import Counter
from math import *
import re



def compute():
        return sum([i for i in range(10000,99999) if sum([int(j)**5 for j in list(str(i))])==i])
                       
                
        #return [i for i in range(999,9999) if reduce(lambda a,b:int(a)**4+int(b)**4,str(i))==i]
        
                



def main():
        
        print(compute())
       
        
  




if __name__ == "__main__":
    main()


