print("{:,}".format(1000000))
print("0000")
str_='2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25'

l=str_.split(',')
l1=[]
l2=[]
for i in l:
    i=float(i)
    l1.append(i)
print(max(l1), min(l1))
for i in sorted(l1):
    l2.append(f'Десятичное число ('+str(i)+')')
print(l2)

d={}
l=['a','b','c']
d=dict.fromkeys(l)
print(d)
s=input("side", )

    
for key in d:
      if key==s:
          pass
      else:
          d[key]=int(input("input<  ",  ))
print(d)

from math import *        
    
if not d['a']:
    print("a:",sqrt(d['c']**2-d['b']**2))
elif not d['b']:
    print("ba:",sqrt(d['c']**2-d['a']**2))
elif not d['c']:
    print("c:",sqrt(d['a']**2+d['b']**2))

def evkl(x,y):
    return sqrt((y[1]-x[1])**2+(y[0]-x[0])**2)

print(evkl((5,3), (10,3)))
