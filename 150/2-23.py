n=int(input("n:",  ))

def sums(n):
    if n>0:
        nl=list(str(n))
        for i in range(len(nl)):
            n=n-int(nl[i])
        sums(n)
sums(n)

numb=1342359
dig=[0,1,2,3,4,5,6,7,8,9]
setnumb=set(list(str(numb)))
for d in dig:
    if str(d) in setnumb:
        pass
    else: print(d)
    
lst1=[1,-2,-4]
lst2=[]
lst3=[]
for i in range(len(lst1)):
   for j in range(len(lst1)):
        if i!=j:
            t=(lst1[i],lst1[j])
            
            t1=abs(lst1[i]-lst1[j])
            lst3.append(t1)
            
            lst2.append(t)

print(lst2)
print(lst3)

prog=[2,8,14,20]
a=prog[1]-prog[0]
h=prog[1]/prog[0]
for i in range(2, len(prog)):
        if prog[i]==(prog[i-1]+a):
            pass
        else:
            print("Not A")
            break
        print("A")

for i in range(2,len(prog)):
    if prog[i]==(prog[i-1]*h):
           pass
    else:
           print("Not G")
           break
    print("G")

