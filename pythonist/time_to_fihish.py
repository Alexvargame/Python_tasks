#https://pythonist.ru/dopishite-do-tochki/
from functools import wraps
from time import time
from collections import Counter
from math import *



def time_to_finish(astr, bstr):

    return len(''.join(astr.replace(bstr,'').split()))/2
    
     
def main():
   
    print(time_to_finish("And so brings my conclusion to its conclusion.",
   "And so brings my conclus"))
    print(time_to_finish("And so brings my conclusion to its conclusion.",
   "And so brings my conclusion to"))
    print(time_to_finish( "Thank you for reading my essay.",
   "T"))
    print(time_to_finish( "As a result, my point is still valid.",
   "As a result, my"))
    
    
    
        
if __name__ == "__main__":
    main()


