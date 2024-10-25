import math
l=[]
l1=[]

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

print(l, min(l))
print(l1, min(l1))
l.sort()
def d(l, l1):
    if (min(l1)<min(l) or l[len(l1)]>max(l1)): print("N")
    else:print("1")
d(l,l1)
