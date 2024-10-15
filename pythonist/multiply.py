#https://pythonist.ru/mnozhitel-spiskov/
from functools import wraps
from time import time
from collections import Counter
from math import *



def multiplay(alst):
   
    return [[alst[i] for k in range(len(alst))]  for i in range(len(alst)) ] 
        

    
def main():
    
    print(multiplay([4,5]))
    print(multiplay(["*", "%", "$"]))
    print(multiplay(["A", "B", "C", "D", "E"]))
    print(multiplay([]))
    print(multiplay([3,4,5])) 
    
        

if __name__ == "__main__":
    main()


