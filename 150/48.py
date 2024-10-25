from random import randint
"""
n=int(input("n ", ))
lst=[]
for i in range(len(str(n))):
    lst.append(str(n)[i])

print(int(('').join(sorted(lst)[::-1]))-int(('').join(sorted(lst))))

n1=int(input("n1  ", ))
lst1=[]
def isprime(a):
    if a>0:
        for i in range(2, int(a/2)+1):
            if(a%i)==0:
                return False
                break
        else: return True
    else:return False
for i in range(3, int(n1/2)+1,2):
    if isprime(i) and isprime(n1-i):
        t=(i, n1-i)
        lst1.append(t)
print(lst1, len(lst1))
"""

ll=[]
n2=int(input("n2:", ))
for i in range(n2):
    ll1=[]
    for j in range(n2):
        k=randint(0,100)
        ll1.append(k)
    ll.append(ll1)
print(ll)

for i in range(n2):
        k=sum(ll[i])
        ll[i].append(k)
        
print(ll)
ll1=[]
for i in range(n2+1):

        sum_=0
        for j in range(n2):
            sum_=sum_+ll[j][i]
        ll1.append(sum_)
ll.append(ll1)
print(ll)
