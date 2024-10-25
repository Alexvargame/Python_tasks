from datetime import *

n=int(input())
print(len(str(n)))
str1=''
for i in str(n):
    print(i)
    i=9-int(i)
    str1=str1+str(i)
print(str1)
str1=''
l=[1,2,4,5,8,3,9,11,12,15]
for i in l:
    str1=str1+str(i)
print(str1)
sum_=0
n1=int(input())
for i in range(n1):
    if i not in l:
        sum_=sum_+i

print(sum_)




      
