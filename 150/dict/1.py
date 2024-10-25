a= {0: 10, 1: 20}
a[2]=30
print(a)
print("-------")

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5: 50,6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
print("---")
a={}
n=6
for i in range(1,n):
    a[i]=i**2
print(a)
print("-----------")

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d1.update(d2)
print(d1)
