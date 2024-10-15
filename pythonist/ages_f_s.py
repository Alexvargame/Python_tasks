from functools import wraps
from time import time
from collections import Counter
from math import *



def age_diff(f_age,s_age):
    dif=f_age/s_age
    if dif==2:
        return "now"
    elif dif>2:
        i=0
        while dif!=2:
            i=i+1
            dif=(f_age-i*(-1))/(s_age-i*(-1))
            
        return i
    else:
        i=0
        while dif!=2:
            i=i+1
            dif=(f_age-i)/(s_age-i)
        return i
def main():

    
    print("Тестовые")
    print("year:", age_diff(36,7))
    print("year:", age_diff(55,30))
    print("year:", age_diff(42,21))
    

    
 

if __name__ == "__main__":
    main()


