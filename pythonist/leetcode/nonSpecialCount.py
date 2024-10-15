from math import sqrt

def nonSpecialCount(l, r):
    if r < 2:
        return 0
    numbers = [False]*2 + [True]*(r-2)
    for p in range(2, int(sqrt(r))+1):
        if numbers[p]:
            for mult in range(p*p, r, p):
                numbers[mult] = False
    prime_ind = [i for i in range(len(numbers)) if numbers[i] and i**2 in range(l, r+1)]
    print(numbers, prime_ind)
    print([i for i in prime_ind if i*i in range(l, r+1)])


    return r-l+1 - len(prime_ind)


def main():

    print(nonSpecialCount(4, 16))


    
    
  
    
if __name__ == "__main__":
    main()
