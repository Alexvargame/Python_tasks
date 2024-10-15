#from itertools import permutations

def permutations1(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    print(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    print(indices)
    cycles = list(range(n, n-r, -1))
    print(cycles)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                #print('1',int(''.join(pool[i] for i in indices[:r])),int(iterable))
                if int(''.join(pool[i] for i in indices[:r]))<int(iterable):
                    yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
def next_smaller(n):
    
    for item in permutations1(str(n),len(str(n))):
        if  ''.join(item)<str(n) and item[0]!='0':
            return  ''.join(item)
    return -1
##    if not [''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) and item[0]!='0']:
##        return -1
##    return int(max([''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) ]))
            
def main():

    print(list(next_smaller(str(4973))))
    #print(next_smaller(907))
    #print(next_smaller(100))
  
 
if __name__ == "__main__":
    main()


###
