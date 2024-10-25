import math
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

p=sum(l)
print(p)
sq=math.sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c))
print(sq)
