import math
l=[1,3,2,-3,4,0,0,5,6,7,8,9]
print(l)


l1=l.copy()
count=0
for i in range(len(l1)):
    if l1[i]>0: count+= 1
l1.insert(0, count)
l1.insert(0, sum(l1))
print(l1)

l1=l.copy()

k=int(input())
m=int(input())
l1 = l1[:k] + l1[k+m:]

print(l1)

l1=[]
for i in range(len(l)):
    if l[i]!=0: l1.append(l[i])
print(l1)


l1=l.copy()

for i in range(len(l)):
    if l[i]<0: l1.insert(i+1, l[i]**2) 
print(l1)

l1=[]

for i in range(len(l)):
    if l[i]<0:
        l1=l[:i]
        break
l1=sorted(l[:i])
if l[:i]==l1: print("Y")
else: print("N")

l1=[]
l2=[]
for i in range(len(l)):
    if l[i]>0:
        l1.append(l[i])
    else: l2.append(l[i])
    
print(l1, l2)

l1=l.copy()
count=0
count1=0
for i in range(len(l1)):
    if l1[i]<0: count+= 1
    elif l1[i]>0:count1+= 1
if count1>count:
    for i in range(count1-count):
        l1.append(1)

print(l1)

l1=l.copy()
sum_=0
sum_1=0
for i in range(len(l1)):
    if l1[i]>0: sum_+= l1[i]
    elif l1[i]<0:sum_1+= l1[i]

if sum_>-sum_1: l1.append(-(sum_+sum_1))
else:l1.append(-(sum_1-sum_))
print(sum_, sum_1)
print(l1)

l1=l.copy()
count=0
t=int(input())
for i in range(len(l1)):
    if l1[i]>0: count+= 1

for i in range(len(l1)):
    if l1[i]>0: l1[i]=l1[i]+ t/count


print(l1)

l1=l.copy()
b=int(input())
c=int(input())

print(l1[:b]+l1[c:])

l1=l.copy()
for i in range(len(l)):
    if l[i]==0:
        l1.pop(i)
        l1.insert(i, l[i-1]+l[i-2])


print(l1)

for i in range(len(l)):
    if l[i]==0 and l[i+1]==0 :
        print("Y")
        break

l1=l.copy()
count=0
count1=0
sum_=0
for i in range(len(l1)):
    if l1[i]!=0 and l1[i]%3==0:
        count+= 1
        if l1[i]!=0 and l1[i]%2==0:
            sum_=sum_+ l1[i]
            count1+= 1
        
    elif l1[i]!=0 and l1[i]%2==0:
            sum_=sum_+ l1[i]
            count1+= 1
print(count, count1, sum_)
l1.insert(0,count)
l1.append(sum_/count1)
print(l1)
