
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(a, b)
#sum_=0
fib=[1,1]
for i in range(2,100):
    fib.append(fib[i-2]+fib[i-1])
    
print(fib)
print(len(fib))
    



