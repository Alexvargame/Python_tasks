#https://pythonist.ru/ediniczy-i-nuli/
from functools import wraps
from time import time
from collections import Counter
from math import *




    
def same_length(n):
    
    if len(str(n))%2==0 and (set(list(str(n)[:int(len(str(n))/2)]))& set(list(str(n)[int(len(str(n))/2):]))==set()):
        return True
                        
    else:
        for i in str(n):
            if i=='1':
                pos=str(n).find('0')
                if str(n)[pos:].find('1')==pos:
                    return same_length(int(str(n)[pos*2:]))
    return False
                
                
 


def main():
    print("res",same_length(1100))
    print("res",same_length(110011100010))
    print("res",same_length(11001110010))




if __name__ == "__main__":
    main()

