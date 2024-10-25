lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
sum_=0
for i in range(len(lst)):
    if lst[i]<30 and lst[i]%3==0:
        print(lst[i])
    else: sum_=sum_+lst[i]
print(sum_)
