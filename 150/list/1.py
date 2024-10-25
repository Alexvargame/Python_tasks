l=[1,3,4,25]
print(sum(l), max(l))
print([i*i for i in l])

l1=['abc', 'xyz', 'aba', '21']
c=0
print(len(l1))
for i in range(len(l1)):
    if len(l1[i])>=2 and l1[i][0]==l1[i][-1]:
           c=c+1
print(c)
print(l+l1, set(l+l1), len(set(l+l1)),len(l),len(l1))
if len(set(l+l1))<(len(l)+len(l1)):print("y")
else: print("n")
lst=[i*i for i in range(31)]
print(lst[0:5]+lst[-5:])
print(lst[5:])


import itertools
print(list(itertools.permutations([1,2,3])))

def konk(lst, n):
    lst1=[]
    for i in range(len(lst)):
        for j in range(1,n+1):
                lst1.append(str(lst[i])+str(j))
    return lst1
        
konk(['w','b',1],4)            

keys=['color_name', 'color_code']

color=["Черный", "Красный", "Бордовый", "Желтый"]
code=["# 000000", "# FF0000", "# 800000", "# FFFF00"]
lst4=[]
for i in range(len(color)):
        for j in range(i,len(code)):
            c={}
            c[keys[0]]=color[i]
            c[keys[1]]=code[j]
            lst4.append(c)
            break
print(lst4)

