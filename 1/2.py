import datetime
l=[]
a=int(input())
l.append(a)
b=int(input())
l.append(b)
c=int(input())
l.append(c)
print(l)
max=l[0]
min=l[0]
for i in range(1,len(l)):
    if max<l[i]: max=l[i]    
print(max)
for i in range(len(l)):
    if min>l[i]: min=l[i]    
print(min)
