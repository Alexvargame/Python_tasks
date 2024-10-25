#+=1
from datetime import *
m=int(input())
lists=[]
ls=[]
str_=''
for i in range(m):
    s=str(input())
    lists.append(s)
    ls.append(len(s))
print(max(ls))
for i in range(len(lists)):
    print('*'*(max(ls)-len(lists[i]))+lists[i])
print("-----------------")

for i in range(len(lists)):
    str_=str_+lists[i]+' '
print(str_)
print("-----------------")

glas=['a','e','i','o','y']
lgl=[]

for i in range(len(lists)):
    count=0
    for l in lists[i]:
        if l in glas:
            count+= 1
    lgl.append(count)
print(lgl)
print("-----------------")


ss=str(input())
lgll=[]
#####################
for i in range(len(lists)):
            count=0
            j=0
            while j in range(len(lists[i])):
                if lists[i].find(ss,j)==-1:
                    break
                else:
                    #print(lists[i].find(ss, j), j)
                    count+= 1
                    
                    j=lists[i].find(ss,j)+len(ss)
                    #print(j, count)

            lgll.append(count)
print(lgll)
print("-----------------")
"""
asswdas
asaws
asa
wd
"""
ss=str(input())

list1=lists.copy()
for i in range(len(lists)):
    list1[i]=lists[i].replace(ss,"")

print(list1)
print("-----------------")


for i in range(len(lists)):
    if len(lists[i])%2!=0:
        print(lists[i][len(lists[i])//2])
print("-----------------")      

for i in range(len(lists)):
    list1=[]
    for j in range(len(lists[i])): 
        list1.append(lists[i][j])
    print((" ").join(list1))
print("-----------------")                     

      
for i in range(len(lists)):
    list1=[]
    list1=lists[i].split('<>')
    for j in range(0,len(list1),2):
        list1.insert(j+1,str(datetime.now()))
    print(("").join(list1))
print("-----------------")

for i in range(len(lists)):
    list1=[]
    list1=lists[i].split(' ')
    print(list1, len(list1)-1)
    
print("-----------------")

list1=lists.copy()
for i in range(len(lists)):
    list1[i]=lists[i].replace('?',"*")

print(list1)
print("-----------------")



