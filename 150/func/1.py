a,b,c=3,12,4
def max_(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    return max(l)
print(max_(a,b,c))
l=[8, 2, 3, 0, 7]
def sum_(l):
    return(sum(l))
print(sum(l))
s="1234abcd"
def revers(s):
    l1=[]
    for i in range(len(s)):
        l1.append(s[i])
    print(l1)
    return ('').join(l1[::-1])
print(revers(s))
l=[2,3,3,3,3,4,5]
def uniq(l):
    s=set(l)
    return list(s)
print(uniq(l))
num=7
def perf(num):
    l=[]
    for i in range(1,num):
        if num%i==0:
            l.append(i)
    if sum(l)==num:
        return True
    else: return False
print(perf(num))

num=1000
def perf(num):
    l1=[]
    for j in range(num):
        l=[]
        for i in range(1,j):
            if j%i==0:
                l.append(i)
        if sum(l)==j:
            l1.append(j)
    return l1
print(perf(num))
n=6
l=[1,1]
def print_(l,n):
    l1=[]
    for i in range(len(l)-1):
        l1.append(l[i]+l[i+1])
    l1.insert(0,1)
    l1.append(1)
    print(l1)
    if len(l1)<n:
        print_(l1,n)
    
print_(l,n)
