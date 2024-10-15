#https://pythonist.ru/igry-so-slozheniem/
from functools import wraps
from time import time
from collections import Counter
from math import *



def closing_in_sum(n):

    if len(str(n))%2==1:
     
        return sum([int(str(n)[i]+str(n)[-1-i]) for i in range(len(str(n))//2)])+int(str(n)[len(str(n))//2])

    return sum([int(str(n)[i]+str(n)[-1-i]) for i in range(len(str(n))//2)])

def is_central1(txt):
    return len(txt)%2 and txt[len(txt)//2] != ' '
    
def main():
   

    print(closing_in_sum(2520))
    print(closing_in_sum(151))
    
    
    
    
    
    
        
if __name__ == "__main__":
    main()


