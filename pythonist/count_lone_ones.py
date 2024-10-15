#https://pythonist.ru/podschityvaem-odinokie-ediniczy/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def count_lone_ones(n):
    astr=' '+str(n)+' '
  
    return(len([astr[i] for i in range(len(astr)-1) if astr[i]=='1' and (astr[i-1]!='1' and astr[i+1]!='1')]))
    #print([str(n)[i] for i in range(len(str(n))-1) if str(n)[i]=='1' and (str(n)[i-1]!='1' and str(n)[i+1]!='1')])




  
                
 


def main():
    print("res",count_lone_ones(101))
    print("res",count_lone_ones(1191))
    print("res",count_lone_ones(111))
    print("res",count_lone_ones(462))
  

if __name__ == "__main__":
    main()

