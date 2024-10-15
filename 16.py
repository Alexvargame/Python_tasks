
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(a, b)
sum_=0
for i in range(len(a)):
    print('i', i, 'b', b[i])
    a.insert(2*i+1, b[i])
print(a)

    



