from datetime import *
import random

l=[3,4]
l1=[1,3,4,5,6]
len_=max(len(l1), len(l))
def ad(l):
    if len(l)<len_:
        l.extend(l[:len_-len(l)])
        ad(l)
    return (l)
print(ad(l))
def fr(l, l1):
    sum_=0   
    ad(l)
    ad(l1)
    for i in range(len_):
        if l[i] and l1[i]:
            sum_=sum_+l[i]*l1[i]
    return sum_
print(fr(l,l1))

def nech(l):
    l2=[]
    for i in l:
        if i%2!=0:
            l2.append(i)
    return l2
print(nech(l))

def arg(*arg):
    li=[]
    li.append(max(arg))
    li.append(min(arg))
    li.append(sum(arg)/len(arg))
    return(li)

print(arg(1,2,3))
print(arg(1))
print(arg(3,4))

def tt(txt, *a):
    ttxt=''
    for i in a:
        ttxt=ttxt+txt[i]
    return ttxt
print(tt("jshdflkwjhlwke", 1,3,1,4,2 ))
print(tt("addddddddddd", 1,1,1))

def f(n,m):
    l=[]
    for i in range(n, m):
        l.append(i**2)
    return(sum(l)/len(l))
def sec(f,n,m):
    it=0
    for i in range(m-n):
         print(f(i,m))
         it=f(n,m)+it
    return it
print(sec(f, 2,6))
#print(sec(f, 1,10))
        
