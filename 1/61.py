#+=1
i=1
count=0
count1=0
sum1=0
pr=1
num=[]
while i>=0:
    m=int(input())
    if m==5555:
        break
    else:
        num.append(m)
        if i%2==0:
            pr=pr*m
            count1+=1
        else:
            sum1=sum1+m
            count+=1
    i+=1
print(num)
print(count, sum1, count1, pr)


