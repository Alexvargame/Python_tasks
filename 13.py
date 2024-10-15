
str_ = input()
matrix = []
matrix.append([])
print(matrix, str_)
m=str_.split()
print(m)
j=0
for i in range(len(m)+1):
    for j in range(len(m)+1):
        if j>i:
            print('i', i, 'j', j, 'm', m[i:j]) 
            matrix.append(m[i:j])
matrix= sorted(matrix, key=len)
print(matrix)

    



