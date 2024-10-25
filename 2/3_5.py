num=int(input("num:", ))
print(num)
num_str=str(num)
sum=0
for i in range(len(num_str)):
    sum=sum+int(num_str[i])
print(sum)
