 
t = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(t)):
    t[i]=t[i][:1]+(100,)

print(t)

print("---")

t=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
t1=[]
for i in range(len(t)):
    if len(t[i])!=0:
        t1.append(t[i])
print(t1)
print("---")

t= [('item1', '12 .20 '), (' item2 ', '15 .10'), ('item3', '24 .5 ')]
print(sorted(t, keys=t[i][1]))
