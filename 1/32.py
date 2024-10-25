import math
l=[1,2,3,4,5,6,7,8,9]

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
if len(l)%2==0: len_=len(l)
else:len_=len(l)-1
i=0
while i in range(len_):
    print(l[i],l[i+1])
    l[i],l[i+1]=l[i+1],l[i]
    i=i+2
    
print(l)
