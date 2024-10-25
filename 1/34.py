import math
l=[1,2,3,4,5,6,7,8,9]
l1=[]
"""
a=int(input())
l.append(a)
b=int(input())
l.append(b)
c=int(input())
l.append(c)
m=int(input())
l1.append(m)
k=int(input())
l1.append(k)
"""

l1[0:len(l)]=l[len(l)//2:]
print(l1)
l1[len(l)+1:]=l[0:len(l)//2]
    
print(l, l1)
