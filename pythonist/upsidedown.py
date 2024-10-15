#https://pythonist.ru/perevorot/
from functools import wraps
from time import time
from collections import Counter
from math import *

#в зеленом поток мыслей, но никуда ни приведший
"""
def upsidedown1(n):
    if len([0 for k,v in Counter(str(''.join([i for i in str(n)[::-1]]))).items() if k!='0' and int(v)%2!=0])>0:
        return False
    
    return True

def upsidedown2(n):
    #print([str(int(i)//3) for i in str(n)])
    l=['6','9']
    if int(''.join([str(int(54/int(i))) for i in str(n)[::-1] if i in l]))-n:
         return False
    return True
""" 
def upsidedown(n):
    nn=''
    for i in str(n)[::-1]:
        if i!='0' and i=='9':
            i='6'
        elif i=='6':
            i='9'
        else:
            pass
        nn+=i
    return nn==str(n)

    
def upsidedown1(n):
    adict={'0':0,'9':6,'6':9}
    if str(n)!=''.join([str(adict[i]) for i in str(n)[::-1]]):
        return False
    
    return True
    
def main():
   
    print(upsidedown(6090609))
    print(upsidedown(6969))
    print(upsidedown(9669))
    print(upsidedown(69069069))
    print("*"*10)
    print(upsidedown1(6090609))
    print(upsidedown1(6969))
    print(upsidedown1(9669))
    print(upsidedown1(69069069))
    
if __name__ == "__main__":
    main()


