"""
for i in range(15, 50):
    if i%5==0 and i%7==0:
        print(i)
s=input("s", )
#print(s.reverse())
l=[1, 2, 3, 4, 5, 7, 8, 9]
count1, count2=0,0
for i in range(len(l)):
    if l[i]%2==0:
        count1=count1+1
    else: 
        count2=count2+1
print(count1, count2)
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'} ]
for i in datalist:
    print(i,  type(i))
print("_------")

n=int(input("n",))
m=int(input("m", ))
l1=[]
for i in range(n):
    l1.append([])
    for j in range(m):
        l1[i].append(i*j)
print(l1)
        
passw=input("passw", )
m=['$','#','@']
for i in passw:
    print('z'>i>'a', 'Z'<i<'A', '1'<i<'9' ,6<len(passw)<16, i in m)
    if not ('z'<i<'a' or 'Z'<i<'A' or '1'<i<'9' or 6>len(passw) or len(passw)>16 or i in m):
        print("n")
else: print("y")
"""
print("____")

for i in range(100,400):
    for j in range(len(str(i))):
        if (int(str(i)[j]))%2!=0:
            break
    else: print(str(i), end=",")
    
