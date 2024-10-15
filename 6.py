import math
from random import randint
def is_prime(a):
    for i in range(a//2+1):
        if (a%(i+2)==0):
            return False
        else:
            return True
            break
        
        
        

a=randint(1,1000)
#a=int(input ('a:', ))

print(a, is_prime(a))

