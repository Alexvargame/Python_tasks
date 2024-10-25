from datetime import *
import random
"""
n=int(input())
a=input()

t=tuple(a)
t1=tuple(t[i] for i in range(len(t)) if i%n==0)
print(t1)
n1=int(input())
t2=tuple(str(n1)[i] for i in range(len(str(n1))))
print(t2)
"""
A=[[(j+1)*10+i+1 for i in range(5)] for j in range(3)]
print(A)
l=[1,3,4,4,5,4]
def lis(l):
    l1=[]
    l1.append(max(l))
    l1.append(l.index(max(l)))
    return l1
print(lis(l))
l2=[]
for i in range(10):
    l2.append(random.randint(0,10))
print(l2)
for j in range(0,(len(l2))//2*2,2):
    for i in range(j,(len(l2))//2*2,2):
        if l2[j]<l2[i]:
            l2[j],l2[i]=l2[i],l2[j]
for j in range(1,(len(l2))//2*2,2):
    for i in range(j,(len(l2))//2*2,2):
        if l2[j]>l2[i]:
            l2[j],l2[i]=l2[i],l2[j]
            
print(l2)    
l3=[]
for i in range(10):
    l3.append(random.randint(0,10))
print(l3)
for i in range(0,(len(l3)+3)//2*2,3):
        l3.insert(i+1, l3[i]+l3[i+1])
print(l3)
l4=[]
l5=[]
for i in range(10):
    l4.append(random.randint(0,10))
    l5.append(random.randint(0,10))
print(l4, l5)
l6=[]
for i in range(len(l4)):
    l6.append(l4[i])
    l6.append(l5[i])
print(l6)
