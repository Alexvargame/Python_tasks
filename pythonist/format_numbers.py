#https://pythonist.ru/preobrazovanie-telefonnyh-nomerov/
from functools import wraps
from time import time
from collections import Counter
from math import *



def compaire(astr,bstr):
    w1=astr.split(' ')[-1].lower().strip('.')
    w2=bstr.split(' ')[-1].lower().strip('.')
    for i in range(min(len(w1),len(w2))):
        if ord(w1[i])<ord(w2[i]):
            return True
        elif ord(w1[i])>ord(w2[i]):
            return False
                   
  
    
def format_numbers(astr):
    alst=[i for i in astr if ord(i) in range(ord('0'),ord('9')+1)]
    return '+'+alst[0]+'('+('').join(alst[1:4])+')'+('').join(alst[4:7])+'-'+('').join(alst[7:9])+'-'+('').join(alst[9:11])
        
        
  
           

    
def main():
 
    print(format_numbers('+79091011010'))
    print(format_numbers('8(909)1011010'))
    print(format_numbers('+7 909 101-10-10'))
        
    
if __name__ == "__main__":
    main()


