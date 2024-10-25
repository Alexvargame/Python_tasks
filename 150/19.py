s=input("s:",)
s1=input("s1:",)
if s.find(s1)!=0:

    s=s1+s
    print(s)
else: print(s)
n=int(input("n", ))
sum_=""
for i in range(n):
    sum_=sum_+s
print(sum_)
