import math
def bank(a, year):
    
    for i in range(year):
        a=a*1.1
        
    return a


a=int(input ('a:', ))
year=int(input('year:', ))
print(bank(a, year))

