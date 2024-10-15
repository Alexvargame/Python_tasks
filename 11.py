n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
print(last + 1)
