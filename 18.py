
a = list(map(int, input().split()))
a= sorted(a)
str_=''
print(a)
for i in range(len(a)):
    str_=str_ +str(a[i])
print(str_)

