import math
from datetime import *

def date_(y,m,d):
    d=date(y,m,d)
    if d>date.today():
        return False
    else:return True

        


d=int(input ('d:', ))
m=int(input ('m:', ))
y=int(input ('y:', ))


print(date_(y,m,d))



