from math import sqrt

def countPrimes(n):
    if n < 2:
        return 0
    numbers = [False, False] + [True]*(n-2)
    print('NUMBERS INIT', numbers)
    for p in range(2, int(sqrt(n))+1):
        print('p_pnum', p, numbers[p])
        if numbers[p]:
            for mult in range(p*p, n, p):
                print(mult)
                numbers[mult] = False
    print(numbers)
    return sum(numbers)


def main():

    print(countPrimes(10))


    
    
  
    
if __name__ == "__main__":
    main()
