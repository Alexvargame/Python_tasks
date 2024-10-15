from functools import wraps
from time import time
from collections import Counter
from math import *



def str_match_by2char(astr,bstr):
    ctn=0
    for i in range(min(len(astr),len(bstr))-1):
        if astr[i:i+2]==bstr[i:i+2]:            
            ctn+=1
    return ctn
def main():
   
    print("Тестовые")
    print("count:", str_match_by2char('yytaazz','yyjaaz'))
    print("count:", str_match_by2char('edabit','ed'))
    print("count:", str_match_by2char('',''))
    print("count:", str_match_by2char('bboiiizz','bbuiiiz'))
    print("count:", str_match_by2char('bboiiizz','bbuiiizzzzzz'))

    
 

if __name__ == "__main__":
    main()


