"""
str_='google.com'
l=[]
for i in range(len(str_)):
    l.append(str_[i])

c={}
for i in l:
    c[i]= l.count(i)
print(c)

str1=input("str", )
if len(str1)<2:
    print("{}")
else:
    print(str1[0:2]+str1[-2:])
s1=input("s1", )
s2=input("s2", )

s3=s1.replace(s1[0],s2[0])+' '+s2.replace(s2[0],s1[0])
print(s3)

s=input("s", )
if s.find('not')==s.find('bad')-4:
    print(s.replace('not bad', 'good'))

s=input("s", )
l=[]
n=int(input("n",))
for i in range(len(s)):
    if i!=n:
        l.append(s[i])
s1=('').join(l)
print(s1)

s=input("s", )
ll=s.split(' ')

c={}
for i in ll:
    c[i]= ll.count(i)
print(c)

s=input("s", )
ll=s.split(',')
print(ll)
print((',').join(sorted(ll)))
"""
s=input("s", )
n=int(input("n", ))

def insert_end(s, n):
    s1=''
    for i in range(n):
        s1=s1+s[len(s)-n::]
    print(s1)
def first_l(s,n):
    print(s[:n])
first_l(s,n)
insert_end(s,n)
     
