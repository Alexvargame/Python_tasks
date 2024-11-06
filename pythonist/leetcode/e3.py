l = 1
r = num // 2 + 1
while l <= r:
    print('b', s, l, r)
    if num % l == 0:
        s += l
        s += num // l
        r = num // l
    l += 1
    print('af', s, l, r)
if s + 1 == num:
    return True
return False